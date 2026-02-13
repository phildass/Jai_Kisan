# (J)ai Kisan - Deployment Troubleshooting Guide

This guide addresses common issues encountered during deployment, including DNS configuration and server setup.

## Table of Contents

1. [Common Local Deployment Issues](#common-local-deployment-issues)
2. [DNS and Domain Issues](#dns-and-domain-issues)
3. [Server and Nginx Issues](#server-and-nginx-issues)
4. [Application Issues](#application-issues)
5. [Database Issues](#database-issues)

---

## Common Local Deployment Issues

### Issue: "No package.json file found" or "yarn: command not found"

**Cause:** This is a **Python Flask application**, not a Node.js application.

**Solution:**
```bash
# DON'T USE (Node.js commands):
# npm install
# yarn start

# USE INSTEAD (Python commands):
pip install -r requirements.txt
python app.py
```

### Issue: "No module named 'flask'"

**Cause:** Python dependencies not installed.

**Solution:**
```bash
pip install -r requirements.txt
```

If using a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: Port 5000 already in use

**Cause:** Another application is using port 5000.

**Solution 1 - Change port in .env:**
```bash
echo "PORT=3050" >> .env
```

**Solution 2 - Stop the conflicting process:**
```bash
# Find what's using port 5000
sudo lsof -i :5000
# Or on Windows
netstat -ano | findstr :5000

# Kill the process (Linux/Mac)
kill -9 <PID>
```

### Issue: Permission denied when running start.sh

**Cause:** Script doesn't have execute permissions.

**Solution:**
```bash
chmod +x start.sh
./start.sh
```

---

## DNS and Domain Issues

### Issue: Domain shows "Default Hostinger Page" instead of app

**Cause:** DNS is not properly configured or default index files are blocking your app.

**Step-by-step Solution:**

#### 1. Verify DNS Configuration

Check your A record points to the correct server IP:

```bash
# Check DNS resolution
dig aienter.in A
nslookup aienter.in

# Or use online tools:
# https://www.whatsmydns.net/
# https://dnschecker.org/
```

Expected output should show your VPS IP address.

#### 2. Set Correct A Record

In your domain registrar/hosting panel (Hostinger):

1. Go to DNS Management
2. Add/Edit A record:
   - **Type:** A
   - **Host:** @ (for aienter.in)
   - **Points to:** Your VPS IP address (e.g., 123.456.789.0)
   - **TTL:** 3600 or Auto

3. Add/Edit A record for www subdomain:
   - **Type:** A
   - **Host:** www
   - **Points to:** Your VPS IP address
   - **TTL:** 3600 or Auto

#### 3. Wait for DNS Propagation

DNS changes can take 1-48 hours to propagate globally. Check progress:
```bash
# Linux/Mac
watch -n 60 'dig aienter.in A'

# Or use online tool
# https://www.whatsmydns.net/?query=aienter.in&type=A
```

#### 4. Remove Default Hostinger Pages

**On your VPS server:**

```bash
# Connect to your VPS
ssh user@your-vps-ip

# Check for default index files
ls -la /var/www/html/
ls -la /usr/share/nginx/html/

# Remove or rename default files
sudo rm /var/www/html/index.html
sudo rm /var/www/html/index.nginx-debian.html
sudo rm /usr/share/nginx/html/index.html

# Or move them as backup
sudo mv /var/www/html/index.html /var/www/html/index.html.bak
```

#### 5. Configure Nginx Server Block

Create Nginx configuration for your domain:

```bash
# Copy the example configuration
sudo cp /home/ubuntu/Jai_Kisan/nginx.conf.example /etc/nginx/sites-available/jai-kisan

# Edit the configuration
sudo nano /etc/nginx/sites-available/jai-kisan

# Update these lines:
# - server_name: Change to your domain (aienter.in)
# - root: Update to your actual path
# - SSL paths: Update if using different locations

# Enable the site
sudo ln -s /etc/nginx/sites-available/jai-kisan /etc/nginx/sites-enabled/

# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Test configuration
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

### Issue: DNS propagated but still seeing old page

**Cause:** Browser cache or CDN cache.

**Solution:**
```bash
# Clear browser cache or try incognito mode
# Or use curl to bypass cache:
curl -I http://aienter.in
curl -I https://aienter.in

# If using Cloudflare, purge cache in dashboard
```

---

## Server and Nginx Issues

### Issue: Nginx not serving the application

**Diagnostic Steps:**

1. **Check if Nginx is running:**
```bash
sudo systemctl status nginx
```

2. **Check if application is running:**
```bash
sudo systemctl status jai-kisan
# Or if running manually:
ps aux | grep gunicorn
ps aux | grep python
```

3. **Check Nginx error logs:**
```bash
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/jai-kisan-error.log
```

4. **Check application logs:**
```bash
sudo journalctl -u jai-kisan -f
```

5. **Test application directly:**
```bash
# Test if app responds on localhost
curl http://localhost:5000
```

### Issue: 502 Bad Gateway Error

**Cause:** Nginx can't connect to the application backend.

**Solution:**

1. **Verify application is running:**
```bash
sudo systemctl status jai-kisan
sudo systemctl start jai-kisan
```

2. **Check if application is listening on correct port:**
```bash
sudo netstat -tulpn | grep :5000
# Or
sudo ss -tulpn | grep :5000
```

3. **Check firewall:**
```bash
# UFW
sudo ufw status
sudo ufw allow 5000/tcp

# iptables
sudo iptables -L
```

### Issue: 403 Forbidden Error

**Cause:** Nginx doesn't have permission to access files.

**Solution:**
```bash
# Fix file permissions
sudo chown -R ubuntu:www-data /home/ubuntu/Jai_Kisan
sudo chmod -R 755 /home/ubuntu/Jai_Kisan

# Fix Nginx user (in nginx.conf)
sudo nano /etc/nginx/nginx.conf
# Set: user www-data;
```

### Issue: Static files (CSS/JS/images) not loading

**Cause:** Incorrect static file paths in Nginx config.

**Solution:**

1. **Verify paths in nginx.conf.example:**
```nginx
location /static {
    alias /home/ubuntu/Jai_Kisan/static;  # Update this path
}

location /public {
    alias /home/ubuntu/Jai_Kisan/public;  # Update this path
}
```

2. **Reload Nginx:**
```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## Application Issues

### Issue: Application won't start

**Diagnostic Steps:**

1. **Check Python version:**
```bash
python3 --version  # Should be 3.7 or higher
```

2. **Check dependencies:**
```bash
source venv/bin/activate
pip list
```

3. **Check .env file:**
```bash
cat .env
# Verify SECRET_KEY, DATABASE_URI, etc. are set
```

4. **Check detailed error:**
```bash
python app.py
# Or check system logs:
sudo journalctl -u jai-kisan -n 50
```

### Issue: Database errors on startup

**Cause:** Database file permissions or corrupted database.

**Solution:**
```bash
# Remove and recreate database
rm jai_kisan.db
python app.py

# Or fix permissions
chmod 664 jai_kisan.db
chown ubuntu:www-data jai_kisan.db
```

### Issue: OTP not sending

**Cause:** Twilio credentials not configured.

**Solution:**

1. **For development (skip OTP):**
   - Comment out OTP verification in app.py (lines 176-198)
   - Or use mock OTP for testing

2. **For production:**
```bash
# In .env file, add:
TWILIO_ACCOUNT_SID=your-actual-sid
TWILIO_AUTH_TOKEN=your-actual-token
TWILIO_PHONE_NUMBER=+1234567890

# Verify credentials at: https://www.twilio.com/console
```

---

## Database Issues

### Issue: "Database is locked"

**Cause:** SQLite doesn't handle concurrent writes well.

**Solution for Production:**

Migrate to PostgreSQL:

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib
pip install psycopg2-binary

# Create database
sudo -u postgres psql
CREATE DATABASE jai_kisan;
CREATE USER jai_kisan_user WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE jai_kisan TO jai_kisan_user;
\q

# Update .env
DATABASE_URI=postgresql://jai_kisan_user:your-password@localhost/jai_kisan

# Restart application
sudo systemctl restart jai-kisan
```

---

## SSL/HTTPS Issues

### Issue: Need to enable HTTPS

**Solution using Let's Encrypt (Free):**

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d aienter.in -d www.aienter.in

# Follow prompts
# Certificate will auto-renew

# Test renewal
sudo certbot renew --dry-run
```

---

## Quick Diagnostic Commands

**Complete health check:**

```bash
#!/bin/bash
echo "=== System Check ==="
python3 --version
pip --version
echo ""

echo "=== DNS Check ==="
dig aienter.in A +short
echo ""

echo "=== Service Status ==="
sudo systemctl status nginx --no-pager
sudo systemctl status jai-kisan --no-pager
echo ""

echo "=== Port Check ==="
sudo netstat -tulpn | grep -E ':80|:443|:5000'
echo ""

echo "=== Recent Errors ==="
sudo tail -n 10 /var/log/nginx/error.log
sudo journalctl -u jai-kisan -n 10 --no-pager
```

---

## Getting Help

If you're still experiencing issues:

1. **Check GitHub Issues:** https://github.com/phildass/Jai_Kisan/issues
2. **Review Documentation:** 
   - [SETUP.md](SETUP.md) - Local setup
   - [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment
   - [README.md](README.md) - General overview
3. **Enable Debug Mode:**
   ```bash
   # In .env
   FLASK_ENV=development
   ```
4. **Collect diagnostic info and create an issue**

---

**जय किसान! (Victory to the Farmers!)**

*May your deployment be smooth and your server stay healthy* 🌾
