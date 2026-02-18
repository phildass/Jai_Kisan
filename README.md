# (J)ai Kisan - जय किसान
**Your Digital Village Elder: An Intelligent Agricultural Consultant for Indian Farmers**

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌾 Overview

(J)ai Kisan is an AI-powered agricultural consultant designed specifically for the Indian farming community. Acting as a "Digital Village Elder," it provides intelligent, context-aware fertilizer recommendations that balance crop productivity with environmental sustainability.

**Indian Farmers AI Road To Prosperity**

## ✨ Key Features

- 🌱 **Comprehensive Crop Coverage**: 29+ major Indian crops across cereals, pulses, cash crops, oilseeds, and horticulture
- 🗺️ **Regional Intelligence**: State-specific soil information and agro-climatic zones for all Indian states
- 💰 **Economic Optimization**: Price comparisons between branded (IFFCO, Chambal, Coromandel) and generic fertilizers
- 🌍 **Environmental Stewardship**: Prioritizes organic and eco-friendly alternatives (Bhoomi Raksha principle)
- 📊 **Growth Stage Optimization**: Tailored N-P-K recommendations for each crop phase
- 🎙️ **Voice API Integration**: Multi-provider voice assistant support with automatic fallback (Bharati & Legacy)
- ⚡ **Zero Dependencies**: Pure Python implementation with no external requirements

## 🚀 Quick Start

> **Important:** This is a **Python Flask web application**, not a Node.js app. 
> Use `python` and `pip` commands, not `npm` or `yarn`.

### Installation

```bash
# Clone the repository
git clone https://github.com/phildass/Jai_Kisan.git
cd Jai_Kisan

# For CLI only - no installation needed (uses only Python standard library)
# For Web Application - install dependencies
pip install -r requirements.txt

# Configure environment (copy and edit .env file)
cp .env.example .env
```

**📘 New to deployment? See [SETUP.md](SETUP.md) for detailed step-by-step instructions.**

### Usage

**Quick Start Script (Easiest):**
```bash
chmod +x start.sh
./start.sh
# Automatically sets up environment and starts the app
```

**Web Application (Recommended):**
```bash
python app.py
# Visit http://localhost:5000 in your browser
# To run on a different port (e.g., 3050):
# Add PORT=3050 to your .env file
```

Features:
- User registration with OTP verification
- 24-hour free trial
- Payment integration (₹116.82)
- Mobile-friendly responsive design
- Download reports feature

**Command Line Interface:**
```bash
python cli.py
```

**Python API:**
```python
from jai_kisan_agent import JaiKisanAgent

agent = JaiKisanAgent()
response = agent.generate_response(
    crop="Paddy (Rice)",
    state="Punjab",
    growth_stage="Vegetative Phase (Leaves/Stem growth)"
)
print(response)
```

## 📖 Documentation


- **[SETUP.md](SETUP.md)** - **NEW!** Step-by-step local deployment guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment with DNS configuration
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - **NEW!** Common issues and solutions
- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Full feature guide and API reference

- **[Complete Documentation](DOCUMENTATION.md)** - Full feature guide and API reference
- **[Voice API Documentation](voice_api/README.md)** - Voice assistant integration guide

- **[System Prompt](system_prompt.md)** - Complete system requirements and persona definition
- **[Example Usage](examples/example_usage.md)** - Detailed scenarios and code examples

## 🌟 What Makes (J)ai Kisan Special?

### 1. **Environmental First**
Always recommends green alternatives before chemical fertilizers:
- Bio-fertilizers and organic manure
- Green manuring practices
- Nano Urea for efficient nitrogen use
- PROM (Phosphate Rich Organic Manure) as DAP alternative

### 2. **Economic Intelligence**
Saves farmers money through:
- Generic/Co-op fertilizer recommendations (save ₹125-150 per bag)
- Eco-smart mixing (1 bag chemical + 2 bags organic = 30% cost reduction)
- Soil Health Card integration to prevent over-fertilization

### 3. **Contextual Awareness**
- State-specific soil pH, type, and common issues
- Growth stage-specific nutrient requirements
- Weather-based timing recommendations
- Agro-climatic zone considerations

### 4. **Farmer-Friendly**
- Simple dropdown interface (Crop → State → Growth Stage)
- Multilingual support framework
- Clear, actionable advice in simple language
- "Digital Village Elder" persona - wise, approachable, practical

### 5. **Voice API Integration**
- Flexible multi-provider voice assistant support
- **Bharati Voice API**: Modern Bharat-VISTAAR 2026 platform with 15+ Indian languages
- **Legacy Voice API**: Traditional voice platform for established infrastructure
- Automatic provider selection based on region, user preference, or configuration
- Automatic fallback mechanism ensures reliability
- See [Voice API Documentation](voice_api/README.md) for details

## 📊 Supported Crops

**Cereals**: Paddy (Rice), Wheat, Maize, Bajra, Jowar, Ragi  
**Pulses**: Tur (Arhar), Moong, Gram (Chana), Masoor, Urad  
**Cash Crops**: Sugarcane, Cotton, Jute, Tobacco  
**Oilseeds**: Soybean, Groundnut, Mustard, Sunflower  
**Horticulture**: Tea, Coffee, Rubber, Potato, Onion, Tomato, Chili

## 🗺️ Regional Coverage

**North**: Punjab, Haryana, Uttar Pradesh, Rajasthan, Himachal Pradesh, Uttarakhand, J&K (UT)  
**West**: Gujarat, Maharashtra, Goa, Madhya Pradesh  
**South**: Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu  
**East & North-East**: West Bengal, Bihar, Jharkhand, Odisha, Assam, Sikkim, and all NE states

## 💡 Example Output

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

### 3. Price Comparison (Per 50kg Bag)
| Option | Nutrient Value | Approx. Price (₹) | Availability |
|--------|----------------|-------------------|---------------|
| IFFCO | 46-0-0 | ₹300 | High |
| Government Subsidized | 46-0-0 | ₹268 | High |

### 4. Eco-Smart Alternatives (Bhoomi Raksha)
**Nano Urea**: ₹240 per bottle
- One bottle replaces one bag of urea
- 50% reduction in chemical fertilizer requirement
- Highly efficient nitrogen use
```

## 🎯 Core Principles

1. **Environmental Stewardship** - Green alternatives first, always
2. **Economic Sensitivity** - Affordable solutions for small holders
3. **Scientific Accuracy** - Based on ICAR and Soil Health Card guidelines
4. **Practical Guidance** - Clear, actionable, weather-aware advice
5. **Cultural Appropriateness** - Respects Indian farming traditions

## 🔮 Future Enhancements

- [ ] Real-time weather API integration
- [ ] Multilingual NLP (Hindi, Marathi, Tamil, Telugu, etc.)
- [ ] Mobile app with voice input/output
- [ ] GPS-based location detection
- [ ] Live market price API integration
- [ ] Crop disease identification
- [ ] Government scheme recommendations
- [ ] Community forum for farmers

## 🤝 Contributing

We welcome contributions from:
- Agricultural scientists and researchers
- Farmers with practical experience
- Developers interested in AgriTech
- Data scientists and ML engineers
- UX designers for farmer-friendly interfaces

Please ensure contributions align with our core principles of environmental stewardship and economic sensitivity for small farmers.

## 📄 License

Open source - available for use in promoting sustainable agriculture in India.

## 🙏 Acknowledgments

- Indian Council of Agricultural Research (ICAR)
- State Departments of Agriculture
- Soil Health Card Program
- Indian farmers who inspire this work

---

**जय किसान! (Victory to the Farmers!)**

*May your fields prosper and your soil stay healthy* 🌾
