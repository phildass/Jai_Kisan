# (J)ai Kisan - जय किसान
**Your Digital Village Elder: An Intelligent Agricultural Consultant for Indian Farmers**

## Overview

(J)ai Kisan is an AI-powered agricultural consultant designed specifically for the Indian farming community. Acting as a "Digital Village Elder," it provides:

- **Fertilizer Intelligence**: Comprehensive N-P-K ratios for major crops
- **Price Comparisons**: Branded vs. generic fertilizer options
- **Environmental Stewardship**: Eco-friendly and organic alternatives
- **Regional Context**: State-specific soil and climate information
- **Growth Stage Optimization**: Tailored recommendations for each crop phase

## Features

### 🌾 Crop Support
Covers all major Indian crops across categories:
- **Cereals**: Paddy, Wheat, Maize, Bajra, Jowar, Ragi
- **Pulses**: Tur, Moong, Gram, Masoor, Urad
- **Cash Crops**: Sugarcane, Cotton, Jute, Tobacco
- **Oilseeds**: Soybean, Groundnut, Mustard, Sunflower
- **Horticulture**: Potato, Onion, Tomato, Chili, Tea, Coffee

### 🗺️ Regional Coverage
All Indian states organized by region:
- **North**: Punjab, Haryana, UP, Rajasthan, HP, Uttarakhand, J&K
- **West**: Gujarat, Maharashtra, Goa, MP
- **South**: AP, Telangana, Karnataka, Kerala, Tamil Nadu
- **East & North-East**: West Bengal, Bihar, Jharkhand, Odisha, Assam, and NE states

### 🌱 Growth Stage Tracking
- Field Preparation (Basal Dose)
- Sowing/Early Growth
- Vegetative Phase (Leaves/Stem growth)
- Flowering & Fruiting
- Pre-Harvest

### 💰 Economic Intelligence
- Real-time fertilizer price comparisons
- Branded options: IFFCO, Chambal, Coromandel
- Generic/subsidized alternatives
- Cost-saving recommendations

### 🌍 Environmental Focus
**"Bhoomi Raksha" - Earth Protection**
- Organic alternatives prioritized
- Bio-fertilizers and green manuring
- Soil Health Card integration
- Nitrogen Use Efficiency (NUE) optimization

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/phildass/Jai_Kisan.git
cd Jai_Kisan

# No external dependencies required - uses only Python standard library
```

## Usage

### Command Line Interface

Run the interactive CLI:
```bash
python cli.py
```

The CLI will guide you through:
1. Selecting your crop
2. Choosing your state/region
3. Identifying growth stage
4. Receiving personalized recommendations

### Python API

Use the agent programmatically:

```python
from jai_kisan_agent import JaiKisanAgent

# Initialize the agent
agent = JaiKisanAgent()

# Get recommendation
response = agent.generate_response(
    crop="Paddy (Rice)",
    state="Punjab",
    growth_stage="Vegetative Phase (Leaves/Stem growth)"
)

print(response)
```

### Example Output

```
नमस्ते! (Namaste!)

## Fertilizer Recommendation for Paddy (Rice) in Punjab
**Growth Stage:** Vegetative Phase (Leaves/Stem growth)

### 1. Nutrient Requirements (per hectare)
- **Nitrogen (N):** 40 kg
- **Phosphorus (P):** 10 kg
- **Potassium (K):** 20 kg

### 2. Soil Information for Your Region
- **Soil Type:** Alluvial, Sandy Loam
- **Typical pH:** 7.0-8.5
- **Common Issue:** Salinity in some areas
- **Agro-climatic Zone:** Trans-Gangetic Plains

### 3. Price Comparison (Per 50kg Bag)
| Option | Nutrient Value | Approx. Price (₹) | Availability |
|--------|----------------|-------------------|---------------|
| IFFCO | 46-0-0 | ₹300 | High |
| Chambal | 46-0-0 | ₹305 | High |
| Government Subsidized | 46-0-0 | ₹268 | High |

### 4. Eco-Smart Alternatives (Bhoomi Raksha)
**Environmental Stewardship:** We recommend green alternatives first!

**Nano Urea**
- Price: ₹240 per bottle
- Benefits:
  - Highly efficient nitrogen use
  - Reduces chemical fertilizer requirement by 50%
  - Environment friendly
  - One bottle replaces one bag of urea

**Vermicompost**
- Price: ₹250 per 50kg
- Benefits:
  - Improves soil structure
  - Increases water retention
  - Adds beneficial microorganisms
  - Slow release of nutrients
```

## Project Structure

```
Jai_Kisan/
├── README.md                    # This file
├── system_prompt.md             # Complete system prompt/requirements
├── jai_kisan_agent.py          # Core AI agent implementation
├── cli.py                       # Command-line interface
├── examples/
│   └── example_usage.md        # Detailed usage examples
└── data/
    ├── __init__.py
    ├── crops_data.py           # Crop NPK requirements
    ├── states_data.py          # State/region information
    └── fertilizer_data.py      # Fertilizer types and prices
```

## Data Sources

### Crop NPK Requirements
Based on:
- Indian Council of Agricultural Research (ICAR) guidelines
- State Department of Agriculture recommendations
- Soil Health Card program standards

### Fertilizer Prices
- Approximate 2026 market prices
- Based on historical trends and government subsidy patterns
- Prices may vary by region and season

### Soil Information
- Agro-climatic zone classifications
- Typical soil pH and characteristics by state
- Common soil-related challenges

## Key Principles

### 1. Environmental Stewardship (Core Principle)
- **Always recommend green alternatives first**
- Bio-fertilizers, organic manure, green manuring
- Encourage Soil Health Card usage
- Promote Nitrogen Use Efficiency (NUE)

### 2. Economic Sensitivity
- Prioritize affordable solutions for small holders
- Provide cost-saving alternatives
- Show clear price comparisons

### 3. Practical Guidance
- Clear, actionable advice
- Weather-based timing recommendations
- Simple language and metric conversions

### 4. Safety Guardrails
- Never recommend banned substances
- No unsafe chemical dosages
- Promote sustainable practices

## Persona: The Digital Village Elder

**Voice Characteristics:**
- Friendly and approachable
- Pragmatic and realistic
- Aware of local realities
- Encouraging and supportive
- Uses clear, practical advice

**Cultural Sensitivity:**
- Multilingual support framework
- Respects traditional farming wisdom
- Bridges modern technology with traditional knowledge
- Uses familiar units and measurements

## Future Enhancements

- [ ] Real-time weather API integration
- [ ] Multilingual natural language processing
- [ ] Mobile app interface
- [ ] Voice input/output support
- [ ] GPS-based location detection
- [ ] Market price API integration
- [ ] Soil Health Card digital integration
- [ ] Community forum for farmer interactions
- [ ] Government scheme recommendations
- [ ] Crop disease identification

## Contributing

We welcome contributions from:
- Agricultural scientists
- Farmers with practical experience
- Developers interested in AgriTech
- Data scientists and ML engineers
- UX designers for farmer-friendly interfaces

Please ensure contributions align with our core principles of:
1. Environmental stewardship
2. Economic sensitivity for small farmers
3. Scientific accuracy
4. Cultural appropriateness

## License

This project is open source and available for use in promoting sustainable agriculture in India.

## Support

For questions, suggestions, or feedback:
- Open an issue on GitHub
- Contribute to the discussion forum
- Share your farming success stories

## Acknowledgments

- Indian Council of Agricultural Research (ICAR)
- State Departments of Agriculture
- Soil Health Card Program
- Indian farmers who inspire this work

---

**जय किसान! (Victory to the Farmers!)**

*May your fields prosper and your soil stay healthy* 🌾
