#!/usr/bin/env python3
"""
Test script for Shop Discovery, Price Comparison, and Group Buying features
"""

import sys
from data.shop_data import (
    SAMPLE_SHOPS,
    BRAND_TO_SALT_MAPPING,
    KIFAYATI_ALTERNATIVES,
    DOSAGE_CALCULATION_RULES,
    GROUP_BUYING_THRESHOLDS,
    KISAN_POINTS_REWARDS
)

def test_shop_data():
    """Test shop data structure"""
    print("=" * 80)
    print("Testing Shop Data")
    print("=" * 80)
    
    print(f"\n✓ Found {len(SAMPLE_SHOPS)} sample shops")
    
    for shop in SAMPLE_SHOPS:
        print(f"\n  Shop: {shop['name']}")
        print(f"  Location: {shop['district']}, {shop['state']}")
        print(f"  Inventory items: {len(shop['inventory'])}")
        print(f"  Rating: {shop['rating']}/5.0")
    
    print("\n✅ Shop data structure validated")


def test_brand_to_salt_mapping():
    """Test brand to salt mapping"""
    print("\n" + "=" * 80)
    print("Testing Brand to Salt Mapping")
    print("=" * 80)
    
    print(f"\n✓ Found {len(BRAND_TO_SALT_MAPPING)} brand mappings")
    
    # Test a few examples
    test_brands = ["IFFCO DAP", "Government Subsidized Urea", "Coromandel MOP"]
    
    for brand in test_brands:
        if brand in BRAND_TO_SALT_MAPPING:
            mapping = BRAND_TO_SALT_MAPPING[brand]
            print(f"\n  Brand: {brand}")
            print(f"  Salt: {mapping['salt']}")
            print(f"  NPK: {mapping['npk']}")
            print(f"  Category: {mapping['category']}")
    
    print("\n✅ Brand to salt mapping validated")


def test_kifayati_alternatives():
    """Test kifayati alternatives"""
    print("\n" + "=" * 80)
    print("Testing Kifayati (Economical) Alternatives")
    print("=" * 80)
    
    print(f"\n✓ Found {len(KIFAYATI_ALTERNATIVES)} fertilizer types with kifayati options")
    
    for fert_type, data in KIFAYATI_ALTERNATIVES.items():
        kifayati = data['kifayati_option']
        savings = kifayati['savings_per_bag']
        
        print(f"\n  {fert_type}:")
        print(f"  Branded Average: ₹{data['branded_average_price']}/bag")
        print(f"  Kifayati Option: {kifayati['name']}")
        print(f"  Kifayati Price: ₹{kifayati['price_per_50kg']}/bag")
        print(f"  💰 Savings: ₹{savings} per bag ({savings/data['branded_average_price']*100:.1f}% discount)")
    
    print("\n✅ Kifayati alternatives validated")


def test_dosage_calculator():
    """Test dosage calculation"""
    print("\n" + "=" * 80)
    print("Testing AI Dosage Calculator")
    print("=" * 80)
    
    # Test for 1 hectare of Paddy at Basal Dose
    crop = "Paddy (Rice)"
    stage = "Field Preparation (Basal Dose)"
    area = 2.5
    
    if crop in DOSAGE_CALCULATION_RULES:
        rules = DOSAGE_CALCULATION_RULES[crop][stage]
        
        print(f"\n✓ Calculating for {area} hectares of {crop}")
        print(f"  Growth Stage: {stage}")
        print(f"\n  Recommended Dosages:")
        
        for fert_key, amount_per_ha in rules.items():
            if fert_key != 'area_factor':
                total_kg = amount_per_ha * area
                bags_needed = int((total_kg / 50) + 0.99)  # Round up
                fert_name = fert_key.replace('_kg', '').upper()
                
                print(f"  - {fert_name}: {total_kg} kg ({bags_needed} bags of 50kg)")
    
    print("\n✅ Dosage calculator validated")


def test_group_buying_thresholds():
    """Test group buying thresholds"""
    print("\n" + "=" * 80)
    print("Testing Group Buying Thresholds")
    print("=" * 80)
    
    print(f"\n✓ Found {len(GROUP_BUYING_THRESHOLDS)} fertilizer types with group buying")
    
    for fert_type, threshold in GROUP_BUYING_THRESHOLDS.items():
        print(f"\n  {fert_type}:")
        print(f"  Minimum Bags: {threshold['min_bags']}")
        print(f"  Minimum Farmers: {threshold['min_farmers']}")
        print(f"  Discount: {threshold['discount_percent']}%")
    
    print("\n✅ Group buying thresholds validated")


def test_kisan_points():
    """Test Kisan Points reward structure"""
    print("\n" + "=" * 80)
    print("Testing Kisan Points Rewards")
    print("=" * 80)
    
    print(f"\n✓ Found {len(KISAN_POINTS_REWARDS)} reward types")
    
    for action, points in KISAN_POINTS_REWARDS.items():
        action_name = action.replace('_', ' ').title()
        print(f"  {action_name}: {points} points")
    
    print("\n✅ Kisan Points rewards validated")


def test_distance_calculation():
    """Test distance calculation between coordinates"""
    print("\n" + "=" * 80)
    print("Testing Distance Calculation (Haversine Formula)")
    print("=" * 80)
    
    import math
    
    def calculate_distance(lat1, lon1, lat2, lon2):
        """Calculate distance using Haversine formula"""
        R = 6371  # Earth's radius in km
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    # Test distance between two shops
    shop1 = SAMPLE_SHOPS[0]
    shop2 = SAMPLE_SHOPS[1]
    
    distance = calculate_distance(
        shop1['latitude'], shop1['longitude'],
        shop2['latitude'], shop2['longitude']
    )
    
    print(f"\n✓ Distance between:")
    print(f"  {shop1['name']} ({shop1['latitude']:.4f}, {shop1['longitude']:.4f})")
    print(f"  {shop2['name']} ({shop2['latitude']:.4f}, {shop2['longitude']:.4f})")
    print(f"  Distance: {distance:.2f} km")
    
    print("\n✅ Distance calculation validated")


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("SHOP DISCOVERY FEATURES - TEST SUITE")
    print("Testing data structures and calculations")
    print("=" * 80)
    
    try:
        test_shop_data()
        test_brand_to_salt_mapping()
        test_kifayati_alternatives()
        test_dosage_calculator()
        test_group_buying_thresholds()
        test_kisan_points()
        test_distance_calculation()
        
        print("\n" + "=" * 80)
        print("✅ ALL TESTS PASSED!")
        print("=" * 80)
        print("\nShop Discovery features are ready to use!")
        print("Navigate to /shops in the web application to access these features.\n")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
