# (J)ai Kisan - Example Usage and Scenarios

## Example 1: DAP Price Concern - Maharashtra Farmer

### Scenario
A farmer in Maharashtra is preparing for the season and finds branded DAP too expensive.

### Query (in Marathi)
"DAP chi kimmat khup vadhli aahe. Mala swasta pariay sanga ani jaminicha pot kasa sudharava?"

*(English: DAP price has increased a lot. Tell me a cheaper alternative and how to improve soil health?)*

### (J)ai Kisan Response

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()
response = agent.generate_response(
    crop="Cotton",
    state="Maharashtra",
    growth_stage="Field Preparation (Basal Dose)"
)
print(response)
```

### Expected Output Highlights:

1. **Price Comparison (Per 50kg Bag)**
   | Option | Nutrient Value | Approx. Price | Saving Tip |
   |---|---|---|---|
   | Branded DAP (IFFCO) | 18-46-0 | ₹1,350 | Standard price |
   | Branded DAP (Chambal) | 18-46-0 | ₹1,375 | Premium brand |
   | Generic/Co-op DAP | 18-46-0 | ₹1,225 | Check local PACs |

2. **The "Eco-Smart" Alternative (Bhoomi Raksha)**
   - Instead of 2 bags of DAP: Use 1 bag DAP + 2 bags Vermicompost/PROM
   - **Benefit:** Reduces chemical cost by 30%
   - **Soil Health:** Increases carbon content and water retention

3. **Weather Alert**
   - Check for rain in next 48-72 hours
   - Delay application if heavy rain expected
   - Prevents nutrient runoff and wastage

---

## Example 2: Paddy Farmer in Punjab - Vegetative Phase

### Scenario
A paddy farmer in Punjab during the vegetative phase needs nitrogen fertilizer recommendations.

### Code Example

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

# Get specific recommendations
recommendation = agent.get_fertilizer_recommendations(
    crop="Paddy (Rice)",
    state="Punjab",
    growth_stage="Vegetative Phase (Leaves/Stem growth)"
)

print("NPK Requirements:", recommendation['npk_requirement'])
print("Eco Alternatives:", list(recommendation['eco_alternatives'].keys()))
print("Price Comparison available for:", len(recommendation['price_comparison']), "options")
```

### Key Recommendations:

**Traditional Approach:**
- Urea: 87 kg (equivalent to 40 kg N)
- Cost: ~₹520 (two 50kg bags @ ₹260 each)

**Modern Eco-Smart Approach:**
- Nano Urea: 1 bottle (500ml)
- Cost: ₹240
- **Savings:** ₹280 per application
- **Environmental Benefit:** 50% reduction in chemical load

---

## Example 3: Wheat Farmer in Uttar Pradesh - Basal Dose

### Scenario
A wheat farmer preparing fields before sowing.

### Interactive Example

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

# Check what crops are available
print("Available Cereals:", agent.get_crop_categories()['Cereals'])

# Get wheat recommendation
response = agent.generate_response(
    crop="Wheat",
    state="Uttar Pradesh",
    growth_stage="Field Preparation (Basal Dose)"
)

print(response)
```

### Key Points:

**Nutrient Requirements:**
- N: 40 kg/ha
- P: 30 kg/ha  
- K: 20 kg/ha

**Fertilizer Options:**
1. DAP (87 kg) + MOP (33 kg)
2. NPK Complex (150 kg of 12:32:16)
3. **Eco Option:** PROM (167 kg) + Vermicompost (300 kg)

**Timing:** Apply 1-2 weeks before sowing for best results

---

## Example 4: Cotton Farmer Query - Generic vs Branded

### Scenario
A cotton farmer wants to understand the difference between branded and generic fertilizers.

### Query Processing

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

# Get all available fertilizer brands for comparison
from data.fertilizer_data import BRANDED_FERTILIZERS

print("DAP Brand Comparison:")
for brand in BRANDED_FERTILIZERS['DAP']:
    print(f"{brand['brand']}: ₹{brand['price_per_50kg']} ({brand['availability']} availability)")
```

### Output:

```
DAP Brand Comparison:
IFFCO: ₹1350 (High availability)
Chambal: ₹1375 (High availability)
Coromandel: ₹1360 (High availability)
Generic/Co-op: ₹1225 (Medium availability)
```

**Key Message:**
- Generic/Co-op DAP saves ₹125-150 per bag
- Same nutrient content (18-46-0)
- Available at Primary Agricultural Cooperative Societies (PACS)
- For 10 bags: Save ₹1,250-1,500!

---

## Example 5: State-Specific Soil Information

### Scenario
A farmer wants to understand their soil characteristics.

### Code Example

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

# Get soil info for different states
states = ["Punjab", "Maharashtra", "West Bengal", "Tamil Nadu"]

for state in states:
    info = agent.get_state_info(state)
    print(f"\n{state}:")
    print(f"  Soil Type: {info['soil_type']}")
    print(f"  pH Range: {info['typical_ph']}")
    print(f"  Common Issue: {info['common_issue']}")
```

### Output:

```
Punjab:
  Soil Type: Alluvial, Sandy Loam
  pH Range: 7.0-8.5
  Common Issue: Salinity in some areas

Maharashtra:
  Soil Type: Black (Vertisol), Laterite
  pH Range: 6.5-8.0
  Common Issue: Low nitrogen, moisture stress

West Bengal:
  Soil Type: Alluvial, Laterite
  pH Range: 5.5-7.0
  Common Issue: Acidity in some areas

Tamil Nadu:
  Soil Type: Black, Red, Alluvial
  pH Range: 6.0-8.0
  Common Issue: Salinity in coastal areas
```

---

## Example 6: Growth Stage Progression

### Scenario
A farmer wants to track fertilizer needs throughout the crop lifecycle.

### Code Example

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

crop = "Sugarcane"
state = "Maharashtra"
stages = agent.get_growth_stages()

print(f"Fertilizer Plan for {crop} in {state}\n")
print("=" * 80)

for stage in stages:
    npk = agent.get_npk_requirement(crop, stage)
    if npk:
        print(f"\n{stage}:")
        print(f"  N: {npk['N']} kg/ha")
        print(f"  P: {npk['P']} kg/ha")
        print(f"  K: {npk['K']} kg/ha")
```

### Output:

```
Fertilizer Plan for Sugarcane in Maharashtra

================================================================================

Field Preparation (Basal Dose):
  N: 60 kg/ha
  P: 40 kg/ha
  K: 40 kg/ha

Sowing/Early Growth:
  N: 40 kg/ha
  P: 20 kg/ha
  K: 20 kg/ha

Vegetative Phase (Leaves/Stem growth):
  N: 80 kg/ha
  P: 20 kg/ha
  K: 40 kg/ha

Flowering & Fruiting:
  N: 40 kg/ha
  P: 10 kg/ha
  K: 40 kg/ha

Pre-Harvest:
  N: 0 kg/ha
  P: 0 kg/ha
  K: 20 kg/ha
```

**Total Season Requirement:**
- N: 220 kg/ha
- P: 90 kg/ha
- K: 160 kg/ha

---

## Example 7: Eco-Friendly Alternatives Focus

### Scenario
A farmer interested in organic farming wants eco-friendly options.

### Code Example

```python
from jai_kisan_agent import JaiKisanAgent
from data.fertilizer_data import ECO_ALTERNATIVES

agent = JaiKisanAgent()

print("Eco-Friendly Fertilizer Alternatives\n")
print("=" * 80)

for name, data in ECO_ALTERNATIVES.items():
    print(f"\n{name}")
    print(f"  Type: {data['type']}")
    
    # Price information
    if 'price_per_50kg' in data:
        print(f"  Price: ₹{data['price_per_50kg']} per 50kg")
    elif 'price_per_bottle' in data:
        print(f"  Price: ₹{data['price_per_bottle']} per bottle")
    elif 'cost' in data:
        print(f"  Cost: {data['cost']}")
    
    # Benefits
    if 'benefits' in data:
        print("  Benefits:")
        for benefit in data['benefits'][:2]:  # Show first 2 benefits
            print(f"    - {benefit}")
```

---

## Example 8: Using the CLI

### Interactive Session Example

```bash
$ python cli.py

================================================================================
                    (J)ai Kisan - जय किसान
               Your Digital Village Elder
================================================================================

Welcome! I am here to help you with fertilizer recommendations
tailored to your crop, region, and growth stage.

Let's get started!


Select Your Crop
================================================================================

Cereals:
  1. Paddy (Rice)
  2. Wheat
  3. Maize
  4. Bajra
  5. Jowar
  6. Ragi

Pulses:
  7. Tur (Arhar)
  8. Moong
  9. Gram (Chana)
  10. Masoor
  11. Urad

[... more options ...]

Enter your choice (1-29): 1

Select Your State/Region
================================================================================

North:
  1. Punjab
  2. Haryana
  3. Uttar Pradesh
[... more options ...]

Enter your choice (1-29): 1

Select Growth Stage
-------------------
1. Field Preparation (Basal Dose)
2. Sowing/Early Growth
3. Vegetative Phase (Leaves/Stem growth)
4. Flowering & Fruiting
5. Pre-Harvest

Enter your choice (1-5): 3

================================================================================
Generating your personalized recommendation...
================================================================================

[Full recommendation displayed here]
```

---

## Example 9: Integration with AI/LLM Systems

### Using as System Prompt

```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()

# Get the system prompt for AI integration
system_prompt = agent.get_system_prompt()

# Use with your favorite LLM
# Example with OpenAI (pseudo-code)
"""
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "मला भात पिकासाठी खत सांगा"}
    ]
)
"""
```

---

## Best Practices

1. **Always check soil health first** - Encourage farmers to get Soil Health Cards
2. **Consider local weather** - Timing is crucial for fertilizer application
3. **Promote eco-alternatives** - Start with organic options, supplement with chemical if needed
4. **Economic sensitivity** - Small farmers need cost-effective solutions
5. **Split applications** - Better nutrient use efficiency than single large dose
6. **Mix organic + chemical** - Best of both worlds for soil health and crop yield

---

**Remember:** The goal is sustainable agriculture that benefits both farmers and the environment! 🌾
