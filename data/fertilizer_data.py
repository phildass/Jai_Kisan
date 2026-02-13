"""
Fertilizer Data for (J)ai Kisan System
Contains fertilizer types, brands, NPK ratios, and market prices
"""

# Common fertilizer types and their NPK ratios
FERTILIZER_TYPES = {
    "Urea": {
        "npk": "46-0-0",
        "nutrient_content": {"N": 46, "P": 0, "K": 0},
        "description": "High nitrogen source for vegetative growth"
    },
    "DAP": {
        "npk": "18-46-0",
        "nutrient_content": {"N": 18, "P": 46, "K": 0},
        "description": "Diammonium Phosphate - good phosphorus source"
    },
    "MOP": {
        "npk": "0-0-60",
        "nutrient_content": {"N": 0, "P": 0, "K": 60},
        "description": "Muriate of Potash - potassium source"
    },
    "SSP": {
        "npk": "0-16-0",
        "nutrient_content": {"N": 0, "P": 16, "K": 0, "S": 11},
        "description": "Single Super Phosphate - contains sulphur"
    },
    "NPK 10:26:26": {
        "npk": "10-26-26",
        "nutrient_content": {"N": 10, "P": 26, "K": 26},
        "description": "Balanced fertilizer for general use"
    },
    "NPK 12:32:16": {
        "npk": "12-32-16",
        "nutrient_content": {"N": 12, "P": 32, "K": 16},
        "description": "Complex fertilizer with higher phosphorus"
    },
    "NPK 20:20:0:13": {
        "npk": "20-20-0-13",
        "nutrient_content": {"N": 20, "P": 20, "K": 0, "S": 13},
        "description": "Balanced with sulphur"
    },
    "Ammonium Sulphate": {
        "npk": "20-0-0",
        "nutrient_content": {"N": 20, "P": 0, "K": 0, "S": 24},
        "description": "Nitrogen with sulphur"
    }
}

# Branded fertilizers (approx. prices in ₹ per 50kg bag - 2026 estimates)
BRANDED_FERTILIZERS = {
    "DAP": [
        {"brand": "IFFCO", "npk": "18-46-0", "price_per_50kg": 1350, "availability": "High"},
        {"brand": "Chambal", "npk": "18-46-0", "price_per_50kg": 1375, "availability": "High"},
        {"brand": "Coromandel", "npk": "18-46-0", "price_per_50kg": 1360, "availability": "High"},
        {"brand": "Generic/Co-op", "npk": "18-46-0", "price_per_50kg": 1225, "availability": "Medium"}
    ],
    "Urea": [
        {"brand": "IFFCO", "npk": "46-0-0", "price_per_50kg": 300, "availability": "High"},
        {"brand": "Chambal", "npk": "46-0-0", "price_per_50kg": 305, "availability": "High"},
        {"brand": "Government Subsidized", "npk": "46-0-0", "price_per_50kg": 268, "availability": "High"}
    ],
    "MOP": [
        {"brand": "IFFCO", "npk": "0-0-60", "price_per_50kg": 900, "availability": "Medium"},
        {"brand": "Coromandel", "npk": "0-0-60", "price_per_50kg": 920, "availability": "Medium"},
        {"brand": "Generic", "npk": "0-0-60", "price_per_50kg": 850, "availability": "Medium"}
    ],
    "NPK 10:26:26": [
        {"brand": "IFFCO", "npk": "10-26-26", "price_per_50kg": 1200, "availability": "High"},
        {"brand": "Coromandel", "npk": "10-26-26", "price_per_50kg": 1220, "availability": "High"}
    ],
    "NPK 20:20:0:13": [
        {"brand": "Chambal", "npk": "20-20-0-13", "price_per_50kg": 1100, "availability": "Medium"},
        {"brand": "IFFCO", "npk": "20-20-0-13", "price_per_50kg": 1120, "availability": "Medium"}
    ]
}

# Organic and eco-friendly alternatives
ECO_ALTERNATIVES = {
    "Vermicompost": {
        "type": "Organic",
        "npk_approx": "1.5-1.0-1.5",
        "price_per_50kg": 250,
        "benefits": [
            "Improves soil structure",
            "Increases water retention",
            "Adds beneficial microorganisms",
            "Slow release of nutrients"
        ]
    },
    "PROM (Phosphate Rich Organic Manure)": {
        "type": "Organic",
        "npk_approx": "3-9-1",
        "price_per_50kg": 300,
        "benefits": [
            "Good phosphorus source",
            "Improves soil health",
            "Cost-effective alternative to DAP"
        ]
    },
    "Farm Yard Manure (FYM)": {
        "type": "Organic",
        "npk_approx": "0.5-0.2-0.5",
        "price_per_ton": 2000,
        "benefits": [
            "Improves soil fertility",
            "Adds organic carbon",
            "Improves soil water holding capacity"
        ]
    },
    "Neem Cake": {
        "type": "Organic",
        "npk_approx": "5-1-1",
        "price_per_50kg": 800,
        "benefits": [
            "Natural pest deterrent",
            "Slow release nitrogen",
            "Improves soil health"
        ]
    },
    "Green Manure": {
        "type": "Practice",
        "cost": "Seed cost only (~₹500-1000/hectare)",
        "benefits": [
            "Free nitrogen fixation (for legumes)",
            "Adds organic matter",
            "Improves soil structure",
            "Weed suppression"
        ],
        "common_crops": ["Dhaincha", "Sunhemp", "Cowpea", "Cluster bean"]
    },
    "Nano Urea": {
        "type": "Advanced",
        "npk_approx": "4-0-0 (liquid, 500ml bottle)",
        "price_per_bottle": 240,
        "benefits": [
            "Highly efficient nitrogen use",
            "Reduces chemical fertilizer requirement by 50%",
            "Environment friendly",
            "One bottle replaces one bag of urea"
        ]
    }
}

# Growth stage specific fertilizer recommendations
GROWTH_STAGE_FERTILIZERS = {
    "Field Preparation (Basal Dose)": {
        "primary": ["DAP", "SSP", "NPK Complex"],
        "eco_alternative": ["PROM", "FYM", "Vermicompost"],
        "timing": "Apply 1-2 weeks before sowing/planting"
    },
    "Sowing/Early Growth": {
        "primary": ["Urea", "DAP"],
        "eco_alternative": ["Vermicompost", "Neem Cake"],
        "timing": "Apply at the time of sowing or within 2 weeks"
    },
    "Vegetative Phase (Leaves/Stem growth)": {
        "primary": ["Urea", "Nano Urea"],
        "eco_alternative": ["Liquid bio-fertilizers", "Vermicompost tea"],
        "timing": "Split application - 3-4 weeks after sowing"
    },
    "Flowering & Fruiting": {
        "primary": ["MOP", "NPK 10:26:26"],
        "eco_alternative": ["Wood ash (for K)", "Vermicompost"],
        "timing": "At flower initiation stage"
    },
    "Pre-Harvest": {
        "primary": ["MOP (if needed)"],
        "eco_alternative": ["Light organic supplements"],
        "timing": "2-3 weeks before harvest, minimal application"
    }
}
