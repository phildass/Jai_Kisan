"""
Marketplace Data for (J)ai Kisan System
Contains shop/retailer information, pricing data, and inventory management
"""

# Sample agricultural input shops database (can be extended with real API integration)
SAMPLE_SHOPS = {
    "Punjab": [
        {
            "id": "PB001",
            "name": "Punjab Agro Center",
            "type": "Authorized Retailer",
            "address": "Main Market, Ludhiana",
            "district": "Ludhiana",
            "coordinates": {"lat": 30.9010, "lon": 75.8573},
            "phone": "+91-161-2345678",
            "products": ["Seeds", "Fertilizers", "Pesticides", "Bio-fertilizers"],
            "rating": 4.5,
            "verified": True,
            "opening_hours": "8:00 AM - 8:00 PM"
        },
        {
            "id": "PB002",
            "name": "Kisan Sewa Kendra",
            "type": "Cooperative Society",
            "address": "Gill Road, Ludhiana",
            "district": "Ludhiana",
            "coordinates": {"lat": 30.8850, "lon": 75.8520},
            "phone": "+91-161-2456789",
            "products": ["Seeds", "Fertilizers", "Pesticides", "Agricultural tools"],
            "rating": 4.8,
            "verified": True,
            "opening_hours": "7:00 AM - 7:00 PM",
            "special": "Kifayati prices - Co-op member benefits"
        },
        {
            "id": "PB003",
            "name": "Green Fields Agro",
            "type": "Private Dealer",
            "address": "GT Road, Jalandhar",
            "district": "Jalandhar",
            "coordinates": {"lat": 31.3260, "lon": 75.5762},
            "phone": "+91-181-3456789",
            "products": ["Organic products", "Bio-pesticides", "Fertilizers"],
            "rating": 4.2,
            "verified": True,
            "opening_hours": "8:00 AM - 7:00 PM",
            "special": "Organic & eco-friendly options"
        }
    ],
    "Maharashtra": [
        {
            "id": "MH001",
            "name": "Maharashtra Krishi Seva",
            "type": "Cooperative Society",
            "address": "Market Yard, Pune",
            "district": "Pune",
            "coordinates": {"lat": 18.5204, "lon": 73.8567},
            "phone": "+91-20-2345678",
            "products": ["Seeds", "Fertilizers", "Pesticides", "Micro-nutrients"],
            "rating": 4.6,
            "verified": True,
            "opening_hours": "7:00 AM - 8:00 PM"
        },
        {
            "id": "MH002",
            "name": "Nashik Agri Inputs",
            "type": "Authorized Retailer",
            "address": "MIDC Road, Nashik",
            "district": "Nashik",
            "coordinates": {"lat": 19.9975, "lon": 73.7898},
            "phone": "+91-253-3456789",
            "products": ["Seeds", "Drip irrigation", "Fertilizers", "Bio-fertilizers"],
            "rating": 4.4,
            "verified": True,
            "opening_hours": "8:00 AM - 8:00 PM",
            "special": "Drip irrigation specialist"
        }
    ],
    "Karnataka": [
        {
            "id": "KA001",
            "name": "Karnataka Raitha Sangha",
            "type": "Cooperative Society",
            "address": "Bangalore-Mysore Road, Bangalore",
            "district": "Bangalore",
            "coordinates": {"lat": 12.9716, "lon": 77.5946},
            "phone": "+91-80-2345678",
            "products": ["Seeds", "Fertilizers", "Pesticides", "Organic inputs"],
            "rating": 4.7,
            "verified": True,
            "opening_hours": "7:00 AM - 7:00 PM",
            "special": "Kifayati prices for members"
        }
    ],
    "Uttar Pradesh": [
        {
            "id": "UP001",
            "name": "UP Kisan Bazar",
            "type": "Government Store",
            "address": "Civil Lines, Kanpur",
            "district": "Kanpur",
            "coordinates": {"lat": 26.4499, "lon": 80.3319},
            "phone": "+91-512-2345678",
            "products": ["Subsidized seeds", "Fertilizers", "Pesticides"],
            "rating": 4.3,
            "verified": True,
            "opening_hours": "9:00 AM - 6:00 PM",
            "special": "Government subsidized rates"
        }
    ]
}

# Product pricing database (expandable with real-time API integration)
PRODUCT_PRICING = {
    "Neem_Oil": {
        "name": "Neem Oil (Organic Pesticide)",
        "category": "Bio-pesticide",
        "unit": "1 Liter",
        "brands": [
            {"name": "Anand Agro", "price": 450, "availability": "High"},
            {"name": "Dhanuka", "price": 520, "availability": "Medium"},
            {"name": "Local Producer", "price": 380, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "1-1.5 L per acre",
        "suitable_for": ["All crops"],
        "effectiveness": "70-80% control of soft-bodied insects"
    },
    "Yellow_Sticky_Traps": {
        "name": "Yellow Sticky Traps",
        "category": "Mechanical control",
        "unit": "Pack of 20",
        "brands": [
            {"name": "Pest Control India", "price": 200, "availability": "High"},
            {"name": "AgriTech", "price": 250, "availability": "Medium"},
            {"name": "DIY Kit", "price": 150, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "20-25 traps per acre",
        "suitable_for": ["Cotton", "Tomato", "Chili", "Onion"],
        "effectiveness": "60-70% whitefly/aphid reduction"
    },
    "Trichoderma": {
        "name": "Trichoderma viride (Bio-fungicide)",
        "category": "Bio-fungicide",
        "unit": "1 Kg",
        "brands": [
            {"name": "T. Stanes", "price": 350, "availability": "High"},
            {"name": "IFFCO Sagarika", "price": 280, "availability": "High", "label": "Kifayati"},
            {"name": "Biostadt", "price": 400, "availability": "Medium"}
        ],
        "application_rate": "2.5 kg per acre (soil) or 4g per kg seed",
        "suitable_for": ["All crops"],
        "effectiveness": "Prevents soil-borne diseases"
    },
    "Pheromone_Traps": {
        "name": "Pheromone Traps (species-specific)",
        "category": "Mechanical control",
        "unit": "Set of 8 traps + lures",
        "variants": [
            {
                "pest": "Pink Bollworm",
                "brands": [
                    {"name": "Pest Control India", "price": 800, "availability": "High"},
                    {"name": "AgriScience", "price": 950, "availability": "Medium"}
                ]
            },
            {
                "pest": "American Bollworm",
                "brands": [
                    {"name": "Pest Control India", "price": 850, "availability": "High"},
                    {"name": "AgriScience", "price": 1000, "availability": "Medium"}
                ]
            }
        ],
        "application_rate": "8-10 traps per acre",
        "suitable_for": ["Cotton", "Tomato"],
        "effectiveness": "80-90% male trapping"
    },
    "Imidacloprid": {
        "name": "Imidacloprid 17.8% SL",
        "category": "Chemical insecticide",
        "unit": "100 ml",
        "brands": [
            {"name": "Bayer Confidor", "price": 450, "availability": "High"},
            {"name": "Dhanuka Cyclone", "price": 380, "availability": "High", "label": "Kifayati"},
            {"name": "UPL Imida", "price": 350, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "100 ml per acre",
        "target_pests": "Aphids, Whiteflies, Jassids",
        "safety": "Moderately hazardous - Yellow label",
        "phi": "7-14 days"
    },
    "Chlorantraniliprole": {
        "name": "Chlorantraniliprole 18.5% SC",
        "category": "Chemical insecticide",
        "unit": "100 ml",
        "brands": [
            {"name": "FMC Coragen", "price": 750, "availability": "High"},
            {"name": "Syngenta Voliam Flexi", "price": 720, "availability": "Medium"},
            {"name": "Dhanuka Taal", "price": 600, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "100 ml per acre",
        "target_pests": "Caterpillars, Borers, Leaf folders",
        "safety": "Slightly hazardous - Blue label",
        "phi": "1-3 days",
        "note": "Safe to beneficial insects"
    },
    "Mancozeb": {
        "name": "Mancozeb 75% WP",
        "category": "Chemical fungicide",
        "unit": "1 Kg",
        "brands": [
            {"name": "Indofil M-45", "price": 320, "availability": "High"},
            {"name": "UPL Diathane", "price": 280, "availability": "High", "label": "Kifayati"},
            {"name": "Dhanuka Moximate", "price": 290, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "500g per acre (2 sprays)",
        "target_diseases": "Blight, Rust, Anthracnose",
        "safety": "Slightly hazardous - Blue label",
        "phi": "7-14 days"
    },
    "Azoxystrobin": {
        "name": "Azoxystrobin 23% SC",
        "category": "Chemical fungicide",
        "unit": "100 ml",
        "brands": [
            {"name": "Syngenta Amistar", "price": 850, "availability": "High"},
            {"name": "PI Industries Heritage", "price": 750, "availability": "Medium", "label": "Kifayati"},
            {"name": "Dhanuka Azoxy", "price": 700, "availability": "High", "label": "Kifayati"}
        ],
        "application_rate": "100 ml per acre",
        "target_diseases": "Blight, Blast, Rust, Powdery Mildew",
        "safety": "Slightly hazardous - Blue label",
        "phi": "3-7 days"
    }
}

# e-Urvarak / iFMS integration placeholder (for future API integration)
E_URVARAK_API_CONFIG = {
    "base_url": "https://api.ifms.nic.in/v1/",
    "endpoints": {
        "shop_locator": "shops/nearby",
        "stock_check": "inventory/check",
        "price_compare": "prices/compare"
    },
    "auth_required": True,
    "note": "Requires government API key - apply at https://ifms.nic.in/developer"
}

# Weather API integration placeholder
WEATHER_API_CONFIG = {
    "provider": "IMD",  # India Meteorological Department
    "base_url": "https://api.imd.gov.in/v1/",
    "endpoints": {
        "current": "weather/current",
        "forecast": "weather/forecast",
        "alerts": "weather/alerts"
    },
    "fallback_provider": "OpenWeatherMap",
    "fallback_url": "https://api.openweathermap.org/data/2.5/",
    "note": "Requires API key - use environment variable WEATHER_API_KEY"
}

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two coordinates using Haversine formula
    Returns distance in kilometers
    """
    from math import radians, sin, cos, sqrt, atan2
    
    R = 6371  # Earth's radius in kilometers
    
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    return round(distance, 2)

def find_nearby_shops(state, district=None, user_lat=None, user_lon=None, max_distance=50):
    """
    Find shops in a state/district or within distance from user location
    
    Args:
        state: State name
        district: District name (optional)
        user_lat: User latitude (optional)
        user_lon: User longitude (optional)
        max_distance: Maximum distance in km (default 50km)
    
    Returns:
        List of shops sorted by distance if coordinates provided, else all shops
    """
    shops = SAMPLE_SHOPS.get(state, [])
    
    if district:
        shops = [s for s in shops if s["district"] == district]
    
    if user_lat and user_lon:
        # Calculate distances and filter
        shops_with_distance = []
        for shop in shops:
            dist = calculate_distance(
                user_lat, user_lon,
                shop["coordinates"]["lat"],
                shop["coordinates"]["lon"]
            )
            if dist <= max_distance:
                shop_copy = shop.copy()
                shop_copy["distance_km"] = dist
                shops_with_distance.append(shop_copy)
        
        # Sort by distance
        shops_with_distance.sort(key=lambda x: x["distance_km"])
        return shops_with_distance
    
    return shops

def get_product_options(product_key, sort_by="price"):
    """
    Get product options with pricing from multiple sources
    
    Args:
        product_key: Product identifier (e.g., "Neem_Oil")
        sort_by: Sort by "price" or "availability"
    
    Returns:
        Product information with sorted brand options
    """
    product = PRODUCT_PRICING.get(product_key, None)
    
    if not product:
        return None
    
    product_copy = product.copy()
    
    if "brands" in product_copy:
        brands = product_copy["brands"].copy()
        if sort_by == "price":
            brands.sort(key=lambda x: x["price"])
        elif sort_by == "availability":
            availability_order = {"High": 0, "Medium": 1, "Low": 2}
            brands.sort(key=lambda x: availability_order.get(x["availability"], 3))
        
        product_copy["brands"] = brands
    
    return product_copy

def get_kifayati_option(product_key):
    """
    Get the most economical (Kifayati) option for a product
    
    Args:
        product_key: Product identifier
    
    Returns:
        Lowest priced option or one marked as "Kifayati"
    """
    product = PRODUCT_PRICING.get(product_key, None)
    
    if not product or "brands" not in product:
        return None
    
    # First, check for explicitly labeled Kifayati options
    kifayati_options = [b for b in product["brands"] if b.get("label") == "Kifayati"]
    if kifayati_options:
        # Return the cheapest among Kifayati options
        return min(kifayati_options, key=lambda x: x["price"])
    
    # Otherwise, return the cheapest overall
    return min(product["brands"], key=lambda x: x["price"])

def compare_prices(product_key, include_description=True):
    """
    Compare prices across brands for a product
    
    Args:
        product_key: Product identifier
        include_description: Include product description
    
    Returns:
        Formatted price comparison
    """
    product = get_product_options(product_key, sort_by="price")
    
    if not product:
        return "Product not found"
    
    comparison = []
    
    if include_description:
        comparison.append(f"**{product['name']}**")
        comparison.append(f"Category: {product['category']}")
        comparison.append(f"Unit: {product['unit']}")
        comparison.append("")
    
    comparison.append("**Price Comparison:**")
    
    if "brands" in product:
        for idx, brand in enumerate(product["brands"], 1):
            label = f" ({brand['label']})" if "label" in brand else ""
            availability = brand.get("availability", "Unknown")
            comparison.append(
                f"{idx}. {brand['name']}{label}: ₹{brand['price']} - {availability} availability"
            )
    elif "variants" in product:
        for variant in product["variants"]:
            comparison.append(f"\n**For {variant['pest']}:**")
            for idx, brand in enumerate(variant["brands"], 1):
                comparison.append(
                    f"{idx}. {brand['name']}: ₹{brand['price']} - {brand['availability']} availability"
                )
    
    return "\n".join(comparison)

def get_shop_contact_info(shop_id):
    """
    Get contact information for a shop
    
    Args:
        shop_id: Shop identifier
    
    Returns:
        Shop contact information including phone and address
    """
    for state, shops in SAMPLE_SHOPS.items():
        for shop in shops:
            if shop["id"] == shop_id:
                return {
                    "name": shop["name"],
                    "phone": shop["phone"],
                    "address": shop["address"],
                    "type": shop["type"],
                    "opening_hours": shop.get("opening_hours", "Not specified"),
                    "special": shop.get("special", None)
                }
    
    return None

def format_shop_list(shops, include_distance=True):
    """
    Format shop list for display
    
    Args:
        shops: List of shop dictionaries
        include_distance: Whether to include distance (if available)
    
    Returns:
        Formatted shop list string
    """
    if not shops:
        return "No shops found in this area. Please contact your district agriculture office for nearest retailers."
    
    output = []
    
    for idx, shop in enumerate(shops, 1):
        distance_str = f" ({shop['distance_km']} km away)" if "distance_km" in shop and include_distance else ""
        special_str = f"\n   Special: {shop['special']}" if "special" in shop else ""
        
        output.append(
            f"{idx}. **{shop['name']}**{distance_str}\n"
            f"   Type: {shop['type']}\n"
            f"   Address: {shop['address']}\n"
            f"   Phone: {shop['phone']} *(Click to call)*\n"
            f"   Hours: {shop.get('opening_hours', 'Not specified')}\n"
            f"   Rating: {'⭐' * int(shop.get('rating', 0))} ({shop.get('rating', 'N/A')})"
            f"{special_str}"
        )
    
    return "\n\n".join(output)
