"""
(J)ai Kisan - Command Line Interface
Interactive tool for farmers to get fertilizer recommendations
"""

import sys
from jai_kisan_agent import JaiKisanAgent


def display_menu(title, options):
    """Display a menu and get user selection"""
    print(f"\n{title}")
    print("-" * len(title))
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = input(f"\nEnter your choice (1-{len(options)}): ")
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nThank you for using (J)ai Kisan!")
            sys.exit(0)


def display_categorized_menu(title, categories):
    """Display a categorized menu"""
    print(f"\n{title}")
    print("=" * len(title))
    
    all_items = []
    for category, items in categories.items():
        print(f"\n{category}:")
        for item in items:
            all_items.append(item)
            print(f"  {len(all_items)}. {item}")
    
    while True:
        try:
            choice = input(f"\nEnter your choice (1-{len(all_items)}): ")
            choice = int(choice)
            if 1 <= choice <= len(all_items):
                return all_items[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(all_items)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nThank you for using (J)ai Kisan!")
            sys.exit(0)


def main():
    """Main CLI interface"""
    print("=" * 80)
    print(" " * 20 + "(J)ai Kisan - जय किसान")
    print(" " * 15 + "Your Digital Village Elder")
    print("=" * 80)
    print("\nWelcome! I am here to help you with fertilizer recommendations")
    print("tailored to your crop, region, and growth stage.")
    print("\nLet's get started!\n")
    
    agent = JaiKisanAgent()
    
    # Get user inputs
    crop = display_categorized_menu("Select Your Crop", agent.get_crop_categories())
    state = display_categorized_menu("Select Your State/Region", agent.get_state_regions())
    growth_stage = display_menu("Select Growth Stage", agent.get_growth_stages())
    
    print("\n" + "=" * 80)
    print("Generating your personalized recommendation...")
    print("=" * 80)
    
    # Generate and display recommendation
    response = agent.generate_response(crop, state, growth_stage)
    print(response)
    
    # Ask if user wants another recommendation
    print("\n" + "=" * 80)
    another = input("Would you like another recommendation? (yes/no): ").lower()
    if another in ['yes', 'y', 'हां', 'ha']:
        main()
    else:
        print("\nThank you for using (J)ai Kisan!")
        print("May your fields prosper! 🌾")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThank you for using (J)ai Kisan!")
        sys.exit(0)
