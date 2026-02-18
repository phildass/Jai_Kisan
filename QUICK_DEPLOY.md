# (J)ai Kisan - Quick Deployment Reference Card

## 🚨 Critical Information

**This is a PYTHON Flask application, NOT Node.js!**

❌ **DON'T USE:**
- `npm install`
- `yarn start` 
- `package.json`

✅ **USE INSTEAD:**
- `pip install -r requirements.txt`
- `python app.py`
- `requirements.txt`

## 🚀 Quick Start (3 Steps)

### Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env

# 3. Start the app
python app.py
# Or use the helper script:
./start.sh
```

**Access:** http://localhost:5000

### Change Port (e.g., to 3050)

Edit `.env` file:
```bash
PORT=3050
```

## 📁 File Structure

```
Jai_Kisan/
├── app.py              # Main Flask application (START HERE)
├── requirements.txt    # Python dependencies
├── .env.example       # Environment template
├── start.sh           # Linux/Mac startup script
├── start.bat          # Windows startup script
│
├── SETUP.md           # Detailed setup guide
├── DEPLOYMENT.md      # Production deployment
├── TROUBLESHOOTING.md # Common issues & solutions
│
├── data/              # Crop, state, fertilizer data
├── templates/         # HTML templates
└── static/            # CSS, JavaScript
```

## 🌐 Production Deployment

### VPS Deployment (with domain like aienter.in)

**1. Server Setup:**
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip nginx

# Clone repository
git clone https://github.com/phildass/Jai_Kisan.git
cd Jai_Kisan

# Install Python packages
pip3 install -r requirements.txt
pip3 install gunicorn
```

**2. Configure Application:**
```bash
cp .env.example .env
nano .env
```

Set production values:
```bash
SECRET_KEY=your-random-secret-key-here
FLASK_ENV=production
DATABASE_URI=sqlite:///jai_kisan.db
PORT=5000
```

**3. Setup Systemd Service:**
```bash
sudo cp jai-kisan.service /etc/systemd/system/
sudo nano /etc/systemd/system/jai-kisan.service
# Update paths to match your installation

sudo systemctl enable jai-kisan
sudo systemctl start jai-kisan
```

**4. Configure Nginx:**
```bash
sudo cp nginx.conf.example /etc/nginx/sites-available/jai-kisan
sudo nano /etc/nginx/sites-available/jai-kisan
# Update domain name and paths

# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Enable your site
sudo ln -s /etc/nginx/sites-available/jai-kisan /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

**5. Setup SSL (HTTPS):**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d aienter.in -d www.aienter.in
```

## 🌍 DNS Configuration

### Setting up domain (e.g., aienter.in)

**In your domain provider (Hostinger, GoDaddy, etc.):**

| Type | Host | Points To | TTL |
|------|------|-----------|-----|
| A | @ | YOUR_VPS_IP | 3600 |
| A | www | YOUR_VPS_IP | 3600 |

**Check DNS propagation:**
```bash
dig aienter.in A +short
# Or visit: https://www.whatsmydns.net/
```

**Remove default pages:**
```bash
sudo rm /var/www/html/index.html
sudo rm /var/www/html/index.nginx-debian.html
```

## 🔧 Common Issues

### "package.json not found"
➜ This is Python, not Node.js. Use `pip install -r requirements.txt`

### "Port already in use"
➜ Change port in `.env` file: `PORT=3050`

### "Still seeing Hostinger default page"
➜ Remove `/var/www/html/index.html` and check Nginx config

### "OTP not working"
➜ Add Twilio credentials to `.env` (optional for testing)

### "Database locked"
➜ Use PostgreSQL for production instead of SQLite

## 📊 Status Checks

```bash
# Check deployment setup
chmod +x check-deployment.sh
./check-deployment.sh

# Check services
sudo systemctl status jai-kisan
sudo systemctl status nginx

# Check logs
sudo journalctl -u jai-kisan -f
sudo tail -f /var/log/nginx/error.log

# Check if app is running
curl http://localhost:5000
```

## 🔗 Documentation Links

| Document | Purpose |
|----------|---------|
| [SETUP.md](SETUP.md) | Detailed local setup |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Production deployment |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Problem solving |
| [README.md](README.md) | Project overview |

## 🆘 Get Help

1. Run: `./check-deployment.sh`
2. Check: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
3. GitHub Issues: https://github.com/phildass/Jai_Kisan/issues

---

**जय किसान! (Victory to the Farmers!)** 🌾
