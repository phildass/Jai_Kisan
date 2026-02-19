"""
Crop Health Data for (J)ai Kisan System
Contains pest/disease knowledge base, IPM recommendations, and regulatory information
"""

# Major pests and diseases for Indian crops organized by crop and season
CROP_PESTS_DISEASES = {
    "Paddy (Rice)": {
        "pests": [
            {
                "name": "Brown Planthopper",
                "scientific_name": "Nilaparvata lugens",
                "peak_season": ["Kharif"],
                "regions": ["South", "East"],
                "symptoms": "Yellowing and drying of plants from base, hopper burn",
                "etl_threshold": "5-10 hoppers per plant"
            },
            {
                "name": "Stem Borer",
                "scientific_name": "Scirpophaga incertulas",
                "peak_season": ["Kharif", "Rabi"],
                "regions": ["All"],
                "symptoms": "Dead hearts in vegetative stage, white ear heads",
                "etl_threshold": "2-5% dead hearts or 1-2 egg masses per m²"
            },
            {
                "name": "Leaf Folder",
                "scientific_name": "Cnaphalocrocis medinalis",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Longitudinal leaf folding, whitish streaks",
                "etl_threshold": "1-2 larvae or fresh damage on 2-3 leaves per plant"
            }
        ],
        "diseases": [
            {
                "name": "Blast",
                "scientific_name": "Pyricularia oryzae",
                "type": "Fungal",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Spindle-shaped lesions with grey centers on leaves, neck blast",
                "favorable_conditions": "High humidity (>90%), 25-28°C, cloudy weather"
            },
            {
                "name": "Bacterial Leaf Blight",
                "scientific_name": "Xanthomonas oryzae",
                "type": "Bacterial",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Water-soaked lesions turning yellow, wavy leaf margins",
                "favorable_conditions": "High humidity, 25-34°C, wind and rain"
            },
            {
                "name": "Sheath Blight",
                "scientific_name": "Rhizoctonia solani",
                "type": "Fungal",
                "peak_season": ["Kharif", "Rabi"],
                "regions": ["All"],
                "symptoms": "Oval greenish-grey lesions on leaf sheath near waterline",
                "favorable_conditions": "High nitrogen, dense planting, high humidity"
            }
        ]
    },
    "Wheat": {
        "pests": [
            {
                "name": "Aphid",
                "scientific_name": "Rhopalosiphum maidis",
                "peak_season": ["Rabi"],
                "regions": ["North", "Central"],
                "symptoms": "Yellowing of leaves, stunted growth, honeydew secretion",
                "etl_threshold": "5-10 aphids per tiller"
            },
            {
                "name": "Termite",
                "scientific_name": "Odontotermes obesus",
                "peak_season": ["Rabi"],
                "regions": ["North", "Central"],
                "symptoms": "Drying and wilting of plants, presence of mud tubes",
                "etl_threshold": "10% plant damage at seedling stage"
            }
        ],
        "diseases": [
            {
                "name": "Yellow Rust",
                "scientific_name": "Puccinia striiformis",
                "type": "Fungal",
                "peak_season": ["Rabi"],
                "regions": ["North", "North-East"],
                "symptoms": "Yellow to orange pustules in linear rows on leaves",
                "favorable_conditions": "Cool temperature (10-15°C), high humidity"
            },
            {
                "name": "Brown Rust",
                "scientific_name": "Puccinia recondita",
                "type": "Fungal",
                "peak_season": ["Rabi"],
                "regions": ["North", "Central"],
                "symptoms": "Orange-brown pustules scattered on leaf surface",
                "favorable_conditions": "Warm temperature (20-25°C), dew on leaves"
            },
            {
                "name": "Powdery Mildew",
                "scientific_name": "Erysiphe graminis",
                "type": "Fungal",
                "peak_season": ["Rabi"],
                "regions": ["North"],
                "symptoms": "White powdery growth on leaves and stems",
                "favorable_conditions": "Moderate temperature, high humidity, cloudy weather"
            }
        ]
    },
    "Cotton": {
        "pests": [
            {
                "name": "Pink Bollworm",
                "scientific_name": "Pectinophora gossypiella",
                "peak_season": ["Kharif"],
                "regions": ["North", "Central", "South"],
                "symptoms": "Rosette flowers, entry holes in green bolls with webbed frass",
                "etl_threshold": "10% rosette flowers or 8-10% green bolls with damage"
            },
            {
                "name": "American Bollworm",
                "scientific_name": "Helicoverpa armigera",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Damaged squares, flowers, and bolls with entry holes",
                "etl_threshold": "1-2 larvae per plant or 10% damaged fruiting bodies"
            },
            {
                "name": "Whitefly",
                "scientific_name": "Bemisia tabaci",
                "peak_season": ["Kharif"],
                "regions": ["North", "Central"],
                "symptoms": "Yellowing of leaves, honeydew, sooty mold, leaf curling",
                "etl_threshold": "5-6 adults per leaf"
            },
            {
                "name": "Aphid",
                "scientific_name": "Aphis gossypii",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Curling of leaves, stunted growth, honeydew secretion",
                "etl_threshold": "10-15 aphids per leaf"
            }
        ],
        "diseases": [
            {
                "name": "Cotton Leaf Curl Disease",
                "scientific_name": "Begomovirus",
                "type": "Viral",
                "peak_season": ["Kharif"],
                "regions": ["North"],
                "symptoms": "Upward/downward leaf curling, vein thickening, stunting",
                "favorable_conditions": "Whitefly vector, 25-35°C temperature"
            },
            {
                "name": "Wilt",
                "scientific_name": "Fusarium oxysporum",
                "type": "Fungal",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Yellowing and drooping of leaves, wilting, vascular browning",
                "favorable_conditions": "25-32°C, acidic soil, moisture stress"
            }
        ]
    },
    "Tomato": {
        "pests": [
            {
                "name": "Fruit Borer",
                "scientific_name": "Helicoverpa armigera",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Holes in fruits, larvae inside fruits",
                "etl_threshold": "1-2 larvae per plant or 5% fruit damage"
            },
            {
                "name": "Leaf Miner",
                "scientific_name": "Liriomyza trifolii",
                "peak_season": ["Summer", "Kharif"],
                "regions": ["All"],
                "symptoms": "Serpentine mines on leaves, whitish patches",
                "etl_threshold": "3-4 mines per leaf"
            }
        ],
        "diseases": [
            {
                "name": "Early Blight",
                "scientific_name": "Alternaria solani",
                "type": "Fungal",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Concentric brown rings on older leaves, target spot pattern",
                "favorable_conditions": "Warm humid weather, 24-29°C, heavy dew"
            },
            {
                "name": "Late Blight",
                "scientific_name": "Phytophthora infestans",
                "type": "Fungal",
                "peak_season": ["Winter"],
                "regions": ["All"],
                "symptoms": "Water-soaked irregular lesions on leaves, white mold on underside",
                "favorable_conditions": "Cool humid weather, 10-25°C, high rainfall"
            },
            {
                "name": "Tomato Leaf Curl Virus",
                "scientific_name": "Begomovirus",
                "type": "Viral",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Severe leaf curling, reduced leaf size, stunted growth",
                "favorable_conditions": "Whitefly vector, warm weather"
            }
        ]
    },
    "Potato": {
        "pests": [
            {
                "name": "Aphid",
                "scientific_name": "Myzus persicae",
                "peak_season": ["Rabi"],
                "regions": ["North"],
                "symptoms": "Curled leaves, stunted growth, virus transmission",
                "etl_threshold": "10-15 aphids per leaf"
            }
        ],
        "diseases": [
            {
                "name": "Late Blight",
                "scientific_name": "Phytophthora infestans",
                "type": "Fungal",
                "peak_season": ["Rabi"],
                "regions": ["North", "North-East"],
                "symptoms": "Water-soaked lesions on leaves, white mold underneath",
                "favorable_conditions": "High humidity (>90%), 15-20°C, cloudy weather"
            },
            {
                "name": "Early Blight",
                "scientific_name": "Alternaria solani",
                "type": "Fungal",
                "peak_season": ["Rabi"],
                "regions": ["All"],
                "symptoms": "Concentric rings on leaves, target spot pattern",
                "favorable_conditions": "Warm humid weather, 24-29°C"
            }
        ]
    },
    "Onion": {
        "pests": [
            {
                "name": "Thrips",
                "scientific_name": "Thrips tabaci",
                "peak_season": ["Rabi", "Kharif"],
                "regions": ["All"],
                "symptoms": "Silver streaks on leaves, distorted growth",
                "etl_threshold": "30-40 thrips per plant"
            }
        ],
        "diseases": [
            {
                "name": "Purple Blotch",
                "scientific_name": "Alternaria porri",
                "type": "Fungal",
                "peak_season": ["Rabi", "Kharif"],
                "regions": ["All"],
                "symptoms": "Purple lesions with concentric rings on leaves",
                "favorable_conditions": "High humidity, 21-30°C, heavy dew"
            }
        ]
    },
    "Chili": {
        "pests": [
            {
                "name": "Thrips",
                "scientific_name": "Scirtothrips dorsalis",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Silvery streaks on leaves, curling, distortion",
                "etl_threshold": "25-30 thrips per leaf"
            },
            {
                "name": "Fruit Borer",
                "scientific_name": "Helicoverpa armigera",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Holes in fruits with larvae inside",
                "etl_threshold": "1-2 larvae per plant or 5% fruit damage"
            }
        ],
        "diseases": [
            {
                "name": "Anthracnose",
                "scientific_name": "Colletotrichum capsici",
                "type": "Fungal",
                "peak_season": ["Kharif"],
                "regions": ["All"],
                "symptoms": "Circular sunken spots on ripe fruits",
                "favorable_conditions": "High humidity, 25-30°C, rain"
            },
            {
                "name": "Leaf Curl",
                "scientific_name": "Chili Leaf Curl Virus",
                "type": "Viral",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Upward/downward curling, reduced leaf size, yellowing",
                "favorable_conditions": "Whitefly vector, warm weather"
            }
        ]
    },
    "Sugarcane": {
        "pests": [
            {
                "name": "Early Shoot Borer",
                "scientific_name": "Chilo infuscatellus",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Dead hearts, drying of central leaves",
                "etl_threshold": "10% dead hearts"
            },
            {
                "name": "Top Borer",
                "scientific_name": "Scirpophaga excerptalis",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Bunchy top, drying of top leaves",
                "etl_threshold": "5-10% bunchy top symptoms"
            }
        ],
        "diseases": [
            {
                "name": "Red Rot",
                "scientific_name": "Colletotrichum falcatum",
                "type": "Fungal",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Reddening and drying of leaves, red discoloration inside stem",
                "favorable_conditions": "High humidity, 25-32°C, waterlogged conditions"
            },
            {
                "name": "Smut",
                "scientific_name": "Ustilago scitaminea",
                "type": "Fungal",
                "peak_season": ["All"],
                "regions": ["All"],
                "symptoms": "Long whip-like growth from top, reduced cane formation",
                "favorable_conditions": "Cool weather during germination"
            }
        ]
    }
}

# 3-Tier IPM (Integrated Pest Management) Recommendations
IPM_RECOMMENDATIONS = {
    "Tier1_Prevention": {
        "name": "Bhoomi Raksha (Prevention)",
        "priority": 1,
        "methods": [
            {
                "method": "Seed Treatment",
                "description": "Treat seeds with bio-agents before sowing",
                "materials": [
                    "Trichoderma viride @ 4g/kg seed",
                    "Pseudomonas fluorescens @ 10g/kg seed",
                    "Turmeric powder + Neem leaf extract (Desi method)"
                ],
                "cost_estimate": "₹50-100 per acre",
                "application_time": "Before sowing"
            },
            {
                "method": "Deep Summer Ploughing",
                "description": "Expose soil to sunlight to kill pest eggs and larvae",
                "materials": ["Tractor/bullock for ploughing"],
                "cost_estimate": "₹800-1200 per acre",
                "application_time": "May-June (peak summer)",
                "effectiveness": "Reduces soil-borne pests by 60-70%"
            },
            {
                "method": "Crop Rotation",
                "description": "Rotate crops to break pest cycles",
                "crop_families": {
                    "Solanaceae": ["Tomato", "Potato", "Chili", "Brinjal"],
                    "Brassicaceae": ["Cabbage", "Cauliflower", "Mustard"],
                    "Cucurbitaceae": ["Cucumber", "Pumpkin", "Watermelon"],
                    "Leguminosae": ["Tur (Arhar)", "Moong", "Gram (Chana)", "Masoor", "Urad", "Groundnut", "Soybean"]
                },
                "rules": [
                    "Never plant same family crops consecutively (e.g., Tomato after Potato)",
                    "Follow cereals with legumes to restore soil nitrogen",
                    "Include deep-rooted and shallow-rooted crops alternately"
                ],
                "cost_estimate": "No additional cost",
                "application_time": "Planning stage"
            },
            {
                "method": "Field Sanitation",
                "description": "Remove crop residues and weeds to reduce pest carryover",
                "materials": ["Labor for cleaning"],
                "cost_estimate": "₹500-800 per acre",
                "application_time": "After harvest and before sowing",
                "effectiveness": "Reduces pest carryover by 40-50%"
            },
            {
                "method": "Resistant Varieties",
                "description": "Use pest/disease resistant varieties",
                "materials": ["Certified seeds of resistant varieties"],
                "cost_estimate": "₹200-500 extra per acre",
                "application_time": "At sowing",
                "effectiveness": "50-80% reduction in pest/disease incidence"
            },
            {
                "method": "Balanced Fertilization",
                "description": "Avoid excess nitrogen which attracts sucking pests",
                "materials": ["Soil test-based fertilizers"],
                "cost_estimate": "No additional cost (actually saves money)",
                "application_time": "Throughout crop growth",
                "effectiveness": "Reduces aphids, whiteflies by 30-40%"
            }
        ]
    },
    "Tier2_Organic_Mechanical": {
        "name": "Jugaad (Low-Cost Organic & Mechanical)",
        "priority": 2,
        "methods": [
            {
                "method": "Yellow Sticky Traps",
                "description": "Attract and trap flying insects like whiteflies, aphids",
                "materials": ["Yellow plastic sheets", "Castor oil/grease", "Bamboo sticks"],
                "recipe": "Apply castor oil on 30cm x 15cm yellow sheets, mount on sticks at crop height",
                "cost_estimate": "₹150-250 per acre (20-25 traps)",
                "application_time": "Install at crop emergence, replace every 2-3 weeks",
                "effectiveness": "60-70% reduction in whitefly, aphid populations",
                "suitable_for": ["Cotton", "Tomato", "Chili", "Onion"]
            },
            {
                "method": "Light Traps",
                "description": "Attract night-flying moths and beetles",
                "materials": ["Electric bulb (40W) or kerosene lamp", "Bowl with water + kerosene"],
                "recipe": "Install light 1-2 feet above water bowl, insects fall in water",
                "cost_estimate": "₹300-500 per acre (2-3 traps)",
                "application_time": "Evening hours during pest active period",
                "effectiveness": "Catches adult moths, reduces egg-laying by 40-50%",
                "suitable_for": ["Paddy (Rice)", "Cotton", "Sugarcane"]
            },
            {
                "method": "Bird Perches",
                "description": "Invite natural predators (birds) to control caterpillars",
                "materials": ["Bamboo poles or tree branches"],
                "recipe": "Install 10-15 T-shaped perches per acre at 5-6 feet height",
                "cost_estimate": "₹100-200 per acre",
                "application_time": "Install after crop is 2-3 weeks old",
                "effectiveness": "Birds eat 40-60 larvae per day per perch",
                "suitable_for": ["All crops"]
            },
            {
                "method": "Neem Oil Spray",
                "description": "Broad-spectrum organic pest repellent",
                "materials": ["Neem oil 1000-1500 ml", "Water 200 liters", "Soap solution 100ml as emulsifier"],
                "recipe": "Mix neem oil + soap in small water, then dilute to 200L. Spray on leaves (both sides)",
                "cost_estimate": "₹400-600 per acre per spray",
                "application_time": "Early morning or evening, avoid flowering period",
                "effectiveness": "70-80% control of soft-bodied insects, some fungi",
                "suitable_for": ["All crops"],
                "safety": "Safe for beneficial insects if used properly, wait 3 days before harvest"
            },
            {
                "method": "Dashparni Arka (10-Leaf Extract)",
                "description": "Traditional multi-plant pest repellent",
                "materials": [
                    "Neem leaves 2kg", "Custard apple leaves 2kg", "Guava leaves 2kg",
                    "Pomegranate leaves 2kg", "Papaya leaves 2kg", "Cow urine 5L", "Water 10L"
                ],
                "recipe": "Mix all leaves + cow urine + water, boil 30 min, cool, filter. Dilute 1:10 before spray",
                "cost_estimate": "₹200-300 per acre per spray",
                "application_time": "Weekly sprays during pest infestation",
                "effectiveness": "60-70% control of sucking and chewing pests",
                "suitable_for": ["All crops"],
                "preparation_time": "2 hours"
            },
            {
                "method": "Garlic-Chili-Ginger Spray",
                "description": "Strong pest deterrent spray",
                "materials": ["Garlic 250g", "Green chili 250g", "Ginger 100g", "Soap 50g", "Water 10L"],
                "recipe": "Grind garlic + chili + ginger, soak overnight in water, filter, add soap, spray",
                "cost_estimate": "₹100-150 per acre per spray",
                "application_time": "Early morning or evening",
                "effectiveness": "50-60% deterrent effect on chewing pests",
                "suitable_for": ["All crops"],
                "preparation_time": "24 hours (overnight soaking)"
            },
            {
                "method": "Pheromone Traps",
                "description": "Species-specific male moth traps",
                "materials": ["Pheromone lures (pest-specific)", "Funnel traps"],
                "cost_estimate": "₹800-1200 per acre (8-10 traps)",
                "application_time": "Install at crop susceptible stage, replace lures every 4-6 weeks",
                "effectiveness": "80-90% male moth trapping, reduces next generation by 60-70%",
                "suitable_for": ["Cotton (Pink/American bollworm)", "Tomato (Fruit borer)", "Sugarcane (Borers)"]
            },
            {
                "method": "Castor/Marigold Trap Crop",
                "description": "Attract pests away from main crop",
                "materials": ["Castor or Marigold seeds"],
                "recipe": "Plant 2-4 rows around field or at intervals. Monitor and destroy heavily infested trap plants",
                "cost_estimate": "₹300-500 per acre",
                "application_time": "Plant 1-2 weeks before main crop",
                "effectiveness": "Diverts 40-60% of pest population",
                "suitable_for": ["Cotton", "Tomato", "Chili"]
            }
        ]
    },
    "Tier3_Chemical": {
        "name": "Targeted Chemical (Last Resort)",
        "priority": 3,
        "etl_note": "ALWAYS check Economic Threshold Level (ETL) before spraying. Never spray below threshold.",
        "safety_first": [
            "Wear mask, gloves, full-sleeve shirt, pants during spraying",
            "Never spray against wind direction",
            "Do not eat, drink, or smoke during spraying",
            "Wash hands and clothes immediately after spraying",
            "Store chemicals away from food and children",
            "Follow label instructions exactly - never overdose",
            "Do not spray near water bodies, flowering crops",
            "Maintain pre-harvest interval (PHI) strictly"
        ],
        "farmer_friends": [
            "Ladybird beetles (eat aphids)",
            "Spiders (eat many pests)",
            "Dragonflies (eat mosquitoes, small insects)",
            "Wasps (parasitize pest eggs)",
            "Lacewings (eat aphids, mites)",
            "Ground beetles (eat soil pests)",
            "Bees (pollination - protect at all costs!)"
        ],
        "methods": [
            {
                "pest_type": "Sucking Pests (Aphids, Whiteflies, Thrips)",
                "check_etl": "Count pests per leaf/plant. Spray only if above threshold.",
                "approved_chemicals": [
                    {
                        "name": "Imidacloprid 17.8% SL",
                        "dose": "0.5 ml per liter water",
                        "mode": "Systemic, contact",
                        "phi": "7-14 days",
                        "cost": "₹350-450 per 100ml bottle",
                        "coverage": "100ml covers 1 acre",
                        "safety_rating": "Moderately hazardous - Yellow label"
                    },
                    {
                        "name": "Thiamethoxam 25% WG",
                        "dose": "0.4 g per liter water",
                        "mode": "Systemic",
                        "phi": "14-21 days",
                        "cost": "₹400-500 per 100g pack",
                        "coverage": "100g covers 1 acre",
                        "safety_rating": "Moderately hazardous - Yellow label"
                    },
                    {
                        "name": "Acetamiprid 20% SP",
                        "dose": "0.5 g per liter water",
                        "mode": "Systemic, contact",
                        "phi": "7-14 days",
                        "cost": "₹300-400 per 100g pack",
                        "coverage": "100g covers 1 acre",
                        "safety_rating": "Slightly hazardous - Blue label"
                    }
                ],
                "spray_timing": "Early morning or late evening, no wind",
                "avoid_flowering": "Yes - harmful to bees and pollinators"
            },
            {
                "pest_type": "Chewing Pests (Caterpillars, Borers, Beetles)",
                "check_etl": "Count larvae per plant or % damage. Spray only if above threshold.",
                "approved_chemicals": [
                    {
                        "name": "Chlorantraniliprole 18.5% SC",
                        "dose": "0.4 ml per liter water",
                        "mode": "Systemic, stomach poison",
                        "phi": "1-3 days",
                        "cost": "₹600-800 per 100ml bottle",
                        "coverage": "100ml covers 1 acre",
                        "safety_rating": "Slightly hazardous - Blue label",
                        "note": "Excellent safety to beneficial insects"
                    },
                    {
                        "name": "Emamectin Benzoate 5% SG",
                        "dose": "0.5 g per liter water",
                        "mode": "Stomach poison, contact",
                        "phi": "7-14 days",
                        "cost": "₹400-550 per 100g pack",
                        "coverage": "100g covers 1 acre",
                        "safety_rating": "Moderately hazardous - Yellow label"
                    },
                    {
                        "name": "Spinosad 45% SC",
                        "dose": "0.5 ml per liter water",
                        "mode": "Contact, stomach poison (organic-origin)",
                        "phi": "1-3 days",
                        "cost": "₹800-1000 per 100ml bottle",
                        "coverage": "100ml covers 1 acre",
                        "safety_rating": "Slightly hazardous - Blue label",
                        "note": "Safe for beneficial insects, bees (after spray dries)"
                    }
                ],
                "spray_timing": "Target early instar larvae for best control",
                "avoid_flowering": "Spinosad safe after spray dries, others avoid flowering"
            },
            {
                "pest_type": "Fungal Diseases",
                "check_symptoms": "Spray only when symptoms appear or weather favors disease",
                "approved_chemicals": [
                    {
                        "name": "Mancozeb 75% WP",
                        "dose": "2.5 g per liter water",
                        "mode": "Contact fungicide (preventive)",
                        "phi": "7-14 days",
                        "cost": "₹250-350 per kg",
                        "coverage": "1 kg covers 2 acres",
                        "safety_rating": "Slightly hazardous - Blue label"
                    },
                    {
                        "name": "Carbendazim 50% WP",
                        "dose": "1 g per liter water",
                        "mode": "Systemic fungicide (curative + preventive)",
                        "phi": "7-14 days",
                        "cost": "₹200-300 per kg",
                        "coverage": "1 kg covers 5 acres",
                        "safety_rating": "Slightly hazardous - Blue label"
                    },
                    {
                        "name": "Azoxystrobin 23% SC",
                        "dose": "1 ml per liter water",
                        "mode": "Systemic fungicide",
                        "phi": "3-7 days",
                        "cost": "₹700-900 per 100ml bottle",
                        "coverage": "100ml covers 1 acre",
                        "safety_rating": "Slightly hazardous - Blue label"
                    }
                ],
                "spray_timing": "Preventive spray before disease or at first symptoms",
                "avoid_flowering": "No specific concern for fungicides"
            }
        ]
    }
}

# Banned chemicals under Agriculture Pest Act 2026 (fictional but realistic)
BANNED_CHEMICALS = {
    "highly_toxic": [
        {
            "name": "Monocrotophos",
            "reason": "Extreme toxicity to humans, birds, and beneficial insects",
            "ban_year": 2020,
            "alternative": "Use Chlorantraniliprole or Emamectin Benzoate for caterpillar control"
        },
        {
            "name": "Phorate",
            "reason": "Highly toxic soil insecticide, groundwater contamination",
            "ban_year": 2020,
            "alternative": "Use seed treatment with Imidacloprid or Thiamethoxam"
        },
        {
            "name": "Carbofuran",
            "reason": "Severe human toxicity, bird kills, groundwater contamination",
            "ban_year": 2018,
            "alternative": "Use Fipronil or Chlorantraniliprole"
        },
        {
            "name": "Methyl Parathion",
            "reason": "Extremely toxic to humans and wildlife",
            "ban_year": 2018,
            "alternative": "Use safer organophosphates or neonicotinoids"
        }
    ],
    "soil_health_damaging": [
        {
            "name": "DDT",
            "reason": "Persistent organic pollutant, bioaccumulation, soil degradation",
            "ban_year": 1989,
            "alternative": "Use pyrethroids or neonicotinoids for vector control"
        },
        {
            "name": "Endosulfan",
            "reason": "Severe environmental persistence, aquatic toxicity",
            "ban_year": 2011,
            "alternative": "Use safer insecticides based on pest type"
        }
    ],
    "resistance_concerns": [
        {
            "name": "Excessive Cypermethrin use",
            "reason": "Resistance development in bollworms and whiteflies",
            "restriction": "Use in rotation only, not more than 2 sprays per season",
            "alternative": "Rotate with different mode-of-action insecticides"
        }
    ],
    "restricted_use": [
        {
            "name": "Fipronil",
            "reason": "Highly toxic to bees and aquatic organisms",
            "restriction": "Banned for foliar spray, allowed only for seed treatment",
            "alternative": "For foliar use, choose Chlorantraniliprole or other bee-safe options"
        }
    ]
}

# Weather-disease relationship for predictive alerts
WEATHER_DISEASE_ALERTS = {
    "High_Humidity_High_Temp": {
        "conditions": {"humidity": ">80%", "temperature": "25-35°C"},
        "at_risk_diseases": [
            {"crop": "Paddy (Rice)", "disease": "Blast", "preventive": "Apply Tricyclazole or Carbendazim preventively"},
            {"crop": "Cotton", "disease": "Cotton Leaf Curl Disease", "preventive": "Control whitefly with neem oil or yellow sticky traps"},
            {"crop": "Tomato", "disease": "Early Blight", "preventive": "Apply Mancozeb or neem oil spray"}
        ]
    },
    "High_Humidity_Cool_Temp": {
        "conditions": {"humidity": ">90%", "temperature": "10-20°C"},
        "at_risk_diseases": [
            {"crop": "Potato", "disease": "Late Blight", "preventive": "Apply Mancozeb or Metalaxyl preventively, avoid overhead irrigation"},
            {"crop": "Wheat", "disease": "Yellow Rust", "preventive": "Apply Propiconazole if symptoms appear"},
            {"crop": "Tomato", "disease": "Late Blight", "preventive": "Apply Mancozeb or Cymoxanil immediately"}
        ]
    },
    "Cloudy_High_Humidity": {
        "conditions": {"humidity": ">85%", "cloudy_days": ">3 consecutive"},
        "at_risk_diseases": [
            {"crop": "Paddy (Rice)", "disease": "Sheath Blight", "preventive": "Apply Validamycin or Hexaconazole"},
            {"crop": "Wheat", "disease": "Powdery Mildew", "preventive": "Apply Sulfur or Triadimefon"}
        ]
    },
    "Rain_Expected": {
        "conditions": {"rainfall_forecast": "within 4-6 hours"},
        "recommendation": "DO NOT SPRAY - Rain will wash away chemicals. Wait for at least 3 hours of dry weather after spray."
    }
}

# Nutrient deficiency vs disease/pest symptoms
DEFICIENCY_VS_DISEASE = {
    "Yellowing_Leaves": {
        "Nitrogen_Deficiency": {
            "pattern": "Yellowing from bottom leaves upward, uniform yellowing",
            "other_symptoms": "Stunted growth, pale green to yellow color",
            "confirmation": "Older leaves affected first, no spots or lesions",
            "remedy": "Apply Nitrogen fertilizer (Urea, Ammonium Sulfate) or Nano Urea"
        },
        "Iron_Deficiency": {
            "pattern": "Yellowing of young leaves while veins remain green (interveinal chlorosis)",
            "other_symptoms": "New growth affected first",
            "confirmation": "Veins stay green, leaf tissue yellow",
            "remedy": "Apply Iron Sulfate (Ferrous Sulfate) spray @ 5g/liter or soil application"
        },
        "Disease_Blast": {
            "pattern": "Yellow patches with brown borders, spindle-shaped lesions",
            "other_symptoms": "Spots with grey centers, can affect neck",
            "confirmation": "Lesions with distinct borders, not uniform yellowing",
            "remedy": "Apply fungicide (Tricyclazole, Carbendazim)"
        }
    },
    "Brown_Spots_Leaves": {
        "Potassium_Deficiency": {
            "pattern": "Browning/scorching of leaf edges and tips",
            "other_symptoms": "Weak stems, reduced fruit quality",
            "confirmation": "Marginal browning, no concentric rings",
            "remedy": "Apply Potassium fertilizer (MOP, SOP) or organic potash"
        },
        "Early_Blight": {
            "pattern": "Concentric brown rings (target spot) on leaves",
            "other_symptoms": "Starts on older leaves, gradually moves up",
            "confirmation": "Target-like rings, distinct lesion borders",
            "remedy": "Apply fungicide (Mancozeb, Chlorothalonil)"
        }
    },
    "Purple_Discoloration": {
        "Phosphorus_Deficiency": {
            "pattern": "Purple tinge on leaves, especially undersides and stems",
            "other_symptoms": "Stunted growth, dark green/purple leaves, delayed maturity",
            "confirmation": "Uniform purple color, cold weather or acidic soil",
            "remedy": "Apply Phosphorus fertilizer (DAP, SSP, PROM)"
        }
    }
}

# Safety tips by language (framework for multilingual support)
SAFETY_TIPS = {
    "english": {
        "before_spray": [
            "Check weather - Do not spray if rain expected within 4 hours",
            "Wear protective gear - mask, gloves, full-sleeve shirt, pants",
            "Read chemical label carefully - follow dose instructions exactly",
            "Check if neighbors' fields will be affected by spray drift"
        ],
        "during_spray": [
            "Spray in early morning (6-9 AM) or late evening (4-6 PM)",
            "Never spray in strong wind or during hottest part of day",
            "Do not eat, drink, or smoke while spraying",
            "Keep children and animals away from spraying area",
            "Cover any water sources nearby to prevent contamination"
        ],
        "after_spray": [
            "Wash hands, face, and all body parts exposed to chemicals immediately",
            "Wash clothes separately from family clothes",
            "Clean spray equipment thoroughly",
            "Store remaining chemicals in original container, locked away from food and children",
            "Follow Pre-Harvest Interval (PHI) - do not harvest before specified days"
        ],
        "emergency": [
            "If chemical enters eyes - Wash with clean water for 15 minutes, seek medical help",
            "If swallowed - Do NOT induce vomiting, take chemical label to doctor immediately",
            "If skin contact - Remove contaminated clothes, wash skin with soap and water",
            "Emergency helpline numbers - 1800-425-2958 (Agriculture), 112 (Emergency)"
        ]
    },
    "hindi": {
        "before_spray": [
            "मौसम देखें - बारिश की संभावना हो तो छिड़काव ना करें",
            "सुरक्षा साधन पहनें - मास्क, दस्ताने, पूरी बाजू का कपड़ा",
            "दवा की मात्रा सही रखें - लेबल पर लिखी मात्रा का पालन करें",
            "पड़ोसी के खेत पर असर ना हो, इसका ध्यान रखें"
        ],
        "during_spray": [
            "सुबह (6-9) या शाम (4-6) में ही छिड़काव करें",
            "तेज हवा या दोपहर की गर्मी में छिड़काव ना करें",
            "छिड़काव के दौरान खाना, पीना, धूम्रपान ना करें",
            "बच्चों और पशुओं को दूर रखें",
            "पानी के स्रोत को ढक दें"
        ],
        "after_spray": [
            "छिड़काव के बाद तुरंत हाथ-मुंह धोएं",
            "कपड़े अलग से धोएं",
            "स्प्रेयर को अच्छे से साफ करें",
            "बचे हुए रसायन को बंद डिब्बे में, बच्चों से दूर रखें",
            "फसल को निर्धारित दिनों के बाद ही काटें"
        ],
        "emergency": [
            "आंख में गया तो - 15 मिनट साफ पानी से धोएं, डॉक्टर को दिखाएं",
            "निगल गया तो - उल्टी ना करवाएं, दवा का डिब्बा लेकर तुरंत डॉक्टर के पास जाएं",
            "त्वचा पर लगा तो - कपड़े उतारें, साबुन से धोएं",
            "आपातकालीन नंबर - 1800-425-2958 (कृषि), 112 (आपातकाल)"
        ]
    }
}

def get_pest_disease_info(crop):
    """Get pest and disease information for a specific crop"""
    return CROP_PESTS_DISEASES.get(crop, {"pests": [], "diseases": []})

def get_ipm_recommendations(tier="all"):
    """Get IPM recommendations by tier"""
    if tier == "all":
        return IPM_RECOMMENDATIONS
    return IPM_RECOMMENDATIONS.get(f"Tier{tier}_{tier.replace('1', '_Prevention').replace('2', '_Organic_Mechanical').replace('3', '_Chemical')}", {})

def check_banned_chemical(chemical_name):
    """Check if a chemical is banned and get alternative"""
    for category, chemicals in BANNED_CHEMICALS.items():
        for chem in chemicals:
            if chemical_name.lower() in chem["name"].lower():
                return True, chem
    return False, None

def get_weather_based_alerts(humidity, temperature, rainfall_forecast=False, cloudy_days=0):
    """Get disease alerts based on weather conditions"""
    alerts = []
    
    if rainfall_forecast:
        alerts.append(WEATHER_DISEASE_ALERTS["Rain_Expected"])
        return alerts
    
    if humidity > 90 and 10 <= temperature <= 20:
        alerts.append(WEATHER_DISEASE_ALERTS["High_Humidity_Cool_Temp"])
    elif humidity > 80 and 25 <= temperature <= 35:
        alerts.append(WEATHER_DISEASE_ALERTS["High_Humidity_High_Temp"])
    
    if cloudy_days > 3 and humidity > 85:
        alerts.append(WEATHER_DISEASE_ALERTS["Cloudy_High_Humidity"])
    
    return alerts

def diagnose_symptom(symptom_type, crop=None):
    """Diagnose whether symptoms are from deficiency or disease"""
    return DEFICIENCY_VS_DISEASE.get(symptom_type, {})
