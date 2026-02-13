# (J)ai Kisan - Quick Setup Guide

**Important: This is a Python Flask application, NOT a Node.js application. There is no `package.json` or `yarn start` command.**

## Prerequisites

- **Python 3.7 or higher** (required)
- **pip** (Python package manager)
- **Git** (to clone the repository)

## Local Deployment - Step by Step

### 1. Clone the Repository

```bash
git clone https://github.com/phildass/Jai_Kisan.git
cd Jai_Kisan
```

### 2. Create a Virtual Environment (Recommended)

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

**Minimal configuration for local testing:**
Edit `.env` and set:

```bash
SECRET_KEY=dev-secret-key-change-in-production
FLASK_ENV=development
DATABASE_URI=sqlite:///jai_kisan.db
PORT=3050
```

**Note:** Twilio, Razorpay, and Google OAuth are optional for local development. The app will work without them, but OTP verification and payments won't function.

### 5. Start the Application

**Option A: Using Python directly (Development)**

```bash
python app.py
```

The application will start on `http://localhost:5000` (or port specified in .env)

**Option B: Using the start script**

```bash
chmod +x start.sh
./start.sh
```

**Option C: On a specific port (e.g., 3050)**

```bash
python app.py --port 3050
```

Or set in `.env`:
```bash
PORT=3050
```

### 6. Access the Application

Open your web browser and navigate to:
- **Local**: http://localhost:3050 (or your configured port)
- **Network**: http://YOUR_IP:3050

## Quick Test (No Installation)

If you just want to test the recommendation engine without the web interface:

```bash
# No dependencies needed - uses only Python standard library
python cli.py
```

Or try the demo:

```bash
python demo.py
```

## File Structure

```
Jai_Kisan/
├── app.py                    # Main Flask web application
├── jai_kisan_agent.py       # Core recommendation engine
├── cli.py                   # Command-line interface
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── data/                   # Crop, state, and fertilizer data
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript files
└── public/                 # Public assets (logos, images)
```

## Troubleshooting

### Error: "No module named 'flask'"

**Solution:** Install dependencies: `pip install -r requirements.txt`

### Error: "package.json not found" or "yarn: command not found"

**This is NOT a Node.js application!** Use Python commands instead:
- Instead of `npm install` → Use `pip install -r requirements.txt`
- Instead of `yarn start` → Use `python app.py`

### Error: "Address already in use"

**Solution:** Another process is using the port. Either:
1. Stop the other process
2. Change the port in `.env` file: `PORT=3050`

### Database errors on startup

**Solution:** Delete the existing database and let it recreate:
```bash
rm jai_kisan.db
python app.py
```

## Production Deployment

For production deployment (VPS/server), see [DEPLOYMENT.md](DEPLOYMENT.md) for:
- Nginx configuration
- SSL/HTTPS setup
- Systemd service
- Database migration to PostgreSQL
- Performance optimization

## DNS Configuration (for aienter.in or custom domains)

See the **DNS Configuration** section in [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on:
- Setting A records
- Nginx server blocks
- SSL certificates with Let's Encrypt
- Removing default hosting provider pages

## Need Help?

1. Check [DOCUMENTATION.md](DOCUMENTATION.md) for complete feature documentation
2. Review [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
3. Open an issue on GitHub: https://github.com/phildass/Jai_Kisan/issues

---

**जय किसान! (Victory to the Farmers!)**

*May your fields prosper and your soil stay healthy* 🌾
