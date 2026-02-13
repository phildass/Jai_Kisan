#!/usr/bin/env python3
"""
Quick Test Script for (J)ai Kisan
Demonstrates key functionality without requiring user input
"""

from jai_kisan_agent import JaiKisanAgent


def test_basic_functionality():
    """Test basic agent functionality"""
    print("=" * 80)
    print("Testing (J)ai Kisan Agent - Basic Functionality")
    print("=" * 80)
    
    agent = JaiKisanAgent()
    
    # Test 1: Get crop categories
    print("\n1. Testing crop categories...")
    categories = agent.get_crop_categories()
    print(f"   ✓ Found {len(categories)} crop categories")
    total_crops = sum(len(crops) for crops in categories.values())
    print(f"   ✓ Total {total_crops} crops supported")
    
    # Test 2: Get state regions
    print("\n2. Testing state/region data...")
    regions = agent.get_state_regions()
    print(f"   ✓ Found {len(regions)} regions")
    total_states = sum(len(states) for states in regions.values())
    print(f"   ✓ Total {total_states} states covered")
    
    # Test 3: Get growth stages
    print("\n3. Testing growth stages...")
    stages = agent.get_growth_stages()
    print(f"   ✓ {len(stages)} growth stages defined")
    
    # Test 4: Get NPK requirements
    print("\n4. Testing NPK requirements...")
    npk = agent.get_npk_requirement("Paddy (Rice)", "Vegetative Phase (Leaves/Stem growth)")
    print(f"   ✓ Paddy NPK (Vegetative): N={npk['N']}, P={npk['P']}, K={npk['K']} kg/ha")
    
    # Test 5: Get state info
    print("\n5. Testing state information...")
    info = agent.get_state_info("Punjab")
    print(f"   ✓ Punjab soil type: {info['soil_type']}")
    print(f"   ✓ Punjab pH range: {info['typical_ph']}")
    
    # Test 6: Generate complete recommendation
    print("\n6. Testing complete recommendation generation...")
    recommendation = agent.get_fertilizer_recommendations(
        crop="Wheat",
        state="Uttar Pradesh",
        growth_stage="Field Preparation (Basal Dose)"
    )
    print(f"   ✓ NPK requirement calculated: {recommendation['npk_requirement']}")
    print(f"   ✓ {len(recommendation['eco_alternatives'])} eco alternatives found")
    print(f"   ✓ {len(recommendation['price_comparison'])} price options available")
    
    print("\n" + "=" * 80)
    print("All tests passed! ✓")
    print("=" * 80)


def demo_scenarios():
    """Demonstrate key scenarios"""
    print("\n\n" + "=" * 80)
    print("DEMO SCENARIOS")
    print("=" * 80)
    
    agent = JaiKisanAgent()
    
    scenarios = [
        {
            "title": "Scenario 1: Paddy farmer in Punjab (Vegetative Phase)",
            "crop": "Paddy (Rice)",
            "state": "Punjab",
            "stage": "Vegetative Phase (Leaves/Stem growth)"
        },
        {
            "title": "Scenario 2: Cotton farmer in Maharashtra (Field Prep)",
            "crop": "Cotton",
            "state": "Maharashtra",
            "stage": "Field Preparation (Basal Dose)"
        },
        {
            "title": "Scenario 3: Wheat farmer in Uttar Pradesh (Sowing)",
            "crop": "Wheat",
            "state": "Uttar Pradesh",
            "stage": "Sowing/Early Growth"
        }
    ]
    
    for scenario in scenarios:
        print("\n" + "-" * 80)
        print(scenario["title"])
        print("-" * 80)
        
        response = agent.generate_response(
            crop=scenario["crop"],
            state=scenario["state"],
            growth_stage=scenario["stage"]
        )
        
        # Print first 500 characters of response
        print(response[:600] + "\n[... truncated for demo ...]\n")


def main():
    """Run all tests and demos"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "(J)ai Kisan - Test Suite" + " " * 34 + "║")
    print("║" + " " * 15 + "Digital Village Elder for Indian Farmers" + " " * 22 + "║")
    print("╚" + "═" * 78 + "╝")
    
    test_basic_functionality()
    demo_scenarios()
    
    print("\n" + "=" * 80)
    print("Test suite completed successfully!")
    print("Try running 'python cli.py' for interactive mode")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
