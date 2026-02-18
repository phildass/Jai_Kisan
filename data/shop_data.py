"""
Shop Data for (J)ai Kisan System
Contains shop information, inventory, and e-Urvarak integration structure
"""

# Sample shop data (will be populated via e-Urvarak API in production)
SAMPLE_SHOPS = [
    {
        "id": "shop_001",
        "name": "Kisan Seva Kendra",
        "owner": "Ramesh Kumar",
        "mobile": "+91-9876543210",
        "address": "Main Market Road, Village Ramnagar",
        "district": "Ludhiana",
        "state": "Punjab",
        "latitude": 30.9010,
        "longitude": 75.8573,
        "license_number": "PB-LDH-2024-001",
        "inventory": {
            "Urea": {"stock_bags": 150, "price_per_50kg": 268, "last_updated": "2026-02-18T10:00:00"},
            "DAP": {"stock_bags": 80, "price_per_50kg": 1225, "last_updated": "2026-02-18T10:00:00"},
            "MOP": {"stock_bags": 45, "price_per_50kg": 850, "last_updated": "2026-02-18T10:00:00"},
            "NPK 10:26:26": {"stock_bags": 60, "price_per_50kg": 1150, "last_updated": "2026-02-18T10:00:00"}
        },
        "is_verified": True,
        "rating": 4.5,
        "total_reports": 23
    },
    {
        "id": "shop_002",
        "name": "Bharat Fertilizer Store",
        "owner": "Suresh Patel",
        "mobile": "+91-9876543211",
        "address": "Near Railway Station, Jalandhar Road",
        "district": "Ludhiana",
        "state": "Punjab",
        "latitude": 30.9100,
        "longitude": 75.8600,
        "license_number": "PB-LDH-2024-002",
        "inventory": {
            "Urea": {"stock_bags": 200, "price_per_50kg": 270, "last_updated": "2026-02-18T09:30:00"},
            "DAP": {"stock_bags": 120, "price_per_50kg": 1235, "last_updated": "2026-02-18T09:30:00"},
            "MOP": {"stock_bags": 70, "price_per_50kg": 860, "last_updated": "2026-02-18T09:30:00"},
            "NPK 20:20:0:13": {"stock_bags": 50, "price_per_50kg": 1080, "last_updated": "2026-02-18T09:30:00"}
        },
        "is_verified": True,
        "rating": 4.3,
        "total_reports": 18
    },
    {
        "id": "shop_003",
        "name": "Cooperative Society - Amritsar",
        "owner": "Punjab Agri Co-op",
        "mobile": "+91-9876543212",
        "address": "Cooperative Building, GT Road",
        "district": "Amritsar",
        "state": "Punjab",
        "latitude": 31.6340,
        "longitude": 74.8723,
        "license_number": "PB-ASR-2024-001",
        "inventory": {
            "Urea": {"stock_bags": 300, "price_per_50kg": 265, "last_updated": "2026-02-18T08:00:00"},
            "DAP": {"stock_bags": 150, "price_per_50kg": 1200, "last_updated": "2026-02-18T08:00:00"},
            "MOP": {"stock_bags": 100, "price_per_50kg": 840, "last_updated": "2026-02-18T08:00:00"},
            "NPK 10:26:26": {"stock_bags": 80, "price_per_50kg": 1140, "last_updated": "2026-02-18T08:00:00"}
        },
        "is_verified": True,
        "rating": 4.8,
        "total_reports": 45
    },
    {
        "id": "shop_004",
        "name": "Modern Agro Center",
        "owner": "Vikram Singh",
        "mobile": "+91-9876543213",
        "address": "Industrial Area, Phase 2",
        "district": "Patiala",
        "state": "Punjab",
        "latitude": 30.3398,
        "longitude": 76.3869,
        "license_number": "PB-PTL-2024-001",
        "inventory": {
            "Urea": {"stock_bags": 180, "price_per_50kg": 272, "last_updated": "2026-02-18T11:00:00"},
            "DAP": {"stock_bags": 95, "price_per_50kg": 1240, "last_updated": "2026-02-18T11:00:00"},
            "MOP": {"stock_bags": 55, "price_per_50kg": 855, "last_updated": "2026-02-18T11:00:00"},
            "NPK 20:20:0:13": {"stock_bags": 40, "price_per_50kg": 1090, "last_updated": "2026-02-18T11:00:00"}
        },
        "is_verified": True,
        "rating": 4.2,
        "total_reports": 12
    }
]

# Brand to Salt (Active Ingredient) mapping
BRAND_TO_SALT_MAPPING = {
    # DAP Products
    "IFFCO DAP": {"salt": "Di-Ammonium Phosphate", "npk": "18-46-0", "category": "DAP"},
    "Chambal DAP": {"salt": "Di-Ammonium Phosphate", "npk": "18-46-0", "category": "DAP"},
    "Coromandel DAP": {"salt": "Di-Ammonium Phosphate", "npk": "18-46-0", "category": "DAP"},
    "Generic DAP": {"salt": "Di-Ammonium Phosphate", "npk": "18-46-0", "category": "DAP"},
    
    # Urea Products
    "IFFCO Urea": {"salt": "Urea (CO(NH2)2)", "npk": "46-0-0", "category": "Urea"},
    "Chambal Urea": {"salt": "Urea (CO(NH2)2)", "npk": "46-0-0", "category": "Urea"},
    "Government Subsidized Urea": {"salt": "Urea (CO(NH2)2)", "npk": "46-0-0", "category": "Urea"},
    
    # MOP Products
    "IFFCO MOP": {"salt": "Muriate of Potash (KCl)", "npk": "0-0-60", "category": "MOP"},
    "Coromandel MOP": {"salt": "Muriate of Potash (KCl)", "npk": "0-0-60", "category": "MOP"},
    "Generic MOP": {"salt": "Muriate of Potash (KCl)", "npk": "0-0-60", "category": "MOP"},
    
    # NPK Complex
    "IFFCO NPK 10:26:26": {"salt": "NPK Complex", "npk": "10-26-26", "category": "NPK 10:26:26"},
    "Coromandel NPK 10:26:26": {"salt": "NPK Complex", "npk": "10-26-26", "category": "NPK 10:26:26"},
    
    "Chambal NPK 20:20:0:13": {"salt": "NPK Complex with Sulphur", "npk": "20-20-0-13", "category": "NPK 20:20:0:13"},
    "IFFCO NPK 20:20:0:13": {"salt": "NPK Complex with Sulphur", "npk": "20-20-0-13", "category": "NPK 20:20:0:13"},
}

# Kifayati (Economical) alternatives mapping
KIFAYATI_ALTERNATIVES = {
    "DAP": {
        "branded_average_price": 1360,
        "kifayati_option": {
            "name": "Co-operative DAP",
            "price_per_50kg": 1200,
            "savings_per_bag": 160,
            "salt": "Di-Ammonium Phosphate",
            "npk": "18-46-0"
        }
    },
    "Urea": {
        "branded_average_price": 302,
        "kifayati_option": {
            "name": "Government Subsidized Urea",
            "price_per_50kg": 268,
            "savings_per_bag": 34,
            "salt": "Urea (CO(NH2)2)",
            "npk": "46-0-0"
        }
    },
    "MOP": {
        "branded_average_price": 910,
        "kifayati_option": {
            "name": "Co-operative MOP",
            "price_per_50kg": 840,
            "savings_per_bag": 70,
            "salt": "Muriate of Potash (KCl)",
            "npk": "0-0-60"
        }
    },
    "NPK 10:26:26": {
        "branded_average_price": 1210,
        "kifayati_option": {
            "name": "Co-operative NPK 10:26:26",
            "price_per_50kg": 1140,
            "savings_per_bag": 70,
            "salt": "NPK Complex",
            "npk": "10-26-26"
        }
    },
    "NPK 20:20:0:13": {
        "branded_average_price": 1110,
        "kifayati_option": {
            "name": "Co-operative NPK 20:20:0:13",
            "price_per_50kg": 1050,
            "savings_per_bag": 60,
            "salt": "NPK Complex with Sulphur",
            "npk": "20-20-0-13"
        }
    }
}

# e-Urvarak API configuration (mock structure)
E_URVARAK_CONFIG = {
    "api_url": "https://ifms.gov.in/api/v1/",  # Mock URL
    "endpoints": {
        "shop_list": "shops/list",
        "shop_inventory": "shops/{shop_id}/inventory",
        "shop_by_location": "shops/nearby"
    },
    "cache_duration_minutes": 30,
    "retry_attempts": 3,
    "timeout_seconds": 10
}

# Dosage calculation rules (per hectare)
DOSAGE_CALCULATION_RULES = {
    "Paddy (Rice)": {
        "Field Preparation (Basal Dose)": {
            "urea_kg": 60,
            "dap_kg": 100,
            "mop_kg": 40,
            "area_factor": 1.0
        },
        "Vegetative Phase (Leaves/Stem growth)": {
            "urea_kg": 80,
            "area_factor": 1.0
        },
        "Flowering/Reproductive Phase": {
            "urea_kg": 40,
            "mop_kg": 20,
            "area_factor": 1.0
        }
    },
    "Wheat": {
        "Field Preparation (Basal Dose)": {
            "urea_kg": 50,
            "dap_kg": 90,
            "mop_kg": 30,
            "area_factor": 1.0
        },
        "Vegetative Phase (Leaves/Stem growth)": {
            "urea_kg": 70,
            "area_factor": 1.0
        },
        "Grain Filling/Fruit Development": {
            "urea_kg": 30,
            "area_factor": 1.0
        }
    },
    "Cotton": {
        "Field Preparation (Basal Dose)": {
            "urea_kg": 40,
            "dap_kg": 80,
            "mop_kg": 50,
            "area_factor": 1.0
        },
        "Vegetative Phase (Leaves/Stem growth)": {
            "urea_kg": 60,
            "mop_kg": 30,
            "area_factor": 1.0
        },
        "Flowering/Reproductive Phase": {
            "urea_kg": 50,
            "mop_kg": 40,
            "area_factor": 1.0
        }
    },
    "default": {
        "Field Preparation (Basal Dose)": {
            "urea_kg": 50,
            "dap_kg": 75,
            "mop_kg": 35,
            "area_factor": 1.0
        },
        "Vegetative Phase (Leaves/Stem growth)": {
            "urea_kg": 60,
            "area_factor": 1.0
        },
        "Flowering/Reproductive Phase": {
            "urea_kg": 40,
            "mop_kg": 25,
            "area_factor": 1.0
        }
    }
}

# Group buying thresholds (minimum for bulk discount)
GROUP_BUYING_THRESHOLDS = {
    "Urea": {"min_bags": 50, "min_farmers": 5, "discount_percent": 3},
    "DAP": {"min_bags": 40, "min_farmers": 5, "discount_percent": 5},
    "MOP": {"min_bags": 30, "min_farmers": 4, "discount_percent": 4},
    "NPK 10:26:26": {"min_bags": 35, "min_farmers": 4, "discount_percent": 4},
    "NPK 20:20:0:13": {"min_bags": 35, "min_farmers": 4, "discount_percent": 4}
}

# Kisan Points reward structure
KISAN_POINTS_REWARDS = {
    "report_stock_available": 5,
    "report_shop_closed": 3,
    "report_price_update": 10,
    "join_group_buying": 8,
    "complete_group_purchase": 15,
    "refer_farmer": 20,
    "verified_report_bonus": 5  # Extra points if report is verified by others
}
