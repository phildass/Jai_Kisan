"""
Crop Data for (J)ai Kisan System
Contains N-P-K ratios and requirements for major Indian crops
"""

CROP_CATEGORIES = {
    "Cereals": ["Paddy (Rice)", "Wheat", "Maize", "Bajra", "Jowar", "Ragi"],
    "Pulses": ["Tur (Arhar)", "Moong", "Gram (Chana)", "Masoor", "Urad"],
    "Cash Crops": ["Sugarcane", "Cotton", "Jute", "Tobacco"],
    "Oilseeds": ["Soybean", "Groundnut", "Mustard", "Sunflower"],
    "Plantation/Horticulture": ["Tea", "Coffee", "Rubber", "Potato", "Onion", "Tomato", "Chili"]
}

# N-P-K requirements (kg/hectare) for major crops by growth stage
CROP_NPK_REQUIREMENTS = {
    "Paddy (Rice)": {
        "Field Preparation (Basal Dose)": {"N": 40, "P": 20, "K": 20},
        "Sowing/Early Growth": {"N": 20, "P": 10, "K": 10},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 40, "P": 10, "K": 20},
        "Flowering & Fruiting": {"N": 20, "P": 10, "K": 20},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 10}
    },
    "Wheat": {
        "Field Preparation (Basal Dose)": {"N": 40, "P": 30, "K": 20},
        "Sowing/Early Growth": {"N": 20, "P": 10, "K": 10},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 40, "P": 10, "K": 10},
        "Flowering & Fruiting": {"N": 20, "P": 5, "K": 10},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 5}
    },
    "Sugarcane": {
        "Field Preparation (Basal Dose)": {"N": 60, "P": 40, "K": 40},
        "Sowing/Early Growth": {"N": 40, "P": 20, "K": 20},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 80, "P": 20, "K": 40},
        "Flowering & Fruiting": {"N": 40, "P": 10, "K": 40},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 20}
    },
    "Cotton": {
        "Field Preparation (Basal Dose)": {"N": 40, "P": 30, "K": 30},
        "Sowing/Early Growth": {"N": 20, "P": 10, "K": 10},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 40, "P": 15, "K": 20},
        "Flowering & Fruiting": {"N": 30, "P": 15, "K": 30},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 10}
    },
    "Tur (Arhar)": {
        "Field Preparation (Basal Dose)": {"N": 20, "P": 40, "K": 20},
        "Sowing/Early Growth": {"N": 10, "P": 15, "K": 10},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 10, "P": 10, "K": 10},
        "Flowering & Fruiting": {"N": 10, "P": 15, "K": 20},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 5}
    },
    "Soybean": {
        "Field Preparation (Basal Dose)": {"N": 20, "P": 40, "K": 20},
        "Sowing/Early Growth": {"N": 10, "P": 15, "K": 10},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 10, "P": 15, "K": 15},
        "Flowering & Fruiting": {"N": 10, "P": 20, "K": 20},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 10}
    },
    "Potato": {
        "Field Preparation (Basal Dose)": {"N": 50, "P": 50, "K": 50},
        "Sowing/Early Growth": {"N": 30, "P": 20, "K": 20},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 40, "P": 20, "K": 30},
        "Flowering & Fruiting": {"N": 30, "P": 10, "K": 50},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 20}
    },
    "Onion": {
        "Field Preparation (Basal Dose)": {"N": 40, "P": 30, "K": 30},
        "Sowing/Early Growth": {"N": 20, "P": 15, "K": 15},
        "Vegetative Phase (Leaves/Stem growth)": {"N": 40, "P": 15, "K": 20},
        "Flowering & Fruiting": {"N": 20, "P": 10, "K": 30},
        "Pre-Harvest": {"N": 0, "P": 0, "K": 15}
    }
}

# Default NPK for crops not in detailed list
DEFAULT_NPK = {
    "Maize": {"N": 120, "P": 60, "K": 40},
    "Bajra": {"N": 80, "P": 40, "K": 40},
    "Jowar": {"N": 80, "P": 40, "K": 40},
    "Ragi": {"N": 50, "P": 40, "K": 25},
    "Moong": {"N": 20, "P": 40, "K": 20},
    "Gram (Chana)": {"N": 20, "P": 40, "K": 20},
    "Masoor": {"N": 20, "P": 40, "K": 20},
    "Urad": {"N": 25, "P": 50, "K": 25},
    "Jute": {"N": 60, "P": 30, "K": 30},
    "Tobacco": {"N": 80, "P": 40, "K": 60},
    "Groundnut": {"N": 25, "P": 50, "K": 50},
    "Mustard": {"N": 80, "P": 40, "K": 40},
    "Sunflower": {"N": 60, "P": 60, "K": 40},
    "Tea": {"N": 100, "P": 40, "K": 40},
    "Coffee": {"N": 80, "P": 40, "K": 80},
    "Rubber": {"N": 60, "P": 30, "K": 60},
    "Tomato": {"N": 120, "P": 60, "K": 60},
    "Chili": {"N": 100, "P": 50, "K": 50}
}
