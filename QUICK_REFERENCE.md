# (J)ai Kisan - Quick Reference Guide

## Quick Start Commands

```bash
# Run interactive CLI
python cli.py

# Run test suite
python test_suite.py

# Run examples
python jai_kisan_agent.py
```

## API Quick Reference

### Initialize Agent
```python
from jai_kisan_agent import JaiKisanAgent
agent = JaiKisanAgent()
```

### Get Available Options
```python
# Get all crop categories
categories = agent.get_crop_categories()
# Returns: {"Cereals": [...], "Pulses": [...], ...}

# Get all states by region
regions = agent.get_state_regions()
# Returns: {"North": [...], "West": [...], ...}

# Get growth stages
stages = agent.get_growth_stages()
# Returns: ["Field Preparation (Basal Dose)", ...]
```

### Get Specific Information
```python
# Get NPK requirement for a crop/stage
npk = agent.get_npk_requirement("Paddy (Rice)", "Vegetative Phase (Leaves/Stem growth)")
# Returns: {"N": 40, "P": 10, "K": 20}

# Get state soil information
info = agent.get_state_info("Punjab")
# Returns: {"typical_ph": "7.0-8.5", "soil_type": "Alluvial, Sandy Loam", ...}
```

### Generate Recommendations
```python
# Get complete recommendation
response = agent.generate_response(
    crop="Cotton",
    state="Maharashtra",
    growth_stage="Field Preparation (Basal Dose)"
)
print(response)  # Formatted markdown output
```

## Data Quick Reference

### Major Crops Supported (26 total)

**Cereals (6):**
- Paddy (Rice), Wheat, Maize, Bajra, Jowar, Ragi

**Pulses (5):**
- Tur (Arhar), Moong, Gram (Chana), Masoor, Urad

**Cash Crops (4):**
- Sugarcane, Cotton, Jute, Tobacco

**Oilseeds (4):**
- Soybean, Groundnut, Mustard, Sunflower

**Horticulture (7):**
- Tea, Coffee, Rubber, Potato, Onion, Tomato, Chili

### States Covered (28 total)

**North (7):** Punjab, Haryana, Uttar Pradesh, Rajasthan, Himachal Pradesh, Uttarakhand, J&K (UT)

**West (4):** Gujarat, Maharashtra, Goa, Madhya Pradesh

**South (5):** Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu

**East & North-East (12):** West Bengal, Bihar, Jharkhand, Odisha, Assam, Sikkim, Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Tripura

### Growth Stages (5)
1. Field Preparation (Basal Dose)
2. Sowing/Early Growth
3. Vegetative Phase (Leaves/Stem growth)
4. Flowering & Fruiting
5. Pre-Harvest

### Fertilizer Types

**Common Chemical:**
- Urea (46-0-0)
- DAP (18-46-0)
- MOP (0-0-60)
- NPK complexes

**Eco-Friendly Alternatives:**
- Vermicompost
- PROM (Phosphate Rich Organic Manure)
- Farm Yard Manure (FYM)
- Neem Cake
- Green Manure
- Nano Urea

## Typical Price Ranges (₹ per 50kg)

| Fertilizer | Branded | Generic/Co-op | Eco Alternative |
|------------|---------|---------------|-----------------|
| DAP | ₹1,350-1,375 | ₹1,225 | PROM: ₹300 |
| Urea | ₹300-305 | ₹268 | Nano Urea: ₹240/bottle |
| MOP | ₹900-920 | ₹850 | - |
| NPK Complex | ₹1,100-1,220 | - | Vermicompost: ₹250 |

## Common Use Cases

### 1. Price Comparison
```python
from data.fertilizer_data import BRANDED_FERTILIZERS

for brand in BRANDED_FERTILIZERS['DAP']:
    print(f"{brand['brand']}: ₹{brand['price_per_50kg']}")
```

### 2. Get Eco-Alternatives
```python
from data.fertilizer_data import ECO_ALTERNATIVES

for name, data in ECO_ALTERNATIVES.items():
    print(f"{name}: {data['benefits'][0]}")
```

### 3. Track Entire Season
```python
crop = "Wheat"
for stage in agent.get_growth_stages():
    npk = agent.get_npk_requirement(crop, stage)
    if npk:
        print(f"{stage}: N={npk['N']}, P={npk['P']}, K={npk['K']}")
```

## Key Features Summary

✓ **26 crops** across 5 categories  
✓ **28 states** with soil information  
✓ **5 growth stages** per crop  
✓ **N-P-K requirements** for each crop/stage  
✓ **Price comparisons** (branded vs generic)  
✓ **Eco-alternatives** prioritized  
✓ **Zero external dependencies**  
✓ **Pure Python implementation**  

## Best Practices

1. **Always check soil health** - Get Soil Health Card
2. **Prefer eco-alternatives** - Better for long-term soil health
3. **Check weather** - Don't apply before heavy rain
4. **Split applications** - Better nutrient efficiency
5. **Mix organic + chemical** - Best results for yield and soil

## File Structure

```
Jai_Kisan/
├── jai_kisan_agent.py      # Main agent (core logic)
├── cli.py                   # Interactive CLI
├── test_suite.py            # Automated tests
├── data/
│   ├── crops_data.py        # Crop NPK requirements
│   ├── states_data.py       # State/soil information
│   └── fertilizer_data.py   # Fertilizer types/prices
├── examples/
│   └── example_usage.md     # Detailed examples
├── DOCUMENTATION.md         # Full documentation
├── system_prompt.md         # System requirements
└── README.md                # Project overview
```

## Support & Resources

- **Documentation**: See DOCUMENTATION.md
- **Examples**: See examples/example_usage.md
- **System Prompt**: See system_prompt.md
- **Tests**: Run test_suite.py

---

**जय किसान! (Victory to the Farmers!)** 🌾
