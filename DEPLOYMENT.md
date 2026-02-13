# (J)ai Kisan Web Application - Deployment Guide

## Overview

This guide covers deploying the (J)ai Kisan web application with all its features including user registration, OTP verification, payment integration, and agricultural recommendations.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A server with at least 512MB RAM
- (Optional) Domain name with SSL certificate for production

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/phildass/Jai_Kisan.git
cd Jai_Kisan
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and configure the following:

```bash
# Required for production
SECRET_KEY=your-randomly-generated-secret-key
FLASK_ENV=production
DATABASE_URI=sqlite:///jai_kisan.db  # Or PostgreSQL/MySQL URI

# Required for OTP functionality
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890

# Required for payment functionality
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret

# Optional: Google Sign-In
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 4. Initialize the Database

The database will be automatically created when you first run the application.

```bash
python app.py
```

## Production Deployment

### Option 1: Using Gunicorn (Recommended)

1. Install Gunicorn:

```bash
pip install gunicorn
```

2. Run the application:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 2: Using uWSGI

1. Install uWSGI:

```bash
pip install uwsgi
```

2. Create `uwsgi.ini`:

```ini
[uwsgi]
module = app:app
master = true
processes = 4
socket = /tmp/jai_kisan.sock
chmod-socket = 660
vacuum = true
die-on-term = true
```

3. Run:

```bash
uwsgi --ini uwsgi.ini
```

### Option 3: Using systemd (Linux Service)

1. Create `/etc/systemd/system/jai-kisan.service`:

```ini
[Unit]
Description=(J)ai Kisan Web Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/Jai_Kisan
Environment="PATH=/path/to/venv/bin"
EnvironmentFile=/path/to/Jai_Kisan/.env
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

2. Enable and start:

```bash
sudo systemctl enable jai-kisan
sudo systemctl start jai-kisan
```

## Nginx Configuration (Reverse Proxy)

Create `/etc/nginx/sites-available/jai-kisan`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/Jai_Kisan/static;
        expires 30d;
    }

    location /public {
        alias /path/to/Jai_Kisan/public;
        expires 30d;
    }
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/jai-kisan /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## SSL Certificate (HTTPS)

Using Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Third-Party Service Setup

### Twilio (OTP SMS)

1. Sign up at https://www.twilio.com
2. Get your Account SID, Auth Token, and Phone Number
3. Update `.env` with these credentials
4. Uncomment the Twilio integration code in `app.py` (line ~87)

### Razorpay (Payment Gateway)

1. Sign up at https://razorpay.com
2. Get your API Key ID and Secret
3. Update `.env` with these credentials
4. Uncomment the Razorpay integration code in `app.py` (line ~106)
5. Update payment page template with Razorpay SDK

### Google OAuth (Optional)

1. Create project at https://console.cloud.google.com
2. Enable Google+ API
3. Create OAuth 2.0 credentials
4. Update `.env` with Client ID and Secret
5. Implement OAuth flow in `/google-auth` route

## Database Migration (SQLite to PostgreSQL)

For production, it's recommended to use PostgreSQL:

1. Install PostgreSQL:

```bash
sudo apt install postgresql postgresql-contrib
pip install psycopg2-binary
```

2. Create database:

```bash
sudo -u postgres psql
CREATE DATABASE jai_kisan;
CREATE USER jai_kisan_user WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE jai_kisan TO jai_kisan_user;
\q
```

3. Update `.env`:

```bash
DATABASE_URI=postgresql://jai_kisan_user:your-password@localhost/jai_kisan
```

## Monitoring and Logging

### Application Logs

Configure logging in `app.py`:

```python
import logging
logging.basicConfig(
    filename='/var/log/jai-kisan/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
```

### System Monitoring

Use tools like:
- **Supervisor**: Process management
- **Sentry**: Error tracking
- **New Relic**: Performance monitoring

## Backup Strategy

### Database Backup

Daily backup script:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
sqlite3 /path/to/jai_kisan.db ".backup '/backups/jai_kisan_$DATE.db'"
# For PostgreSQL:
# pg_dump jai_kisan > /backups/jai_kisan_$DATE.sql
```

Add to crontab:

```bash
0 2 * * * /path/to/backup-script.sh
```

## Security Checklist

- [ ] SECRET_KEY is randomly generated and secure
- [ ] FLASK_ENV is set to 'production'
- [ ] Debug mode is disabled
- [ ] HTTPS is enabled with valid certificate
- [ ] Firewall is configured (allow only 80, 443, SSH)
- [ ] Database credentials are secure
- [ ] Regular security updates applied
- [ ] File permissions are restrictive
- [ ] API keys are kept secret
- [ ] Rate limiting is configured

## Troubleshooting

### Issue: Database locked

**Solution**: Use PostgreSQL instead of SQLite for production

### Issue: OTP not sending

**Solution**: Check Twilio credentials and account balance

### Issue: Payment failing

**Solution**: Verify Razorpay credentials and test mode settings

### Issue: Application not starting

**Solution**: Check logs in `/var/log/` or `tail -f /tmp/flask_final.log`

## Scaling Considerations

For high traffic:

1. **Load Balancer**: Use multiple Gunicorn workers behind Nginx
2. **Database**: PostgreSQL with connection pooling
3. **Caching**: Redis for session storage and caching
4. **CDN**: CloudFlare for static assets
5. **Queue**: Celery for background tasks (OTP, reports)

## Support

For issues or questions:
- GitHub Issues: https://github.com/phildass/Jai_Kisan/issues
- Documentation: https://github.com/phildass/Jai_Kisan/blob/main/DOCUMENTATION.md

---

**जय किसान! (Victory to the Farmers!)**

May your fields prosper and your soil stay healthy 🌾
