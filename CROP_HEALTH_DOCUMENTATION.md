# Crop Health & Marketplace Module - Documentation

## Overview

The **Digital Village Elder Crop Health & Marketplace** module is a comprehensive addition to the (J)ai Kisan platform that empowers farmers with actionable crop health diagnosis, IPM (Integrated Pest Management) recommendations, and real-time marketplace access.

## Features

### 1. Critical Crop & Disease Knowledge Layer

**Purpose:** Provide farmers with instant access to pest and disease information for major Indian crops.

**Key Components:**
- **Comprehensive Database:** 8+ major crops with detailed pest and disease information
  - Paddy (Rice), Wheat, Cotton, Tomato, Potato, Onion, Chili, Sugarcane
- **Regional & Seasonal Mapping:** Pests/diseases linked to specific regions and seasons
- **ETL (Economic Threshold Levels):** Scientific thresholds for chemical intervention
- **Symptoms & Identification:** Clear descriptions for easy field identification

**How to Use:**
1. Navigate to **Crop Health** dashboard
2. Select your crop from dropdown
3. View all major pests and diseases with:
   - Scientific names
   - Peak seasons
   - Symptoms
   - ETL thresholds
   - Favorable conditions for diseases

**Example Data:**
```
Crop: Cotton
Pest: Pink Bollworm
- Scientific Name: Pectinophora gossypiella
- Peak Season: Kharif
- Symptoms: Rosette flowers, entry holes in green bolls
- ETL: 10% rosette flowers or 8-10% green bolls damaged
```

### 2. AI-Driven "3-Step Ward-Off" IPM Advisor

**Purpose:** Provide a systematic, environmentally-friendly approach to pest and disease management.

**Three-Tier System:**

#### Tier 1: Bhoomi Raksha (Prevention) 🛡️
*Prevention is better than cure - reduces pest occurrence by 60-70%*

**Methods:**
1. **Seed Treatment**
   - Trichoderma viride @ 4g/kg seed
   - Pseudomonas fluorescens @ 10g/kg seed
   - Traditional: Turmeric + Neem extract
   - Cost: ₹50-100 per acre

2. **Deep Summer Ploughing**
   - Exposes soil to sunlight
   - Kills pest eggs and larvae
   - Cost: ₹800-1200 per acre
   - Effectiveness: 60-70% reduction

3. **Smart Crop Rotation**
   - Avoid same family crops consecutively
   - Built-in family checker (Solanaceae, Brassicaceae, Leguminosae, etc.)
   - Example: Never plant Tomato after Potato (both Solanaceae)

4. **Field Sanitation**
   - Remove crop residues after harvest
   - Cost: ₹500-800 per acre
   - Effectiveness: 40-50% reduction

5. **Resistant Varieties**
   - Use certified disease-resistant seeds
   - Cost: ₹200-500 extra per acre
   - Effectiveness: 50-80% reduction

6. **Balanced Fertilization**
   - Avoid excess nitrogen (attracts aphids/whiteflies)
   - Follow Soil Health Card recommendations
   - Effectiveness: 30-40% reduction

#### Tier 2: Jugaad (Organic & Mechanical) 🌱
*Low-cost, farmer-friendly solutions with 60-70% effectiveness*

**Methods:**
1. **Yellow Sticky Traps**
   - Material: Yellow plastic sheets + castor oil
   - Cost: ₹150-250 per acre (20-25 traps)
   - Effectiveness: 60-70% whitefly/aphid reduction
   - Suitable for: Cotton, Tomato, Chili, Onion

2. **Light Traps**
   - Material: 40W bulb + water bowl with kerosene
   - Cost: ₹300-500 per acre (2-3 traps)
   - Effectiveness: 40-50% reduction in egg-laying
   - Suitable for: Paddy, Cotton, Sugarcane

3. **Bird Perches**
   - Material: Bamboo poles/tree branches
   - Cost: ₹100-200 per acre
   - Effectiveness: Birds eat 40-60 larvae per day
   - Suitable for: All crops

4. **Neem Oil Spray**
   - Recipe: 1000-1500ml neem oil + 100ml soap in 200L water
   - Cost: ₹400-600 per acre per spray
   - Effectiveness: 70-80% control of soft-bodied insects
   - Safety: Wait 3 days before harvest

5. **Dashparni Arka (10-Leaf Extract)**
   - Traditional multi-plant extract
   - Ingredients: Neem, Custard apple, Guava, Pomegranate, Papaya leaves + cow urine
   - Cost: ₹200-300 per acre
   - Effectiveness: 60-70% pest control
   - Preparation: 2 hours

6. **Garlic-Chili-Ginger Spray**
   - Recipe: Grind 250g garlic + 250g chili + 100g ginger, soak overnight
   - Cost: ₹100-150 per acre
   - Effectiveness: 50-60% deterrent
   - Preparation: 24 hours

7. **Pheromone Traps**
   - Species-specific male moth traps
   - Cost: ₹800-1200 per acre (8-10 traps)
   - Effectiveness: 80-90% male trapping, 60-70% next generation reduction
   - Suitable for: Cotton, Tomato, Sugarcane

8. **Trap Crops**
   - Plant Castor/Marigold around field
   - Cost: ₹300-500 per acre
   - Effectiveness: Diverts 40-60% pests
   - Suitable for: Cotton, Tomato, Chili

#### Tier 3: Targeted Chemical (Last Resort) ⚗️
*Use ONLY when ETL is crossed and after trying Tier 1 & 2*

**Critical Requirements:**
- ✓ Check ETL (Economic Threshold Level) - NEVER spray below threshold
- ✓ Try organic methods first
- ✓ Wear protective gear (mask, gloves, full clothes)
- ✓ Spray only in early morning (6-9 AM) or evening (4-6 PM)
- ✓ Never spray during flowering or if rain expected in 4 hours
- ✓ Follow Pre-Harvest Interval (PHI) strictly

**Approved Chemicals:**

*For Sucking Pests (Aphids, Whiteflies, Thrips):*
1. **Imidacloprid 17.8% SL**
   - Dose: 0.5 ml/liter water
   - PHI: 7-14 days
   - Cost: ₹350-450 per 100ml (covers 1 acre)
   - Safety: Yellow label (Moderately hazardous)

2. **Thiamethoxam 25% WG**
   - Dose: 0.4 g/liter water
   - PHI: 14-21 days
   - Cost: ₹400-500 per 100g (covers 1 acre)
   - Safety: Yellow label

3. **Acetamiprid 20% SP**
   - Dose: 0.5 g/liter water
   - PHI: 7-14 days
   - Cost: ₹300-400 per 100g (covers 1 acre)
   - Safety: Blue label (Slightly hazardous)

*For Chewing Pests (Caterpillars, Borers):*
1. **Chlorantraniliprole 18.5% SC**
   - Dose: 0.4 ml/liter water
   - PHI: 1-3 days
   - Cost: ₹600-800 per 100ml (covers 1 acre)
   - Safety: Blue label
   - Note: Safe to beneficial insects

2. **Emamectin Benzoate 5% SG**
   - Dose: 0.5 g/liter water
   - PHI: 7-14 days
   - Cost: ₹400-550 per 100g (covers 1 acre)
   - Safety: Yellow label

3. **Spinosad 45% SC**
   - Dose: 0.5 ml/liter water
   - PHI: 1-3 days
   - Cost: ₹800-1000 per 100ml (covers 1 acre)
   - Safety: Blue label
   - Note: Organic origin, safe to bees after drying

*For Fungal Diseases:*
1. **Mancozeb 75% WP**
   - Dose: 2.5 g/liter water
   - PHI: 7-14 days
   - Cost: ₹250-350 per kg (covers 2 acres)
   - Safety: Blue label

2. **Carbendazim 50% WP**
   - Dose: 1 g/liter water
   - PHI: 7-14 days
   - Cost: ₹200-300 per kg (covers 5 acres)
   - Safety: Blue label

3. **Azoxystrobin 23% SC**
   - Dose: 1 ml/liter water
   - PHI: 3-7 days
   - Cost: ₹700-900 per 100ml (covers 1 acre)
   - Safety: Blue label

**Safety Protocol:**
- **Before Spraying:**
  - Check weather forecast (no rain for 4+ hours)
  - Wear protective gear
  - Read label instructions carefully
  - Inform neighbors

- **During Spraying:**
  - Spray in early morning or late evening
  - No wind or strong sunlight
  - No eating/drinking/smoking
  - Keep children and animals away
  - Cover water sources

- **After Spraying:**
  - Wash hands, face, and all exposed body parts
  - Wash clothes separately
  - Clean equipment thoroughly
  - Store chemicals locked away from food/children
  - Follow PHI before harvest

### 3. Real-Time Infection Alert Engine

**Purpose:** Provide early warnings to farmers about disease risks in their area.

**Features:**

#### Weather-Driven Predictive Alerts
- Integrates weather conditions with disease risk models
- Example: "High humidity (>90%) + 25-28°C = Paddy Blast risk"
- Provides preventive recommendations before disease appears

**Alert Conditions:**
1. **High Humidity + High Temperature (>80%, 25-35°C)**
   - Crops at Risk: Paddy (Blast), Cotton (Leaf Curl), Tomato (Early Blight)
   - Action: Apply preventive organic sprays

2. **High Humidity + Cool Temperature (>90%, 10-20°C)**
   - Crops at Risk: Potato (Late Blight), Wheat (Yellow Rust), Tomato (Late Blight)
   - Action: Apply Mancozeb preventively

3. **Cloudy Days + High Humidity (>3 days, >85%)**
   - Crops at Risk: Paddy (Sheath Blight), Wheat (Powdery Mildew)
   - Action: Apply fungicide preventively

4. **Rain Expected**
   - Action: DO NOT SPRAY - wait for dry weather

#### Neighborhood Watch System
- **Crowdsourced Reporting:** Farmers report pest/disease sightings
- **Automatic Alerts:** If 3+ farmers report same issue in a district, automatic alert sent to nearby farmers
- **5km Radius:** Geo-based queries to find nearby reports
- **Real-time Updates:** See pest/disease activity in your area (last 7 days)

**How It Works:**
1. Farmer A reports Pink Bollworm in Cotton (Severity: High)
2. Farmer B reports Pink Bollworm in Cotton (Severity: Medium)
3. Farmer C reports Pink Bollworm in Cotton (Severity: High)
4. System automatically creates alert: "Pink Bollworm outbreak in [District]"
5. All farmers within 5km receive notification
6. Alert includes preventive measures and IPM recommendations

### 4. Visual Diagnostics - "Photo Doctor"

**Purpose:** Enable farmers to diagnose crop problems using smartphone photos.

**Current Status:** 
- ✅ UI/Upload interface complete
- ⏳ Computer Vision model integration pending

**Planned Technology:**
- **Model:** TensorFlow Lite / ONNX
- **Architecture:** Vision Transformer / CNN optimized for mobile
- **Training Data:** Thousands of crop disease images
- **Offline Capability:** Model can run on-device without internet

**Features:**
1. **Photo Upload**
   - Camera capture or gallery selection
   - Preview before submission
   - Tips for best photo quality

2. **AI Analysis** (Pending)
   - Crop identification
   - Disease/pest recognition
   - Nutrient deficiency detection
   - Confidence scoring

3. **Diagnosis Output:**
   - Problem identification (disease vs. deficiency)
   - Severity assessment
   - Organic remedies (Tier 2)
   - Nearest shop for products
   - Safety tips if chemical needed

**Interim Solution:**
- **Manual Diagnosis Guide:** Quick visual reference table
  - Symptom → Likely Cause → What to Check
  - Example: "Yellowing from bottom up" → "Nitrogen deficiency" → "Uniform yellowing, no spots"
- **IPM Advisor Redirect:** Describe symptoms to get recommendations

### 5. Integrated Marketplace Access

**Purpose:** Help farmers find agricultural inputs at best prices from nearby shops.

**Features:**

#### Shop Database
- **Sample shops** in Punjab, Maharashtra, Karnataka, Uttar Pradesh
- **Shop Types:**
  - Authorized Retailers
  - Cooperative Societies (Kifayati prices)
  - Government Stores (Subsidized rates)
  - Private Dealers

**Shop Information:**
- Name, Type, Address, District
- GPS Coordinates
- Phone (Click to call)
- Products available
- Rating
- Opening hours
- Special offers

#### Price Comparison Engine
- **Multiple Brands:** Compare IFFCO, Dhanuka, UPL, Coromandel, etc.
- **Kifayati Options:** Highlight economical choices (save ₹100-200)
- **Product Categories:**
  - Organic pesticides (Neem Oil, Trichoderma)
  - Mechanical controls (Sticky Traps, Pheromone Traps)
  - Chemical pesticides (Imidacloprid, Chlorantraniliprole)
  - Fungicides (Mancozeb, Azoxystrobin)

**Example Price Comparison:**
```
Neem Oil (1 Liter)
1. Anand Agro: ₹450 (High availability)
2. Dhanuka: ₹520 (Medium availability)
3. Local Producer: ₹380 (High availability) ⭐ Kifayati

Imidacloprid 17.8% SL (100ml)
1. Bayer Confidor: ₹450 (High availability)
2. Dhanuka Cyclone: ₹380 (High availability) ⭐ Kifayati
3. UPL Imida: ₹350 (High availability) ⭐ Kifayati
```

#### Distance Calculation
- **Haversine Formula:** Calculate distance between farmer and shop
- **Sort by Distance:** Nearest shops first
- **Max Radius:** 50km by default (configurable)

#### Weather-Spray Timing Overlay
- **Rain Check:** "Rain expected in 4 hours - DO NOT spray!"
- **Best Timing:** Early morning (6-9 AM) or evening (4-6 PM)
- **Avoid:** Mid-day (chemicals evaporate), windy days, flowering period

**Example Advisory:**
```
🚫 DO NOT SPRAY NOW!
Rain expected in 3 hours. Spraying now will:
- Waste your money (chemicals wash away)
- Pollute water sources
- Not control pests effectively

Wait for 4+ hours of dry weather after spraying.
```

### 6. Regulatory Compliance Enforcement

**Purpose:** Protect farmers and environment by preventing use of banned chemicals.

**Banned Chemicals Database:**

#### Highly Toxic (Banned)
1. **Monocrotophos** (Banned 2020)
   - Reason: Extreme toxicity to humans, birds, beneficial insects
   - Alternative: Chlorantraniliprole or Emamectin Benzoate

2. **Phorate** (Banned 2020)
   - Reason: Highly toxic, groundwater contamination
   - Alternative: Seed treatment with Imidacloprid/Thiamethoxam

3. **Carbofuran** (Banned 2018)
   - Reason: Severe human toxicity, bird kills
   - Alternative: Fipronil or Chlorantraniliprole

4. **Methyl Parathion** (Banned 2018)
   - Reason: Extremely toxic to humans and wildlife
   - Alternative: Safer alternatives based on pest type

#### Soil Health Damaging (Banned)
1. **DDT** (Banned 1989)
   - Reason: Persistent pollutant, bioaccumulation
   - Alternative: Pyrethroids or neonicotinoids

2. **Endosulfan** (Banned 2011)
   - Reason: Environmental persistence, aquatic toxicity
   - Alternative: Based on pest type

#### Restricted Use
1. **Fipronil**
   - Restriction: Banned for foliar spray, allowed only for seed treatment
   - Reason: Highly toxic to bees
   - Alternative: Chlorantraniliprole (bee-safe)

**Chemical Ban Checker:**
- Instant lookup: Enter chemical name → Get ban status
- If banned: Display warning + reason + alternative
- If approved: Show safety rating and precautions

**Example:**
```
⚠️ BANNED!
Monocrotophos is banned for extreme toxicity to humans, birds, and beneficial insects.

Alternative: Use Chlorantraniliprole or Emamectin Benzoate for caterpillar control.
```

### 7. Safety Protocols System

**Multi-lingual Support:** English and Hindi (expandable to Marathi, Tamil, Telugu, etc.)

**Safety Tips Categories:**

#### Before Spraying
- Check weather forecast
- Wear protective gear
- Read label instructions
- Inform neighbors

#### During Spraying
- Spray in early morning or evening
- Never spray in wind
- No eating/drinking/smoking
- Keep children and animals away
- Cover water sources

#### After Spraying
- Wash exposed body parts immediately
- Wash clothes separately
- Clean equipment thoroughly
- Store chemicals securely
- Follow Pre-Harvest Interval

#### Emergency
- Eye contact: Wash 15 minutes, seek medical help
- Swallowed: Do NOT induce vomiting, take label to doctor
- Skin contact: Remove clothes, wash with soap
- Emergency numbers: 1800-425-2958 (Agriculture), 112 (Emergency)

## Database Schema

### New Tables

#### 1. PestReport
```python
- id: Integer (Primary Key)
- user_id: Foreign Key (User)
- crop: String
- pest_disease_name: String
- pest_disease_type: String (pest/disease)
- severity: String (low/medium/high/critical)
- pest_count: String
- symptoms: Text
- location: String
- latitude: Float
- longitude: Float
- report_date: DateTime
- status: String (active/controlled/resolved)
- photo_path: String
- verified: Boolean
```

#### 2. DiseaseAlert
```python
- id: Integer (Primary Key)
- alert_type: String (weather/neighborhood/seasonal)
- crop: String
- disease_name: String
- region: String
- severity: String (low/medium/high)
- description: Text
- preventive_measures: Text
- alert_date: DateTime
- expiry_date: DateTime
- weather_conditions: String
- active: Boolean
```

#### 3. CropLog
```python
- id: Integer (Primary Key)
- user_id: Foreign Key (User)
- crop: String
- variety: String
- area_hectares: Float
- sowing_date: Date
- expected_harvest_date: Date
- current_stage: String
- location: String
- latitude: Float
- longitude: Float
- notes: Text
- created_date: DateTime
- last_updated: DateTime
```

#### 4. User (Extended)
```python
# Added fields:
- latitude: Float
- longitude: Float
- pest_reports: Relationship (PestReport)
```

## API Endpoints

### Crop Health Routes

```
GET  /crop-health                    - Main crop health dashboard
GET  /ipm-advisor                    - IPM advisor form
POST /ipm-advisor                    - Get IPM recommendations
GET  /pest-disease-info/<crop>       - Get pest/disease info for crop
POST /check-chemical-ban             - Check if chemical is banned
POST /weather-spray-check            - Check spray timing based on weather
GET  /report-pest                    - Pest reporting form
POST /report-pest                    - Submit pest report
GET  /marketplace                    - Marketplace dashboard
POST /find-shops                     - Find shops for product
POST /crop-rotation-check            - Check crop rotation compatibility
GET  /photo-diagnosis                - Photo upload form
POST /photo-diagnosis                - Upload and diagnose photo
```

## Usage Examples

### Example 1: Get IPM Recommendations for Cotton Pink Bollworm

**Request:**
```javascript
POST /ipm-advisor
{
  "crop": "Cotton",
  "pest_disease": "Pink Bollworm",
  "pest_count": "15% rosette flowers"
}
```

**Response:**
```
नमस्ते! (Namaste!)

## IPM for Pink Bollworm in Cotton

**Problem Identified:** Pink Bollworm (Pectinophora gossypiella)
**Symptoms:** Rosette flowers, entry holes in green bolls

### 🛡️ Tier 1: Bhoomi Raksha (Prevention)
**Prevention methods reduce pest occurrence by 60-70%:**

**Deep Summer Ploughing**
- Expose soil to sunlight to kill pest eggs
- Cost: ₹800-1200 per acre
- Effectiveness: 60-70% reduction

**Field Sanitation**
- Remove crop residues after harvest
- Cost: ₹500-800 per acre
- Effectiveness: 40-50% reduction

### 🌱 Tier 2: Jugaad (Organic & Mechanical)
**Try organic methods first:**

**Pheromone Traps**
- Species-specific Pink Bollworm traps
- Cost: ₹800-1200 per acre (8-10 traps)
- Effectiveness: 80-90% male trapping

**Neem Oil Spray**
- 1000-1500ml neem oil + soap in 200L water
- Cost: ₹400-600 per acre
- Effectiveness: 70-80% control

### ⚗️ Tier 3: Chemical (Last Resort)
**⚠️ Check ETL first!**
**ETL for Pink Bollworm:** 10% rosette flowers or 8-10% green bolls
**Your count:** 15% rosette flowers
**Action:** ✓ Spray recommended (above threshold)

**Recommended Chemical:**
- Chlorantraniliprole 18.5% SC @ 0.4ml/liter
- Safe to beneficial insects
- Cost: ₹600-800 per acre
- PHI: 1-3 days

### 🔒 Safety First!
- Wear mask, gloves, full clothes
- Spray in early morning or evening
- Never spray during flowering
- Follow PHI strictly
```

### Example 2: Find Shops for Neem Oil

**Request:**
```javascript
POST /find-shops
{
  "product_name": "Neem Oil",
  "state": "Punjab",
  "district": "Ludhiana"
}
```

**Response:**
```
## Shops for Neem Oil in Punjab
**District:** Ludhiana

1. **Punjab Agro Center**
   Type: Authorized Retailer
   Address: Main Market, Ludhiana
   Phone: +91-161-2345678 (Click to call)
   Hours: 8:00 AM - 8:00 PM
   Rating: ⭐⭐⭐⭐ (4.5)

2. **Kisan Sewa Kendra**
   Type: Cooperative Society
   Address: Gill Road, Ludhiana
   Phone: +91-161-2456789 (Click to call)
   Hours: 7:00 AM - 7:00 PM
   Rating: ⭐⭐⭐⭐⭐ (4.8)
   Special: Kifayati prices - Co-op member benefits

### 💰 Price Comparison:

**Neem Oil (Organic Pesticide)**
Category: Bio-pesticide
Unit: 1 Liter

**Price Comparison:**
1. Local Producer (Kifayati): ₹380 - High availability
2. Anand Agro: ₹450 - High availability
3. Dhanuka: ₹520 - Medium availability

**💡 Kifayati (Most Economical) Option:**
- Local Producer: ₹380
```

### Example 3: Check Chemical Ban Status

**Request:**
```javascript
POST /check-chemical-ban
{
  "chemical_name": "Monocrotophos"
}
```

**Response:**
```json
{
  "banned": true,
  "chemical": "Monocrotophos",
  "reason": "Extreme toxicity to humans, birds, and beneficial insects",
  "ban_year": 2020,
  "alternative": "Use Chlorantraniliprole or Emamectin Benzoate for caterpillar control",
  "warning": "⚠️ ALERT: Monocrotophos is banned! Extreme toxicity to humans, birds, and beneficial insects"
}
```

### Example 4: Weather Spray Check

**Request:**
```javascript
POST /weather-spray-check
{
  "rainfall_forecast_hours": 3
}
```

**Response:**
```
## ⛅ Weather Advisory for Spraying

🚫 **DO NOT SPRAY NOW!**

Rain is expected in 3 hours. Spraying now will:
- Waste your money (chemicals will wash away)
- Pollute water sources
- Not control pests/diseases effectively

**Recommendation:** Wait until at least 4 hours of dry weather is assured after spraying.
Better to delay by 1-2 days than to waste chemicals.
```

## Future Enhancements

### Phase 9 (Pending)
1. **Weather API Integration**
   - Live weather data from IMD/OpenWeatherMap
   - Automatic disease risk calculations
   - Real-time spray timing alerts

2. **Computer Vision Model**
   - Train TensorFlow Lite model on crop disease dataset
   - On-device inference for offline diagnosis
   - Support for 20+ major diseases
   - Nutrient deficiency detection

3. **e-Urvarak/iFMS API Integration**
   - Live shop inventory data
   - Real-time pricing updates
   - Stock availability alerts
   - Online ordering capability

4. **Expanded Geographic Coverage**
   - More states and districts
   - More shop databases
   - Regional language support (Marathi, Tamil, Telugu, Bengali)

5. **Advanced Features**
   - SMS alerts for pest outbreaks
   - WhatsApp integration for quick consultations
   - Voice-based interface for low-literacy farmers
   - Expert verification system for pest reports
   - Farmer-to-farmer chat groups
   - Government scheme recommendations

## Technical Notes

### Offline Capability
- Knowledge base data stored locally in Python dictionaries
- No external API calls required for basic IPM recommendations
- Database caching for shop information
- Progressive Web App (PWA) for offline access

### Mobile Optimization
- Responsive design (Bootstrap 5)
- Large tap targets for farmer-friendly UI
- High contrast colors for outdoor sun visibility
- Image compression for low-bandwidth areas
- Minimal JavaScript for faster loading

### Data Privacy
- Exact farmer locations not shared publicly
- Only district-level information in neighborhood watch
- User data encrypted in database
- GDPR/Data Protection Act compliant

### Performance
- Python standard library only (no heavy dependencies)
- Efficient database queries with indexing
- Lazy loading of images
- Pagination for large datasets

## Deployment

### Requirements
```
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.3
python-dotenv==1.0.0
Werkzeug==3.0.3
```

### Environment Variables
```
SECRET_KEY=<your_secret_key>
DATABASE_URI=sqlite:///jai_kisan.db  # or PostgreSQL for production
FLASK_ENV=development  # or production
WEATHER_API_KEY=<optional_weather_api_key>
```

### Database Migration
```bash
# Initialize database
python
>>> from app import app, db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()

# Or run the application (auto-creates tables)
python app.py
```

### Running the Application
```bash
python app.py
# Visit http://localhost:5000
```

## Support

For technical support or feature requests:
- GitHub Issues: https://github.com/phildass/Jai_Kisan/issues
- Email: support@jaikisan.in (example)

---

**जय किसान! (Victory to the Farmers!)**

*May your crops be healthy and your harvests bountiful* 🌾
