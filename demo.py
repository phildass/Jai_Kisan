#!/usr/bin/env python3
"""
Demo Output Generator for (J)ai Kisan
Generates sample outputs for documentation and demonstration
"""

from jai_kisan_agent import JaiKisanAgent


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80 + "\n")


def demo_1_basic_usage():
    """Demo 1: Basic usage example"""
    print_header("DEMO 1: Basic Fertilizer Recommendation")
    
    agent = JaiKisanAgent()
    
    print("User Input:")
    print("  Crop: Paddy (Rice)")
    print("  State: Punjab")
    print("  Growth Stage: Vegetative Phase (Leaves/Stem growth)")
    print("\n" + "-" * 80)
    
    response = agent.generate_response(
        crop="Paddy (Rice)",
        state="Punjab",
        growth_stage="Vegetative Phase (Leaves/Stem growth)"
    )
    
    print(response)


def demo_2_price_comparison():
    """Demo 2: Focus on price comparison"""
    print_header("DEMO 2: DAP Price Comparison (Maharashtra Cotton Farmer)")
    
    from data.fertilizer_data import BRANDED_FERTILIZERS, ECO_ALTERNATIVES
    
    print("Problem: DAP prices have increased significantly")
    print("\nPrice Comparison Table:\n")
    
    print("| Brand/Option | NPK | Price (₹/50kg) | Savings |")
    print("|--------------|-----|----------------|---------|")
    
    for item in BRANDED_FERTILIZERS['DAP']:
        savings = ""
        if "Generic" in item['brand'] or "Co-op" in item['brand']:
            base_price = 1350
            savings = f"Save ₹{base_price - item['price_per_50kg']}"
        print(f"| {item['brand']:<20} | {item['npk']} | ₹{item['price_per_50kg']:>6} | {savings:<15} |")
    
    print("\nEco-Smart Alternative:")
    print("  Instead of 2 bags DAP (₹2,700):")
    print("  → Use 1 bag DAP (₹1,350) + 2 bags PROM (₹600)")
    print("  → Total: ₹1,950")
    print("  → Savings: ₹750 (28% cost reduction)")
    print("  → Bonus: Improved soil health!")


def demo_3_season_plan():
    """Demo 3: Complete season fertilizer plan"""
    print_header("DEMO 3: Complete Season Fertilizer Plan for Wheat (UP)")
    
    agent = JaiKisanAgent()
    
    crop = "Wheat"
    state = "Uttar Pradesh"
    
    print(f"Crop: {crop}")
    print(f"Location: {state}\n")
    print("-" * 80)
    
    stages = agent.get_growth_stages()
    total_n, total_p, total_k = 0, 0, 0
    
    print("\n| Growth Stage | N (kg/ha) | P (kg/ha) | K (kg/ha) | Timing |")
    print("|--------------|-----------|-----------|-----------|---------|")
    
    for stage in stages:
        npk = agent.get_npk_requirement(crop, stage)
        if npk:
            from data.fertilizer_data import GROWTH_STAGE_FERTILIZERS
            timing = GROWTH_STAGE_FERTILIZERS.get(stage, {}).get("timing", "As needed")
            
            print(f"| {stage[:30]:<30} | {npk['N']:>6} | {npk['P']:>6} | {npk['K']:>6} | {timing[:30]:<30} |")
            
            total_n += npk['N']
            total_p += npk['P']
            total_k += npk['K']
    
    print(f"| {'TOTAL SEASON':<30} | {total_n:>6} | {total_p:>6} | {total_k:>6} | {'':<30} |")
    print("-" * 80)
    
    print(f"\nTotal Season Requirements:")
    print(f"  • Nitrogen (N): {total_n} kg/hectare")
    print(f"  • Phosphorus (P): {total_p} kg/hectare")
    print(f"  • Potassium (K): {total_k} kg/hectare")


def demo_4_eco_alternatives():
    """Demo 4: Eco-friendly alternatives showcase"""
    print_header("DEMO 4: Eco-Friendly Alternatives (Bhoomi Raksha)")
    
    from data.fertilizer_data import ECO_ALTERNATIVES
    
    print("Environmental Stewardship - Green Alternatives First!\n")
    
    for i, (name, data) in enumerate(ECO_ALTERNATIVES.items(), 1):
        print(f"{i}. {name}")
        print(f"   Type: {data['type']}")
        
        # Price
        if 'price_per_50kg' in data:
            print(f"   Price: ₹{data['price_per_50kg']} per 50kg")
        elif 'price_per_bottle' in data:
            print(f"   Price: ₹{data['price_per_bottle']} per bottle")
        elif 'price_per_ton' in data:
            print(f"   Price: ₹{data['price_per_ton']} per ton")
        elif 'cost' in data:
            print(f"   Cost: {data['cost']}")
        
        # Top benefits
        if 'benefits' in data and len(data['benefits']) > 0:
            print(f"   Key Benefit: {data['benefits'][0]}")
        
        print()


def demo_5_state_comparison():
    """Demo 5: State soil comparison"""
    print_header("DEMO 5: State Soil Characteristics Comparison")
    
    agent = JaiKisanAgent()
    
    states = ["Punjab", "Maharashtra", "West Bengal", "Karnataka", "Bihar"]
    
    print("| State | Soil Type | pH Range | Common Issue |")
    print("|-------|-----------|----------|--------------|")
    
    for state in states:
        info = agent.get_state_info(state)
        if info:
            print(f"| {state:<15} | {info['soil_type'][:25]:<25} | {info['typical_ph']:<10} | {info['common_issue'][:30]:<30} |")


def main():
    """Run all demos"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 25 + "(J)ai Kisan" + " " * 42 + "║")
    print("║" + " " * 19 + "Demonstration Output" + " " * 39 + "║")
    print("║" + " " * 15 + "Digital Village Elder for Farmers" + " " * 30 + "║")
    print("╚" + "═" * 78 + "╝")
    
    demo_1_basic_usage()
    demo_2_price_comparison()
    demo_3_season_plan()
    demo_4_eco_alternatives()
    demo_5_state_comparison()
    
    print("\n" + "=" * 80)
    print("End of Demonstration".center(80))
    print("=" * 80)
    print("\nTo try it yourself:")
    print("  • Run 'python cli.py' for interactive mode")
    print("  • Run 'python test_suite.py' for automated tests")
    print("  • See DOCUMENTATION.md for full guide")
    print("\n" + "जय किसान! (Victory to the Farmers!) 🌾\n")


if __name__ == "__main__":
    main()
