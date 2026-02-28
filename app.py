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
import re

import math

from dotenv import load_dotenv

from jai_kisan_agent import JaiKisanAgent
from voice_api import get_voice_api, get_factory_instance

# Load environment variables from .env file
load_dotenv()

# Email validation regex (RFC 5322 simplified)
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///jai_kisan.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# CSRF token context processor
@app.context_processor
def inject_csrf_token():
    """Inject a CSRF token into all templates."""
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return {'csrf_token': session['csrf_token']}

def validate_csrf(token):
    """Validate the CSRF token from form submission."""
    return token and token == session.get('csrf_token')

# Initialize Jai Kisan Agent
jai_kisan_agent = JaiKisanAgent()

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=True)
    mobile = db.Column(db.String(15), unique=True, nullable=True)
    state = db.Column(db.String(50), nullable=True)
    district = db.Column(db.String(50))
    occupation = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password_hash = db.Column(db.String(200))
    email_verified = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    phone = db.Column(db.String(20), nullable=True)
    last_login_at = db.Column(db.DateTime, nullable=True)
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


    kisan_points = db.Column(db.Integer, default=0)  # Gamification points

    # Voice API preference - new field for voice assistant provider selection
    # Default is 'bharati' for new users; existing users get NULL initially but UI defaults to 'bharati'
    voice_api_preference = db.Column(db.String(20), default='bharati')  # bharati, legacy


    
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
    
    def add_kisan_points(self, points, reason):
        """Add Kisan Points to user for contributions"""
        self.kisan_points += points


class Shop(db.Model):
    """Shop/Retailer information"""
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.String(50), unique=True, nullable=False)  # e-Urvarak ID
    name = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.String(100))
    mobile = db.Column(db.String(15))
    address = db.Column(db.String(500))
    district = db.Column(db.String(50))
    state = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    license_number = db.Column(db.String(100))
    is_verified = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float, default=0.0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)


class ShopInventory(db.Model):
    """Shop inventory for fertilizers"""
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.String(50), db.ForeignKey('shop.shop_id'), nullable=False)
    fertilizer_type = db.Column(db.String(50), nullable=False)  # Urea, DAP, MOP, etc.
    stock_bags = db.Column(db.Integer, default=0)
    price_per_50kg = db.Column(db.Float)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(20), default='api')  # api, crowdsourced


class CrowdsourcedReport(db.Model):
    """Farmer reports on shop status and stock"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shop_id = db.Column(db.String(50), db.ForeignKey('shop.shop_id'), nullable=False)
    report_type = db.Column(db.String(50), nullable=False)  # stock_available, shop_closed, price_update
    fertilizer_type = db.Column(db.String(50))  # If reporting specific fertilizer
    details = db.Column(db.String(500))
    is_verified = db.Column(db.Boolean, default=False)
    verification_count = db.Column(db.Integer, default=0)  # How many farmers confirmed this
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    points_awarded = db.Column(db.Integer, default=0)


class GroupBuying(db.Model):
    """Group buying aggregation"""
    id = db.Column(db.Integer, primary_key=True)
    fertilizer_type = db.Column(db.String(50), nullable=False)
    village = db.Column(db.String(100))
    district = db.Column(db.String(50))
    state = db.Column(db.String(50))
    total_bags_requested = db.Column(db.Integer, default=0)
    farmer_count = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='open')  # open, threshold_met, offer_sent, completed
    target_shop_id = db.Column(db.String(50), db.ForeignKey('shop.shop_id'))
    discount_offered = db.Column(db.Float, default=0.0)
    final_price_per_bag = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    closes_at = db.Column(db.DateTime)


class GroupBuyingParticipant(db.Model):
    """Individual farmer participation in group buying"""
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group_buying.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bags_requested = db.Column(db.Integer, nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_confirmed = db.Column(db.Boolean, default=False)


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
        # Validate CSRF token
        if not validate_csrf(request.form.get('csrf_token')):
            flash('Invalid request. Please try again.', 'error')
            return render_template('auth/register.html')

        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name', '').strip()
        phone = request.form.get('phone', '').strip()
        accept_terms = request.form.get('accept_terms')

        # Validation
        if not email or not password:
            flash('Email and password are required', 'error')
            return render_template('auth/register.html')

        # Email validation
        if not re.match(EMAIL_REGEX, email):
            flash('Invalid email address', 'error')
            return render_template('auth/register.html')

        # Password validation
        if len(password) < 8:
            flash('Password must be at least 8 characters', 'error')
            return render_template('auth/register.html')

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/register.html')

        if not accept_terms:
            flash('You must accept the Terms & Conditions', 'error')
            return render_template('auth/register.html')

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'error')
            return render_template('auth/register.html')

        # Create new user
        user = User(
            email=email,
            full_name=full_name or None,
            phone=phone or None,
            is_active=True,
            email_verified=False
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('auth/register.html')


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
        # Validate CSRF token
        if not validate_csrf(request.form.get('csrf_token')):
            flash('Invalid request. Please try again.', 'error')
            return render_template('auth/login.html')

        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        remember_me = request.form.get('remember_me')

        if not email or not password:
            flash('Email and password are required', 'error')
            return render_template('auth/login.html')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Invalid email or password', 'error')
            return render_template('auth/login.html')

        if not user.is_active:
            flash('Your account has been deactivated', 'error')
            return render_template('auth/login.html')

        if not user.check_password(password):
            flash('Invalid email or password', 'error')
            return render_template('auth/login.html')

        # Update last login timestamp
        user.last_login_at = datetime.utcnow()
        db.session.commit()

        login_user(user, remember=bool(remember_me))
        if remember_me:
            session.permanent = True

        flash('Welcome back!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    """User logout"""
    logout_user()
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))


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


# Shop Discovery and Inventory Routes
@app.route('/shops')
@login_required
def shop_discovery():
    """Shop discovery page"""
    if not current_user.is_trial_active() and current_user.payment_status != 'paid':
        return redirect(url_for('payment'))
    
    return render_template('shop_discovery.html')


@app.route('/api/shops/nearby', methods=['POST'])
@login_required
def get_nearby_shops():
    """Get nearby shops based on location"""
    from data.shop_data import SAMPLE_SHOPS
    
    data = request.json
    user_lat = data.get('latitude')
    user_lng = data.get('longitude')
    radius_km = data.get('radius', 50)  # Default 50km radius
    state = data.get('state', current_user.state)
    
    # Calculate distance for each shop
    def calculate_distance(lat1, lon1, lat2, lon2):
        """Calculate distance between two coordinates using Haversine formula"""
        R = 6371  # Earth's radius in km
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    nearby_shops = []
    
    # Filter shops by state and calculate distance
    for shop in SAMPLE_SHOPS:
        if shop['state'] == state:
            if user_lat and user_lng:
                distance = calculate_distance(user_lat, user_lng, shop['latitude'], shop['longitude'])
                if distance <= radius_km:
                    shop_copy = shop.copy()
                    shop_copy['distance_km'] = round(distance, 1)
                    nearby_shops.append(shop_copy)
            else:
                # If no coordinates, return all shops in state
                shop_copy = shop.copy()
                shop_copy['distance_km'] = None
                nearby_shops.append(shop_copy)
    
    # Sort by distance if available
    if user_lat and user_lng:
        nearby_shops.sort(key=lambda x: x['distance_km'])
    
    return jsonify({'shops': nearby_shops})


@app.route('/api/shops/<shop_id>/inventory')
@login_required
def get_shop_inventory(shop_id):
    """Get inventory for a specific shop"""
    from data.shop_data import SAMPLE_SHOPS
    
    for shop in SAMPLE_SHOPS:
        if shop['id'] == shop_id:
            return jsonify({'inventory': shop['inventory'], 'shop': shop})
    
    return jsonify({'error': 'Shop not found'}), 404


@app.route('/api/crowdsource/report', methods=['POST'])
@login_required
def submit_crowdsource_report():
    """Submit crowdsourced report about shop/stock"""
    from data.shop_data import KISAN_POINTS_REWARDS
    
    data = request.json
    shop_id = data.get('shop_id')
    report_type = data.get('report_type')  # stock_available, shop_closed, price_update
    fertilizer_type = data.get('fertilizer_type')
    details = data.get('details', '')
    
    # Create report
    report = CrowdsourcedReport(
        user_id=current_user.id,
        shop_id=shop_id,
        report_type=report_type,
        fertilizer_type=fertilizer_type,
        details=details
    )
    
    # Award Kisan Points
    points = KISAN_POINTS_REWARDS.get(f'report_{report_type}', 5)
    report.points_awarded = points
    
    db.session.add(report)
    current_user.add_kisan_points(points, f"Report: {report_type}")
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'total_points': current_user.kisan_points,
        'message': f'Thank you! You earned {points} Kisan Points.'
    })


@app.route('/api/price-comparison')
@login_required
def price_comparison():
    """Get price comparison for branded vs kifayati options"""
    from data.shop_data import KIFAYATI_ALTERNATIVES, BRAND_TO_SALT_MAPPING
    
    fertilizer_type = request.args.get('type')  # e.g., "DAP", "Urea"
    
    if fertilizer_type in KIFAYATI_ALTERNATIVES:
        comparison = KIFAYATI_ALTERNATIVES[fertilizer_type]
        return jsonify({
            'fertilizer_type': fertilizer_type,
            'salt': comparison['kifayati_option']['salt'],
            'npk': comparison['kifayati_option']['npk'],
            'branded_average': comparison['branded_average_price'],
            'kifayati_option': comparison['kifayati_option'],
            'savings': comparison['kifayati_option']['savings_per_bag']
        })
    
    return jsonify({'error': 'Fertilizer type not found'}), 404


@app.route('/api/dosage-calculator', methods=['POST'])
@login_required
def dosage_calculator():
    """Calculate dosage based on crop, area, and growth stage"""
    from data.shop_data import DOSAGE_CALCULATION_RULES
    
    data = request.json
    crop = data.get('crop')
    area_hectares = float(data.get('area_hectares', 1.0))
    growth_stage = data.get('growth_stage')
    
    # Get dosage rules
    crop_rules = DOSAGE_CALCULATION_RULES.get(crop, DOSAGE_CALCULATION_RULES['default'])
    stage_rules = crop_rules.get(growth_stage, crop_rules.get('Field Preparation (Basal Dose)', {}))
    
    # Calculate dosages
    dosages = {}
    for fert_key, amount in stage_rules.items():
        if fert_key != 'area_factor':
            # Scale by area
            dosages[fert_key] = round(amount * area_hectares, 2)
    
    # Calculate number of bags needed (50kg per bag)
    bags_needed = {}
    for fert_key, kg_amount in dosages.items():
        if 'kg' in fert_key:
            fert_type = fert_key.replace('_kg', '').upper()
            bags_needed[fert_type] = {
                'kg_required': kg_amount,
                'bags_50kg': round(kg_amount / 50, 2),
                'bags_to_buy': int(math.ceil(kg_amount / 50))  # Round up to whole bags
            }
    
    return jsonify({
        'crop': crop,
        'area_hectares': area_hectares,
        'growth_stage': growth_stage,
        'dosages': dosages,
        'bags_needed': bags_needed,
        'recommendation': f"For {area_hectares} hectares of {crop} at {growth_stage}"
    })


@app.route('/api/group-buying/create', methods=['POST'])
@login_required
def create_group_buying():
    """Create or join a group buying request"""
    from data.shop_data import GROUP_BUYING_THRESHOLDS, KISAN_POINTS_REWARDS
    
    data = request.json
    fertilizer_type = data.get('fertilizer_type')
    bags_requested = int(data.get('bags_requested', 1))
    village = data.get('village', current_user.district)
    
    # Check if there's an open group for this fertilizer in the area
    existing_group = GroupBuying.query.filter_by(
        fertilizer_type=fertilizer_type,
        district=current_user.district,
        status='open'
    ).first()
    
    if existing_group:
        # Join existing group
        participant = GroupBuyingParticipant(
            group_id=existing_group.id,
            user_id=current_user.id,
            bags_requested=bags_requested
        )
        db.session.add(participant)
        
        # Update group totals
        existing_group.total_bags_requested += bags_requested
        existing_group.farmer_count += 1
        
        # Award points
        current_user.add_kisan_points(KISAN_POINTS_REWARDS['join_group_buying'], "Joined group buying")
        
        # Check if threshold is met
        threshold = GROUP_BUYING_THRESHOLDS.get(fertilizer_type, {})
        if (existing_group.total_bags_requested >= threshold.get('min_bags', 50) and
            existing_group.farmer_count >= threshold.get('min_farmers', 5)):
            existing_group.status = 'threshold_met'
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'group_id': existing_group.id,
            'total_bags': existing_group.total_bags_requested,
            'farmer_count': existing_group.farmer_count,
            'threshold_met': existing_group.status == 'threshold_met',
            'points_earned': KISAN_POINTS_REWARDS['join_group_buying']
        })
    else:
        # Create new group
        new_group = GroupBuying(
            fertilizer_type=fertilizer_type,
            village=village,
            district=current_user.district,
            state=current_user.state,
            total_bags_requested=bags_requested,
            farmer_count=1,
            closes_at=datetime.utcnow() + timedelta(days=7)  # 7 days to form group
        )
        db.session.add(new_group)
        db.session.flush()  # Get the group ID
        
        # Add as first participant
        participant = GroupBuyingParticipant(
            group_id=new_group.id,
            user_id=current_user.id,
            bags_requested=bags_requested
        )
        db.session.add(participant)
        
        # Award points
        current_user.add_kisan_points(KISAN_POINTS_REWARDS['join_group_buying'], "Started group buying")
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'group_id': new_group.id,
            'total_bags': new_group.total_bags_requested,
            'farmer_count': new_group.farmer_count,
            'threshold_met': False,
            'points_earned': KISAN_POINTS_REWARDS['join_group_buying']
        })


@app.route('/api/group-buying/status/<int:group_id>')
@login_required
def get_group_buying_status(group_id):
    """Get status of a group buying request"""
    from data.shop_data import GROUP_BUYING_THRESHOLDS
    
    group = GroupBuying.query.get_or_404(group_id)
    threshold = GROUP_BUYING_THRESHOLDS.get(group.fertilizer_type, {})
    
    return jsonify({
        'group_id': group.id,
        'fertilizer_type': group.fertilizer_type,
        'total_bags': group.total_bags_requested,
        'farmer_count': group.farmer_count,
        'status': group.status,
        'threshold': {
            'min_bags': threshold.get('min_bags', 50),
            'min_farmers': threshold.get('min_farmers', 5),
            'discount_percent': threshold.get('discount_percent', 0)
        },
        'progress': {
            'bags_percent': min(100, (group.total_bags_requested / threshold.get('min_bags', 50)) * 100),
            'farmers_percent': min(100, (group.farmer_count / threshold.get('min_farmers', 5)) * 100)
        },
        'discount_offered': group.discount_offered,
        'final_price': group.final_price_per_bag
    })


@app.route('/public/<path:filename>')
def serve_public(filename):
    """Serve files from public directory"""
    from flask import send_from_directory
    return send_from_directory('public', filename)



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

# Voice API Endpoints
@app.route('/api/voice/query', methods=['POST'])
@login_required
def voice_query():
    """
    Handle voice query from farmer.
    Accepts voice call events and processes them.
    """
    try:
        call_event = request.get_json()
        
        # Get farmer profile
        farmer_profile = {
            'mobile': current_user.mobile,
            'name': current_user.full_name,
            'state': current_user.state,
            'voice_api_preference': current_user.voice_api_preference
        }
        
        # Get voice API factory
        factory = get_factory_instance()
        
        # Process the voice query
        result = factory.receive_voice_query(call_event)
        
        if result.get('success'):
            # Extract the query text and use Jai Kisan Agent to generate response
            query_text = result.get('query_text', '')
            
            # Here you would process the query with JaiKisanAgent
            # For now, just return the processed query
            return jsonify({
                'success': True,
                'query_received': query_text,
                'provider': result.get('provider'),
                'message': 'Query processed successfully'
            })
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/voice/send', methods=['POST'])
@login_required
def voice_send():
    """
    Send voice answer to farmer.
    Accepts text response and sends it as voice message.
    """
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        # Get farmer profile
        farmer_profile = {
            'mobile': current_user.mobile,
            'name': current_user.full_name,
            'state': current_user.state,
            'voice_api_preference': current_user.voice_api_preference
        }
        
        # Get voice API factory and send message
        factory = get_factory_instance()
        result = factory.send_voice_answer(message, farmer_profile)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/voice/status')
@login_required
def voice_status():
    """Get status of all voice API providers."""
    try:
        factory = get_factory_instance()
        status = factory.get_provider_status()
        
        # Add user's current preference
        status['user_preference'] = current_user.voice_api_preference
        status['user_state'] = current_user.state
        
        return jsonify(status)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/voice/preference', methods=['POST'])
@login_required
def set_voice_preference():
    """Update user's voice API preference."""
    try:
        data = request.get_json()
        preference = data.get('preference', '').lower()
        
        if preference not in ['bharati', 'legacy']:
            return jsonify({
                'success': False,
                'error': 'Invalid preference. Must be "bharati" or "legacy"'
            }), 400
        
        # Update user preference
        current_user.voice_api_preference = preference
        db.session.commit()
        
        return jsonify({
            'success': True,
            'preference': preference,
            'message': 'Voice API preference updated successfully'
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500



# Initialize database
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    # Only enable debug mode in development (not in production)
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
