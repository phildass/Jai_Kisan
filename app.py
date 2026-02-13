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


# Initialize database
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    # Only enable debug mode in development (not in production)
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
