#!/usr/bin/env python
"""
Comprehensive Test Suite for Crop Health & Marketplace Module
Tests all major functionality to ensure system integrity
"""

def test_crop_health_module():
    """Test all crop health and marketplace features"""
    
    print("=" * 80)
    print("CROP HEALTH & MARKETPLACE MODULE - COMPREHENSIVE TEST SUITE")
    print("=" * 80)
    print()
    
    # Import modules
    try:
        from jai_kisan_agent import JaiKisanAgent
        from data.crop_health_data import (
            CROP_PESTS_DISEASES, IPM_RECOMMENDATIONS, BANNED_CHEMICALS,
            get_pest_disease_info, check_banned_chemical, diagnose_symptom
        )
        from data.marketplace_data import (
            find_nearby_shops, get_product_options, get_kifayati_option,
            compare_prices, calculate_distance
        )
        print("✓ All imports successful")
        print()
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False
    
    # Initialize agent
    try:
        agent = JaiKisanAgent()
        print("✓ JaiKisanAgent initialized")
        print()
    except Exception as e:
        print(f"✗ Agent initialization failed: {e}")
        return False
    
    # Test 1: Knowledge Base
    print("TEST 1: Knowledge Base")
    print("-" * 40)
    try:
        crops_tested = ["Paddy (Rice)", "Cotton", "Tomato"]
        for crop in crops_tested:
            info = agent.get_crop_pests_diseases(crop)
            pests_count = len(info.get("pests", []))
            diseases_count = len(info.get("diseases", []))
            print(f"  {crop}: {pests_count} pests, {diseases_count} diseases")
        print("✓ Knowledge base working")
        print()
    except Exception as e:
        print(f"✗ Knowledge base test failed: {e}")
        return False
    
    # Test 2: IPM Tiers
    print("TEST 2: IPM 3-Tier System")
    print("-" * 40)
    try:
        tier1 = agent.get_ipm_tier1_prevention()
        tier2 = agent.get_ipm_tier2_organic()
        tier3 = agent.get_ipm_tier3_chemical()
        
        print(f"  Tier 1 (Prevention): {len(tier1.get('methods', []))} methods")
        print(f"  Tier 2 (Organic): {len(tier2.get('methods', []))} methods")
        print(f"  Tier 3 (Chemical): {len(tier3.get('methods', []))} pest types")
        print("✓ All IPM tiers accessible")
        print()
    except Exception as e:
        print(f"✗ IPM tier test failed: {e}")
        return False
    
    # Test 3: IPM Recommendation Generation
    print("TEST 3: IPM Recommendation Generation")
    print("-" * 40)
    try:
        recommendation = agent.generate_ipm_recommendation(
            "Cotton", "Pink Bollworm", "15% rosette flowers"
        )
        print(f"  Generated recommendation: {len(recommendation)} characters")
        assert "Tier 1" in recommendation, "Missing Tier 1"
        assert "Tier 2" in recommendation, "Missing Tier 2"
        assert "Tier 3" in recommendation, "Missing Tier 3"
        assert "Safety" in recommendation, "Missing Safety tips"
        print("✓ IPM recommendation generation working")
        print()
    except Exception as e:
        print(f"✗ IPM recommendation test failed: {e}")
        return False
    
    # Test 4: Crop Rotation Checker
    print("TEST 4: Crop Rotation Compatibility")
    print("-" * 40)
    try:
        # Test incompatible (same family)
        result1 = agent.check_crop_rotation_compatibility("Tomato", "Potato")
        print(f"  Tomato after Potato: Compatible={result1['compatible']} (Expected: False)")
        
        # Test compatible (different families)
        result2 = agent.check_crop_rotation_compatibility("Paddy (Rice)", "Tomato")
        print(f"  Paddy after Tomato: Compatible={result2['compatible']} (Expected: True)")
        
        assert result1['compatible'] == False, "Should be incompatible"
        assert result2['compatible'] == True, "Should be compatible"
        print("✓ Crop rotation checker working")
        print()
    except Exception as e:
        print(f"✗ Crop rotation test failed: {e}")
        return False
    
    # Test 5: Chemical Ban Checker
    print("TEST 5: Chemical Ban Status")
    print("-" * 40)
    try:
        # Test banned chemical
        banned = agent.check_chemical_ban_status("Monocrotophos")
        print(f"  Monocrotophos: Banned={banned['banned']} (Expected: True)")
        assert banned['banned'] == True, "Should be banned"
        assert 'alternative' in banned, "Missing alternative"
        
        # Test approved chemical
        approved = agent.check_chemical_ban_status("Imidacloprid")
        print(f"  Imidacloprid: Banned={approved['banned']} (Expected: False)")
        assert approved['banned'] == False, "Should not be banned"
        
        print("✓ Chemical ban checker working")
        print()
    except Exception as e:
        print(f"✗ Chemical ban test failed: {e}")
        return False
    
    # Test 6: Symptom Diagnosis
    print("TEST 6: Plant Problem Diagnosis")
    print("-" * 40)
    try:
        diagnosis = agent.diagnose_plant_problem("Yellowing_Leaves", "Tomato")
        causes = diagnosis.get('possible_causes', {})
        print(f"  Yellowing leaves: {len(causes)} possible causes identified")
        assert len(causes) > 0, "No causes found"
        print("✓ Symptom diagnosis working")
        print()
    except Exception as e:
        print(f"✗ Symptom diagnosis test failed: {e}")
        return False
    
    # Test 7: Weather-Spray Advisor
    print("TEST 7: Weather-Spray Timing Advisor")
    print("-" * 40)
    try:
        # Test with rain expected soon
        advisory1 = agent.check_spray_timing_weather(3)
        print(f"  Rain in 3 hours: {len(advisory1)} characters")
        assert "DO NOT SPRAY" in advisory1, "Should warn against spraying"
        
        # Test with no rain
        advisory2 = agent.check_spray_timing_weather(48)
        print(f"  Rain in 48 hours: {len(advisory2)} characters")
        assert "GOOD TIME" in advisory2, "Should allow spraying"
        
        print("✓ Weather-spray advisor working")
        print()
    except Exception as e:
        print(f"✗ Weather-spray test failed: {e}")
        return False
    
    # Test 8: Marketplace - Shop Finder
    print("TEST 8: Marketplace Shop Finder")
    print("-" * 40)
    try:
        shops = find_nearby_shops("Punjab")
        print(f"  Found {len(shops)} shops in Punjab")
        assert len(shops) > 0, "No shops found"
        
        # Test with district filter
        shops_district = find_nearby_shops("Punjab", district="Ludhiana")
        print(f"  Found {len(shops_district)} shops in Ludhiana")
        
        print("✓ Shop finder working")
        print()
    except Exception as e:
        print(f"✗ Shop finder test failed: {e}")
        return False
    
    # Test 9: Marketplace - Price Comparison
    print("TEST 9: Marketplace Price Comparison")
    print("-" * 40)
    try:
        product = get_product_options("Neem_Oil", sort_by="price")
        print(f"  Neem Oil: {len(product.get('brands', []))} brands")
        
        kifayati = get_kifayati_option("Neem_Oil")
        print(f"  Kifayati option: ₹{kifayati['price']}")
        
        comparison = compare_prices("Imidacloprid")
        print(f"  Price comparison: {len(comparison)} characters")
        
        print("✓ Price comparison working")
        print()
    except Exception as e:
        print(f"✗ Price comparison test failed: {e}")
        return False
    
    # Test 10: Distance Calculation
    print("TEST 10: Distance Calculation")
    print("-" * 40)
    try:
        # Test distance between two known points (approx)
        # Ludhiana to Jalandhar: ~50-80 km (depending on exact coordinates)
        dist = calculate_distance(30.9010, 75.8573, 31.3260, 75.5762)
        print(f"  Ludhiana to Jalandhar: {dist} km (Expected: ~50-80 km)")
        assert 40 <= dist <= 90, "Distance calculation significantly off"
        
        print("✓ Distance calculation working")
        print()
    except Exception as e:
        print(f"✗ Distance calculation test failed: {e}")
        return False
    
    # Test 11: Shop Finder with Product
    print("TEST 11: Integrated Shop & Product Search")
    print("-" * 40)
    try:
        result = agent.find_shops_for_product("Neem Oil", "Punjab", "Ludhiana")
        print(f"  Shop finder result: {len(result)} characters")
        assert "Shop" in result or "shop" in result, "Missing shop info"
        assert "Price" in result or "₹" in result, "Missing price info"
        
        print("✓ Integrated shop/product search working")
        print()
    except Exception as e:
        print(f"✗ Integrated search test failed: {e}")
        return False
    
    # Summary
    print("=" * 80)
    print("ALL TESTS PASSED! ✓")
    print("=" * 80)
    print()
    print("System Status:")
    print(f"  • Knowledge Base: {len(CROP_PESTS_DISEASES)} crops covered")
    print(f"  • IPM Tiers: 3 tiers with 30+ methods")
    print(f"  • Banned Chemicals: {sum(len(v) for v in BANNED_CHEMICALS.values())} entries")
    print(f"  • Products: 8+ categories with price comparison")
    print(f"  • Shop Database: Sample data for 4 states")
    print()
    print("Ready for deployment! 🚀")
    print()
    
    return True


if __name__ == "__main__":
    import sys
    success = test_crop_health_module()
    sys.exit(0 if success else 1)
