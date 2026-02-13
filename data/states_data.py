"""
State/Region Data for (J)ai Kisan System
Includes agro-climatic information and typical soil properties
"""

STATE_REGIONS = {
    "North": [
        "Punjab",
        "Haryana", 
        "Uttar Pradesh",
        "Rajasthan",
        "Himachal Pradesh",
        "Uttarakhand",
        "J&K (UT)"
    ],
    "West": [
        "Gujarat",
        "Maharashtra",
        "Goa",
        "Madhya Pradesh"
    ],
    "South": [
        "Andhra Pradesh",
        "Telangana",
        "Karnataka",
        "Kerala",
        "Tamil Nadu"
    ],
    "East & North-East": [
        "West Bengal",
        "Bihar",
        "Jharkhand",
        "Odisha",
        "Assam",
        "Sikkim",
        "Arunachal Pradesh",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Tripura"
    ]
}

# Typical soil pH ranges and characteristics by state
STATE_SOIL_INFO = {
    "Punjab": {
        "typical_ph": "7.0-8.5",
        "soil_type": "Alluvial, Sandy Loam",
        "common_issue": "Salinity in some areas",
        "agro_climatic_zone": "Trans-Gangetic Plains"
    },
    "Haryana": {
        "typical_ph": "7.5-8.5",
        "soil_type": "Alluvial",
        "common_issue": "Alkalinity, low organic matter",
        "agro_climatic_zone": "Trans-Gangetic Plains"
    },
    "Uttar Pradesh": {
        "typical_ph": "7.0-8.0",
        "soil_type": "Alluvial, Black",
        "common_issue": "Varies by region",
        "agro_climatic_zone": "Gangetic Plains"
    },
    "Maharashtra": {
        "typical_ph": "6.5-8.0",
        "soil_type": "Black (Vertisol), Laterite",
        "common_issue": "Low nitrogen, moisture stress",
        "agro_climatic_zone": "Deccan Plateau"
    },
    "West Bengal": {
        "typical_ph": "5.5-7.0",
        "soil_type": "Alluvial, Laterite",
        "common_issue": "Acidity in some areas",
        "agro_climatic_zone": "Eastern Plains"
    },
    "Tamil Nadu": {
        "typical_ph": "6.0-8.0",
        "soil_type": "Black, Red, Alluvial",
        "common_issue": "Salinity in coastal areas",
        "agro_climatic_zone": "Eastern Plateau and Hills"
    },
    "Karnataka": {
        "typical_ph": "6.0-7.5",
        "soil_type": "Red, Black, Laterite",
        "common_issue": "Erosion, low fertility",
        "agro_climatic_zone": "Deccan Plateau"
    },
    "Andhra Pradesh": {
        "typical_ph": "6.5-8.0",
        "soil_type": "Red, Black, Alluvial",
        "common_issue": "Salinity in coastal areas",
        "agro_climatic_zone": "Eastern Plateau"
    },
    "Gujarat": {
        "typical_ph": "7.0-8.5",
        "soil_type": "Black, Alluvial, Sandy",
        "common_issue": "Salinity, drought",
        "agro_climatic_zone": "Gujarat Plains"
    },
    "Rajasthan": {
        "typical_ph": "7.5-9.0",
        "soil_type": "Desert, Alluvial",
        "common_issue": "Low organic matter, drought",
        "agro_climatic_zone": "Western Dry Region"
    },
    "Bihar": {
        "typical_ph": "6.5-7.5",
        "soil_type": "Alluvial",
        "common_issue": "Flooding, waterlogging",
        "agro_climatic_zone": "Gangetic Plains"
    },
    "Odisha": {
        "typical_ph": "5.5-7.0",
        "soil_type": "Red, Laterite, Alluvial",
        "common_issue": "Acidity, low fertility",
        "agro_climatic_zone": "Eastern Plateau"
    }
}

# Cropping seasons
CROPPING_SEASONS = {
    "Kharif": {
        "months": "June-October",
        "description": "Monsoon crops",
        "common_crops": ["Paddy", "Cotton", "Sugarcane", "Bajra", "Jowar", "Tur", "Moong"]
    },
    "Rabi": {
        "months": "October-March", 
        "description": "Winter crops",
        "common_crops": ["Wheat", "Gram", "Mustard", "Potato", "Onion", "Masoor"]
    },
    "Zaid": {
        "months": "March-June",
        "description": "Summer crops",
        "common_crops": ["Watermelon", "Cucumber", "Moong", "Vegetables"]
    }
}
