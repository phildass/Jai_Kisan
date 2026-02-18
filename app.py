"""
(J)ai Kisan - Web Application
Flask-based web interface for the Jai Kisan agricultural consultant
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
import secrets
from jai_kisan_agent import JaiKisanAgent

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///jai_kisan.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize Jai Kisan Agent
jai_kisan_agent = JaiKisanAgent()

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)
    state = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50))
    occupation = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(200))
    google_id = db.Column(db.String(100), unique=True)
    otp = db.Column(db.String(6))
    otp_verified = db.Column(db.Boolean, default=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(20), default='trial')  # trial, paid, expired
    payment_date = db.Column(db.DateTime)
    # Location for neighborhood watch
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    # Relationships
    pest_reports = db.relationship('PestReport', backref='reporter', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_trial_active(self):
        """Check if 24-hour free trial is still active"""
        if self.payment_status == 'paid':
            return True
        trial_end = self.registration_date + timedelta(hours=24)
        return datetime.utcnow() < trial_end
    
    def get_trial_remaining(self):
        """Get remaining trial time in hours"""
        if self.payment_status == 'paid':
            return None
        trial_end = self.registration_date + timedelta(hours=24)
        remaining = trial_end - datetime.utcnow()
        return max(0, remaining.total_seconds() / 3600)


class PestReport(db.Model):
    """Model for storing pest/disease reports from farmers"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop = db.Column(db.String(100), nullable=False)
    pest_disease_name = db.Column(db.String(100), nullable=False)
    pest_disease_type = db.Column(db.String(20), nullable=False)  # 'pest' or 'disease'
    severity = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high', 'critical'
    pest_count = db.Column(db.String(50))  # e.g., "5-10 per leaf" or "20% infestation"
    symptoms = db.Column(db.Text)
    location = db.Column(db.String(200))  # District, Village
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    report_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # active, controlled, resolved
    photo_path = db.Column(db.String(500))  # Path to uploaded photo
    verified = db.Column(db.Boolean, default=False)  # Verified by expert
    
    def __repr__(self):
        return f'<PestReport {self.pest_disease_name} in {self.crop}>'


class DiseaseAlert(db.Model):
    """Model for storing disease risk alerts"""
    id = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(db.String(50), nullable=False)  # 'weather', 'neighborhood', 'seasonal'
    crop = db.Column(db.String(100), nullable=False)
    disease_name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100))  # State or District
    severity = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    description = db.Column(db.Text, nullable=False)
    preventive_measures = db.Column(db.Text)
    alert_date = db.Column(db.DateTime, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime)  # When alert is no longer relevant
    weather_conditions = db.Column(db.String(200))  # e.g., "High humidity, 25-30°C"
    active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<DiseaseAlert {self.disease_name} for {self.crop}>'


class CropLog(db.Model):
    """Model for storing farmers' crop cultivation logs"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop = db.Column(db.String(100), nullable=False)
    variety = db.Column(db.String(100))
    area_hectares = db.Column(db.Float)
    sowing_date = db.Column(db.Date)
    expected_harvest_date = db.Column(db.Date)
    current_stage = db.Column(db.String(100))
    location = db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='crop_logs')
    
    def __repr__(self):
        return f'<CropLog {self.crop} by User {self.user_id}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Helper functions for OTP and Payment
def send_otp_sms(mobile, otp):
    """Send OTP via SMS using Twilio (placeholder implementation)"""
    # In production, integrate with Twilio or other SMS service
    # For demo purposes, we'll just print it
    print(f"Sending OTP {otp} to {mobile}")
    # Uncomment below for actual Twilio integration:
    # from twilio.rest import Client
    # account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    # auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body=f"Your (J)ai Kisan OTP is: {otp}",
    #     from_=os.getenv('TWILIO_PHONE_NUMBER'),
    #     to=mobile
    # )
    return True


def create_payment_order(amount=11682):  # Amount in paise (₹116.82)
    """Create payment order using Razorpay (placeholder implementation)"""
    # In production, integrate with Razorpay
    # For demo purposes, return a mock order
    print(f"Creating payment order for ₹{amount/100}")
    # Uncomment below for actual Razorpay integration:
    # import razorpay
    # client = razorpay.Client(
    #     auth=(os.getenv('RAZORPAY_KEY_ID'), os.getenv('RAZORPAY_KEY_SECRET'))
    # )
    # order = client.order.create({
    #     'amount': amount,
    #     'currency': 'INR',
    #     'payment_capture': 1
    # })
    # return order
    return {'id': 'order_demo_123', 'amount': amount}


# Routes
@app.route('/')
def home():
    """Home/Landing page"""
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page"""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        mobile = request.form.get('mobile')
        state = request.form.get('state')
        district = request.form.get('district')
        occupation = request.form.get('occupation')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if not all([full_name, mobile, state, occupation, password]):
            flash('Please fill all required fields', 'error')
            return render_template('register.html')
        
        # Check if user already exists
        existing_user = User.query.filter_by(mobile=mobile).first()
        if existing_user:
            flash('Mobile number already registered', 'error')
            return render_template('register.html')
        
        # Generate OTP
        otp = str(secrets.randbelow(1000000)).zfill(6)
        
        # Create new user
        user = User(
            full_name=full_name,
            mobile=mobile,
            state=state,
            district=district,
            occupation=occupation,
            email=email,
            otp=otp
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Send OTP
        send_otp_sms(mobile, otp)
        
        # Store user_id in session for OTP verification
        session['pending_user_id'] = user.id
        flash('Registration successful! Please verify OTP sent to your mobile.', 'success')
        return redirect(url_for('verify_otp'))
    
    # Get states for dropdown
    from data.states_data import STATE_REGIONS
    states = []
    for region, region_states in STATE_REGIONS.items():
        states.extend(region_states)
    
    return render_template('register.html', states=states)


@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    """OTP verification page"""
    if 'pending_user_id' not in session:
        flash('Please register first', 'error')
        return redirect(url_for('register'))
    
    if request.method == 'POST':
        otp = request.form.get('otp')
        user_id = session.get('pending_user_id')
        user = User.query.get(user_id)
        
        if user and user.otp == otp:
            user.otp_verified = True
            db.session.commit()
            session.pop('pending_user_id', None)
            login_user(user)
            flash('OTP verified successfully! Welcome to (J)ai Kisan!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid OTP. Please try again.', 'error')
    
    return render_template('verify_otp.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        
        user = User.query.filter_by(mobile=mobile).first()
        
        if user and user.check_password(password):
            if not user.otp_verified:
                flash('Please verify your OTP first', 'error')
                session['pending_user_id'] = user.id
                return redirect(url_for('verify_otp'))
            
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid mobile number or password', 'error')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard - main app interface"""
    # Check trial status
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return redirect(url_for('payment'))
    
    trial_remaining = current_user.get_trial_remaining()
    
    # Get crops and states for dropdowns
    from data.crops_data import CROP_CATEGORIES
    from data.states_data import STATE_REGIONS
    
    states = []
    for region, region_states in STATE_REGIONS.items():
        states.extend(region_states)
    
    return render_template('dashboard.html', 
                         crop_categories=CROP_CATEGORIES,
                         states=states,
                         trial_remaining=trial_remaining)


@app.route('/get-recommendation', methods=['POST'])
@login_required
def get_recommendation():
    """Get fertilizer recommendation"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired. Please make payment to continue.'}), 403
    
    crop = request.json.get('crop')
    state = request.json.get('state')
    growth_stage = request.json.get('growth_stage')
    
    try:
        recommendation = jai_kisan_agent.generate_response(crop, state, growth_stage)
        return jsonify({'recommendation': recommendation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/payment')
@login_required
def payment():
    """Payment page for continuing after trial"""
    if current_user.payment_status == 'paid':
        flash('You already have an active subscription', 'info')
        return redirect(url_for('dashboard'))
    
    # Create payment order
    order = create_payment_order()
    
    return render_template('payment.html', 
                         order=order,
                         razorpay_key=os.getenv('RAZORPAY_KEY_ID', 'demo_key'))


@app.route('/payment-success', methods=['POST'])
@login_required
def payment_success():
    """Handle successful payment"""
    # In production, verify payment signature
    payment_id = request.form.get('payment_id')
    order_id = request.form.get('order_id')
    signature = request.form.get('signature')
    
    # Update user payment status
    current_user.payment_status = 'paid'
    current_user.payment_date = datetime.utcnow()
    db.session.commit()
    
    flash('Payment successful! You now have full access to (J)ai Kisan.', 'success')
    return redirect(url_for('dashboard'))


@app.route('/download')
@login_required
def download():
    """Download user's recommendation history or summary"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        flash('Trial expired. Please make payment to continue.', 'error')
        return redirect(url_for('payment'))
    
    # For demo, create a simple text file with user info
    content = f"""
(J)ai Kisan - User Report
========================

User: {current_user.full_name}
Mobile: {current_user.mobile}
State: {current_user.state}
Occupation: {current_user.occupation}
Registration Date: {current_user.registration_date.strftime('%Y-%m-%d %H:%M')}
Payment Status: {current_user.payment_status}

Thank you for using (J)ai Kisan!
जय किसान! (Victory to the Farmers!)
"""
    
    # Create temp file - it will be sent and then we clean it up
    import tempfile
    import os as os_module
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(content)
        temp_path = f.name
    
    try:
        return send_file(temp_path, 
                        as_attachment=True, 
                        download_name=f'jai_kisan_report_{current_user.id}.txt',
                        mimetype='text/plain')
    finally:
        # Clean up temp file after sending
        try:
            os_module.remove(temp_path)
        except:
            pass


@app.route('/google-auth')
def google_auth():
    """Google Sign-In (placeholder)"""
    # In production, implement Google OAuth flow
    flash('Google Sign-In is not yet implemented. Please use regular registration.', 'info')
    return redirect(url_for('register'))


@app.route('/public/<path:filename>')
def serve_public(filename):
    """Serve files from public directory"""
    from flask import send_from_directory
    return send_from_directory('public', filename)


# ==================== CROP HEALTH & MARKETPLACE ROUTES ====================

@app.route('/crop-health')
@login_required
def crop_health():
    """Crop Health & Pest Management Dashboard"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return redirect(url_for('payment'))
    
    # Get all crops for dropdown
    crops = jai_kisan_agent.get_all_crops()
    
    # Get recent alerts for user's region
    alerts = DiseaseAlert.query.filter_by(
        region=current_user.state,
        active=True
    ).order_by(DiseaseAlert.alert_date.desc()).limit(5).all()
    
    # Get nearby pest reports (within last 7 days)
    from datetime import timedelta
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    recent_reports = PestReport.query.filter(
        PestReport.report_date >= seven_days_ago,
        PestReport.location.like(f'%{current_user.district}%')
    ).order_by(PestReport.report_date.desc()).limit(10).all()
    
    return render_template('crop_health.html',
                         crops=crops,
                         alerts=alerts,
                         recent_reports=recent_reports,
                         user_state=current_user.state)


@app.route('/ipm-advisor', methods=['GET', 'POST'])
@login_required
def ipm_advisor():
    """IPM (Integrated Pest Management) Advisor"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired. Please make payment to continue.'}), 403
    
    if request.method == 'POST':
        crop = request.json.get('crop')
        pest_disease = request.json.get('pest_disease')
        pest_count = request.json.get('pest_count')
        
        try:
            recommendation = jai_kisan_agent.generate_ipm_recommendation(
                crop, pest_disease, pest_count
            )
            return jsonify({'recommendation': recommendation})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # GET request - show form
    crops = jai_kisan_agent.get_all_crops()
    return render_template('ipm_advisor.html', crops=crops)


@app.route('/pest-disease-info/<crop>')
@login_required
def pest_disease_info(crop):
    """Get pest and disease information for a specific crop"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired'}), 403
    
    info = jai_kisan_agent.get_crop_pests_diseases(crop)
    return jsonify(info)


@app.route('/check-chemical-ban', methods=['POST'])
@login_required
def check_chemical_ban():
    """Check if a chemical is banned"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired'}), 403
    
    chemical_name = request.json.get('chemical_name')
    
    if not chemical_name:
        return jsonify({'error': 'Chemical name required'}), 400
    
    result = jai_kisan_agent.check_chemical_ban_status(chemical_name)
    return jsonify(result)


@app.route('/weather-spray-check', methods=['POST'])
@login_required
def weather_spray_check():
    """Check if weather is suitable for spraying"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired'}), 403
    
    rainfall_forecast_hours = request.json.get('rainfall_forecast_hours')
    
    advisory = jai_kisan_agent.check_spray_timing_weather(rainfall_forecast_hours)
    return jsonify({'advisory': advisory})


@app.route('/report-pest', methods=['GET', 'POST'])
@login_required
def report_pest():
    """Report pest/disease sighting"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        if request.method == 'POST':
            return jsonify({'error': 'Trial expired'}), 403
        return redirect(url_for('payment'))
    
    if request.method == 'POST':
        crop = request.json.get('crop')
        pest_disease_name = request.json.get('pest_disease_name')
        pest_disease_type = request.json.get('pest_disease_type')
        severity = request.json.get('severity')
        pest_count = request.json.get('pest_count')
        symptoms = request.json.get('symptoms')
        latitude = request.json.get('latitude')
        longitude = request.json.get('longitude')
        
        # Create pest report
        report = PestReport(
            user_id=current_user.id,
            crop=crop,
            pest_disease_name=pest_disease_name,
            pest_disease_type=pest_disease_type,
            severity=severity,
            pest_count=pest_count,
            symptoms=symptoms,
            location=f"{current_user.district}, {current_user.state}",
            latitude=latitude or current_user.latitude,
            longitude=longitude or current_user.longitude
        )
        
        db.session.add(report)
        db.session.commit()
        
        # Check if we should create an alert for nearby farmers
        nearby_reports = PestReport.query.filter(
            PestReport.pest_disease_name == pest_disease_name,
            PestReport.crop == crop,
            PestReport.status == 'active',
            PestReport.location.like(f'%{current_user.district}%')
        ).count()
        
        if nearby_reports >= 3:  # If 3+ reports of same issue
            # Create alert
            alert = DiseaseAlert(
                alert_type='neighborhood',
                crop=crop,
                disease_name=pest_disease_name,
                region=current_user.district,
                severity=severity,
                description=f"Multiple farmers have reported {pest_disease_name} in {crop}. Take preventive measures immediately.",
                preventive_measures="Apply organic/preventive measures as recommended in IPM advisor.",
                expiry_date=datetime.utcnow() + timedelta(days=14)
            )
            db.session.add(alert)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Report submitted successfully. Thank you for helping the farming community!',
            'report_id': report.id
        })
    
    # GET request - show form
    crops = jai_kisan_agent.get_all_crops()
    return render_template('report_pest.html', crops=crops)


@app.route('/marketplace')
@login_required
def marketplace():
    """Agricultural inputs marketplace"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return redirect(url_for('payment'))
    
    return render_template('marketplace.html', user_state=current_user.state)


@app.route('/find-shops', methods=['POST'])
@login_required
def find_shops():
    """Find nearby shops for a product"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired'}), 403
    
    product_name = request.json.get('product_name')
    state = request.json.get('state', current_user.state)
    district = request.json.get('district', current_user.district)
    
    result = jai_kisan_agent.find_shops_for_product(product_name, state, district)
    return jsonify({'shops': result})


@app.route('/crop-rotation-check', methods=['POST'])
@login_required
def crop_rotation_check():
    """Check crop rotation compatibility"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return jsonify({'error': 'Trial expired'}), 403
    
    current_crop = request.json.get('current_crop')
    previous_crop = request.json.get('previous_crop')
    
    result = jai_kisan_agent.check_crop_rotation_compatibility(current_crop, previous_crop)
    return jsonify(result)


@app.route('/photo-diagnosis', methods=['GET', 'POST'])
@login_required
def photo_diagnosis():
    """Photo-based crop disease diagnosis (placeholder for CV model)"""
    # Check access
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        if request.method == 'POST':
            return jsonify({'error': 'Trial expired'}), 403
        return redirect(url_for('payment'))
    
    if request.method == 'POST':
        # TODO: Implement actual CV model integration
        # For now, return a placeholder response
        
        # Check if file was uploaded
        if 'photo' not in request.files:
            return jsonify({'error': 'No photo uploaded'}), 400
        
        file = request.files['photo']
        
        if file.filename == '':
            return jsonify({'error': 'No photo selected'}), 400
        
        # Placeholder response
        return jsonify({
            'success': True,
            'diagnosis': 'Photo received successfully',
            'message': 'CV model integration pending. Manual diagnosis: Please describe symptoms in IPM Advisor for recommendations.',
            'next_steps': [
                'Go to IPM Advisor',
                'Select your crop and describe symptoms',
                'Get 3-tier recommendations'
            ]
        })
    
    # GET request - show upload form
    return render_template('photo_diagnosis.html')


# Initialize database
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    # Only enable debug mode in development (not in production)
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
