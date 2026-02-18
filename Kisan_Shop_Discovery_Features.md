# Kisan Shop Discovery Features Documentation

## Overview
This document describes the Local Shop Discovery, Price Comparison, and Group Buying features implemented for {J}AI KISAN.

## Feature Table

| Feature           | Backend              | Frontend/UI         | Data/API        | Pro-Farmer Tip                    |
|-------------------|----------------------|---------------------|-----------------|-----------------------------------|
| Shop Discovery    | e-Urvarak integration, crowdsourcing | Map/list, Live/call, report button | iFMS/e-Urvarak, user reports | Show "recently confirmed by locals" |
| Price Comparison  | Brand-salt catalogue, price analytics | Compare view, "Kifayati Option"   | Brand + co-op data | Only use "Kifayati" for best value |
| AI Dosage Advice  | Crop rules, dosage calculator     | Input form, advice widget         | Crop-based rules | "Don't waste money on big brands"  |
| Group Buying      | Demand aggregation, shop alerts      | Join group, special offer         | Shop DB, messaging  | Highest savings for group order    |

---

## 1. Local Shop & Stock Discovery

### A. e-Urvarak Integration

**Backend Implementation:**
- Mock e-Urvarak API integration structure in `data/shop_data.py`
- `E_URVARAK_CONFIG` contains API endpoints configuration
- Sample shop data with real-time inventory tracking
- Cache duration: 30 minutes for inventory data
- Automatic fallback to last known data if API is unavailable

**Database Models:**
- `Shop`: Store retailer information (name, location, license, rating)
- `ShopInventory`: Track fertilizer stock levels and prices
- `CrowdsourcedReport`: Store farmer reports about shops

**API Endpoints:**
- `GET /shops`: Shop discovery page
- `POST /api/shops/nearby`: Get shops within specified radius
- `GET /api/shops/<shop_id>/inventory`: Get specific shop inventory

**Features:**
- Distance calculation using Haversine formula
- GPS-based location detection
- Radius filtering (10km, 25km, 50km, 100km)
- Fallback to state-based filtering when GPS unavailable

### B. Frontend UI

**Map View & List View:**
- Toggle between map and list views
- List view shows all shops with detailed information
- Map view placeholder (for future Google Maps integration)

**Shop Card Information:**
- Shop name and owner
- Distance from user location
- Contact number with "Click to Call" functionality
- Live stock status for all fertilizers
- Price per 50kg bag
- Shop rating and verification count

**Stock Status Colors:**
- Green: High stock (>100 bags)
- Orange: Low stock (1-20 bags)
- Red: Out of stock (0 bags)

### C. Crowdsourced "Live" Status

**Report Types:**
1. **Stock Available**: Farmer confirms stock availability
2. **Shop Closed**: Report shop closure
3. **Price Update**: Submit updated pricing information

**Gamification - Kisan Points:**
- Report stock available: 5 points
- Report shop closed: 3 points
- Report price update: 10 points
- Verified report bonus: 5 extra points

**Display:**
- Shows "Recently confirmed by X fellow farmers"
- Verification count visible on each shop
- Points balance displayed prominently

---

## 2. Price Comparison - "The Price Fight"

### A. The "Salt" Scanner

**Brand-to-Salt Mapping:**
- Complete database in `BRAND_TO_SALT_MAPPING`
- Maps all branded products to active ingredients
- NPK ratio tracking for accurate comparison

**Supported Fertilizers:**
1. **Urea (46-0-0)**
   - Salt: Urea (CO(NH2)2)
   - Branded avg: ₹302/bag
   - Kifayati: ₹268/bag (Government Subsidized)
   - Savings: ₹34/bag

2. **DAP (18-46-0)**
   - Salt: Di-Ammonium Phosphate
   - Branded avg: ₹1360/bag
   - Kifayati: ₹1200/bag (Co-operative)
   - Savings: ₹160/bag

3. **MOP (0-0-60)**
   - Salt: Muriate of Potash (KCl)
   - Branded avg: ₹910/bag
   - Kifayati: ₹840/bag (Co-operative)
   - Savings: ₹70/bag

4. **NPK 10:26:26**
   - Salt: NPK Complex
   - Branded avg: ₹1210/bag
   - Kifayati: ₹1140/bag
   - Savings: ₹70/bag

5. **NPK 20:20:0:13**
   - Salt: NPK Complex with Sulphur
   - Branded avg: ₹1110/bag
   - Kifayati: ₹1050/bag
   - Savings: ₹60/bag

**Frontend Display:**
```
Brand X (₹1,360)—Salt: Di-Ammonium Phosphate (18-46-0)

Kifayati Option: Co-operative DAP (₹1,200)

💰 You Save: ₹160 per bag!
```

**Design Principles:**
- Always use "Kifayati (Economical) Option" label (never "Generic")
- Highlight savings in large, bold text
- Show identical salt/NPK composition
- Green badge for Kifayati option

### B. API Endpoint

**Route:** `GET /api/price-comparison?type=<fertilizer_type>`

**Response:**
```json
{
  "fertilizer_type": "DAP",
  "salt": "Di-Ammonium Phosphate",
  "npk": "18-46-0",
  "branded_average": 1360,
  "kifayati_option": {
    "name": "Co-operative DAP",
    "price_per_50kg": 1200,
    "savings_per_bag": 160
  }
}
```

---

## 3. AI Dosage Calculator

### A. Calculation Logic

**Supported Crops:**
- Paddy (Rice)
- Wheat
- Cotton
- Default rules for other crops

**Growth Stages:**
1. Field Preparation (Basal Dose)
2. Vegetative Phase (Leaves/Stem growth)
3. Flowering/Reproductive Phase

**Calculation Formula:**
```
Required kg = (Base requirement per hectare) × (Area in hectares)
Bags needed = ceil(Required kg / 50)
```

**Example for 1 Hectare Paddy (Basal Dose):**
- Urea: 60 kg → 2 bags
- DAP: 100 kg → 2 bags
- MOP: 40 kg → 1 bag

### B. API Endpoint

**Route:** `POST /api/dosage-calculator`

**Request:**
```json
{
  "crop": "Paddy (Rice)",
  "area_hectares": 2.5,
  "growth_stage": "Field Preparation (Basal Dose)"
}
```

**Response:**
```json
{
  "crop": "Paddy (Rice)",
  "area_hectares": 2.5,
  "growth_stage": "Field Preparation (Basal Dose)",
  "bags_needed": {
    "UREA": {
      "kg_required": 150,
      "bags_50kg": 3,
      "bags_to_buy": 3
    },
    "DAP": {
      "kg_required": 250,
      "bags_50kg": 5,
      "bags_to_buy": 5
    }
  }
}
```

**Pro-Farmer Advice:**
- "Don't waste money on larger pack sizes!"
- "Buy exactly what you need"
- Shows exact kg requirements
- Rounds up to whole bags for purchase

---

## 4. Group Buying (Kisan Group)

### A. Group Matching Logic

**Thresholds by Fertilizer:**
- Urea: 50 bags minimum, 5 farmers, 3% discount
- DAP: 40 bags minimum, 5 farmers, 5% discount
- MOP: 30 bags minimum, 4 farmers, 4% discount
- NPK varieties: 35 bags minimum, 4 farmers, 4% discount

**Database Models:**
- `GroupBuying`: Track group aggregation status
- `GroupBuyingParticipant`: Individual farmer participation

**Group Status Flow:**
1. **Open**: Accepting new participants
2. **Threshold Met**: Minimum requirements reached
3. **Offer Sent**: Shop contacted for bulk discount
4. **Completed**: Purchase finalized

### B. API Endpoints

**Create/Join Group:**
- Route: `POST /api/group-buying/create`
- Automatically joins existing open group or creates new one
- Awards 8 Kisan Points for joining

**Check Status:**
- Route: `GET /api/group-buying/status/<group_id>`
- Returns progress toward thresholds
- Shows discount percentage when threshold met

### C. Frontend Display

**Progress Tracking:**
- Visual progress bar for bags and farmer count
- Percentage completion shown
- Success message when threshold reached

**Benefits Display:**
- Potential savings highlighted
- Discount percentage shown
- Group size and total bags displayed

**Kisan Points:**
- Join group: 8 points
- Complete purchase: 15 points

---

## 5. UX/Localization - Pro-Farmer Design

### A. Language & Terminology

**Always Use:**
- "Kifayati (Economical) Option" ✅
- "Fellow farmers" when referring to community
- Hindi greetings: "नमस्ते" (Namaste)
- "जय किसान!" (Victory to the Farmers!)

**Never Use:**
- "Generic" ❌
- Technical jargon without explanation
- English-only labels

### B. High-Contrast UI

**Color Scheme:**
- Primary: #2e7d32 (Dark Green) - for headers, primary actions
- Success: #4caf50 (Green) - for positive actions, savings
- Warning: #ff9800 (Orange) - for low stock
- Error: #f44336 (Red) - for out of stock
- Accent: #ffd700 (Gold) - for Kisan Points

**Typography:**
- Large font sizes (16px minimum)
- High contrast ratios (WCAG AA compliant)
- Bold weights for important information

**Touch Targets:**
- Minimum 44px × 44px for all buttons
- Adequate spacing between clickable elements

### C. Offline-First Architecture

**Data Caching:**
- Shop inventory cached with timestamps
- Last known data shown when API unavailable
- "Last updated" timestamp displayed
- Sync automatically when connection restores

**Future Enhancements:**
- Service worker for offline page access
- Local storage for recent searches
- Queue reports for submission when online

---

## 6. Technical Implementation Details

### A. Database Schema

**New Tables:**
1. `user` - Added `kisan_points` field (Integer, default 0)
2. `shop` - Retailer information
3. `shop_inventory` - Stock tracking
4. `crowdsourced_report` - Farmer reports
5. `group_buying` - Group aggregation
6. `group_buying_participant` - Individual participation

**Relationships:**
- User → CrowdsourcedReport (One-to-Many)
- User → GroupBuyingParticipant (One-to-Many)
- Shop → ShopInventory (One-to-Many)
- Shop → CrowdsourcedReport (One-to-Many)
- GroupBuying → GroupBuyingParticipant (One-to-Many)

### B. Data Files

**New Data File:** `data/shop_data.py`

Contains:
- `SAMPLE_SHOPS`: Mock shop data with locations
- `BRAND_TO_SALT_MAPPING`: Brand to active ingredient mapping
- `KIFAYATI_ALTERNATIVES`: Economical alternatives database
- `E_URVARAK_CONFIG`: API configuration
- `DOSAGE_CALCULATION_RULES`: Crop-specific dosage rules
- `GROUP_BUYING_THRESHOLDS`: Minimum requirements for bulk buying
- `KISAN_POINTS_REWARDS`: Point values for actions

### C. Frontend Template

**New Template:** `templates/shop_discovery.html`

Features:
- Responsive grid layout
- GPS location detection
- Dynamic shop cards
- Real-time inventory display
- Inline price comparison tool
- Dosage calculator widget
- Group buying interface
- Kisan Points display

### D. API Routes

**All New Routes:**
```python
GET  /shops                          # Shop discovery page
POST /api/shops/nearby               # Get nearby shops
GET  /api/shops/<shop_id>/inventory  # Shop inventory
POST /api/crowdsource/report         # Submit report
GET  /api/price-comparison           # Compare prices
POST /api/dosage-calculator          # Calculate dosage
POST /api/group-buying/create        # Create/join group
GET  /api/group-buying/status/<id>   # Group status
```

---

## 7. Testing & Validation

### A. Test Scenarios

**Shop Discovery:**
1. Test location permission grant/deny
2. Verify distance calculation accuracy
3. Test radius filtering
4. Validate state-based fallback
5. Check shop card rendering

**Price Comparison:**
1. Test all fertilizer types
2. Verify savings calculation
3. Check salt mapping accuracy
4. Validate kifayati option display

**Dosage Calculator:**
1. Test all supported crops
2. Verify calculation for different areas
3. Check bag rounding logic
4. Test growth stage variations

**Group Buying:**
1. Test group creation
2. Verify joining existing group
3. Check threshold detection
4. Validate Kisan Points awards
5. Test progress tracking

### B. Test Data

**Sample Shops:**
- 4 shops in Punjab state
- Various districts (Ludhiana, Amritsar, Patiala)
- Different inventory levels
- Realistic pricing

**Location Testing:**
- Use Punjab coordinates for testing
- Ludhiana: 30.9010, 75.8573
- Amritsar: 31.6340, 74.8723

---

## 8. Future Enhancements

### A. Phase 2 Features

1. **Real e-Urvarak Integration:**
   - Connect to actual iFMS API
   - Automatic inventory synchronization
   - Government data validation

2. **Google Maps Integration:**
   - Interactive map view
   - Route navigation to shops
   - Street view preview

3. **SMS Notifications:**
   - Group buying threshold alerts
   - Price drop notifications
   - New shop alerts

4. **Shop Dashboard:**
   - Separate portal for retailers
   - Inventory management interface
   - Bulk order management
   - Direct farmer communication

5. **Advanced Analytics:**
   - Price trend analysis
   - Demand forecasting
   - Seasonal recommendations
   - Regional comparison

### B. Scalability Considerations

**Database:**
- Add indexes on frequently queried fields
- Implement database sharding for large datasets
- Use read replicas for shop queries

**Caching:**
- Implement Redis for shop inventory cache
- Cache price comparisons
- Store frequently accessed groups

**API Rate Limiting:**
- Implement rate limiting per user
- Throttle shop search requests
- Queue group buying operations

---

## 9. Deployment Notes

### A. Environment Variables

No new environment variables required. All configuration is in code.

### B. Database Migration

Run database migration to create new tables:
```bash
python app.py
# Tables will be auto-created on first run
```

### C. Static Assets

Ensure the following are available:
- `/public/images/jai_kisan_logo.png` (existing)
- All CSS styling is inline in template

### D. Dependencies

No new dependencies required. Using existing Flask, SQLAlchemy, and Python standard library.

---

## 10. User Guide

### A. For Farmers

**Finding Shops:**
1. Navigate to "🏪 Shops" from dashboard
2. Click "Use My Location" or "Search Shops"
3. Browse nearby shops in list view
4. Call shops directly or report status
5. Earn Kisan Points for contributions

**Comparing Prices:**
1. Select fertilizer type from dropdown
2. Click "Compare Prices"
3. See branded vs kifayati options
4. Calculate potential savings

**Calculating Dosage:**
1. Select crop, area, and growth stage
2. Get exact fertilizer requirements
3. See number of bags to purchase
4. Avoid over-purchasing

**Group Buying:**
1. Select fertilizer and quantity needed
2. Join or create buying group
3. Track progress toward threshold
4. Get notified when discount is available
5. Complete purchase with group

### B. For Shop Owners

**Responding to Group Buying:**
1. Receive notification of bulk demand
2. Review farmer count and quantity
3. Offer competitive bulk discount
4. Coordinate delivery/pickup

---

## Conclusion

This implementation provides a comprehensive solution for local shop discovery, transparent price comparison, intelligent dosage calculation, and community-driven group buying. The system is designed with farmers' best interests in mind, using "Kifayati" terminology, high-contrast UI, and offline-first architecture.

**Key Success Metrics:**
- Farmer savings per transaction
- Kisan Points engagement
- Group buying participation rate
- Crowdsourced report accuracy
- Shop discovery usage

**Pro-Farmer Philosophy:**
- Transparency in pricing
- Community collaboration
- Cost savings emphasis
- Accessibility and ease of use
- Respect for local knowledge
