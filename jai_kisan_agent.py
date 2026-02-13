"""
(J)ai Kisan - Intelligent Agricultural Consultant for Indian Farmers
Core AI Agent Implementation
"""

from data.crops_data import CROP_CATEGORIES, CROP_NPK_REQUIREMENTS, DEFAULT_NPK
from data.states_data import STATE_REGIONS, STATE_SOIL_INFO, CROPPING_SEASONS
from data.fertilizer_data import (
    FERTILIZER_TYPES, BRANDED_FERTILIZERS, ECO_ALTERNATIVES,
    GROWTH_STAGE_FERTILIZERS
)


class JaiKisanAgent:
    """
    (J)ai Kisan AI Agent - Digital Village Elder
    
    A wise, tech-savvy agricultural consultant committed to farmer prosperity
    and environmental stewardship.
    """
    
    def __init__(self):
        self.persona = "Digital Village Elder"
        self.greeting = "नमस्ते! (Namaste!)"
        
    def get_crop_categories(self):
        """Returns all crop categories and their crops"""
        return CROP_CATEGORIES
    
    def get_all_crops(self):
        """Returns a flat list of all crops"""
        all_crops = []
        for crops in CROP_CATEGORIES.values():
            all_crops.extend(crops)
        return all_crops
    
    def get_state_regions(self):
        """Returns all states organized by region"""
        return STATE_REGIONS
    
    def get_all_states(self):
        """Returns a flat list of all states"""
        all_states = []
        for states in STATE_REGIONS.values():
            all_states.extend(states)
        return all_states
    
    def get_growth_stages(self):
        """Returns all growth stages"""
        return [
            "Field Preparation (Basal Dose)",
            "Sowing/Early Growth",
            "Vegetative Phase (Leaves/Stem growth)",
            "Flowering & Fruiting",
            "Pre-Harvest"
        ]
    
    def get_npk_requirement(self, crop, growth_stage):
        """
        Get NPK requirement for a specific crop and growth stage
        
        Args:
            crop: Name of the crop
            growth_stage: Current growth stage
            
        Returns:
            Dictionary with N, P, K requirements in kg/hectare
        """
        if crop in CROP_NPK_REQUIREMENTS:
            if growth_stage in CROP_NPK_REQUIREMENTS[crop]:
                return CROP_NPK_REQUIREMENTS[crop][growth_stage]
        
        # Fallback to default NPK if available
        if crop in DEFAULT_NPK:
            total = DEFAULT_NPK[crop]
            # Distribute based on growth stage
            if "Basal" in growth_stage:
                return {"N": total["N"] * 0.3, "P": total["P"] * 0.6, "K": total["K"] * 0.4}
            elif "Vegetative" in growth_stage:
                return {"N": total["N"] * 0.4, "P": total["P"] * 0.2, "K": total["K"] * 0.3}
            elif "Flowering" in growth_stage:
                return {"N": total["N"] * 0.2, "P": total["P"] * 0.2, "K": total["K"] * 0.3}
        
        return None
    
    def get_state_info(self, state):
        """
        Get soil and climatic information for a state
        
        Args:
            state: Name of the state
            
        Returns:
            Dictionary with soil pH, type, common issues, and agro-climatic zone
        """
        return STATE_SOIL_INFO.get(state, None)
    
    def get_fertilizer_recommendations(self, crop, state, growth_stage):
        """
        Generate comprehensive fertilizer recommendations
        
        Args:
            crop: Name of the crop
            state: Name of the state
            growth_stage: Current growth stage
            
        Returns:
            Dictionary with recommendations including NPK needs, fertilizer options,
            prices, and eco-friendly alternatives
        """
        npk_needs = self.get_npk_requirement(crop, growth_stage)
        state_info = self.get_state_info(state)
        stage_fertilizers = GROWTH_STAGE_FERTILIZERS.get(growth_stage, {})
        
        recommendation = {
            "crop": crop,
            "state": state,
            "growth_stage": growth_stage,
            "npk_requirement": npk_needs,
            "state_info": state_info,
            "recommended_fertilizers": stage_fertilizers,
            "eco_alternatives": self._get_relevant_eco_alternatives(growth_stage),
            "price_comparison": self._get_price_comparison(stage_fertilizers.get("primary", []))
        }
        
        return recommendation
    
    def _get_relevant_eco_alternatives(self, growth_stage):
        """Get eco-friendly alternatives relevant to growth stage"""
        stage_info = GROWTH_STAGE_FERTILIZERS.get(growth_stage, {})
        eco_names = stage_info.get("eco_alternative", [])
        
        eco_options = {}
        for name in eco_names:
            for eco_name, eco_data in ECO_ALTERNATIVES.items():
                if name.lower() in eco_name.lower():
                    eco_options[eco_name] = eco_data
        
        # Always include some core alternatives
        if "Vermicompost" not in eco_options:
            eco_options["Vermicompost"] = ECO_ALTERNATIVES["Vermicompost"]
        if "Nano Urea" not in eco_options and "Vegetative" in growth_stage:
            eco_options["Nano Urea"] = ECO_ALTERNATIVES["Nano Urea"]
            
        return eco_options
    
    def _get_price_comparison(self, fertilizer_types):
        """Generate price comparison table for fertilizers"""
        comparison = []
        
        for fert_type in fertilizer_types:
            if fert_type in BRANDED_FERTILIZERS:
                comparison.extend(BRANDED_FERTILIZERS[fert_type])
        
        return comparison
    
    def generate_response(self, crop, state, growth_stage, query=None):
        """
        Generate a complete (J)ai Kisan response
        
        Args:
            crop: Selected crop
            state: Selected state
            growth_stage: Selected growth stage
            query: Optional natural language query
            
        Returns:
            Formatted response string
        """
        recommendation = self.get_fertilizer_recommendations(crop, state, growth_stage)
        
        response = f"{self.greeting}\n\n"
        response += f"## Fertilizer Recommendation for {crop} in {state}\n"
        response += f"**Growth Stage:** {growth_stage}\n\n"
        
        # NPK Requirements
        if recommendation["npk_requirement"]:
            npk = recommendation["npk_requirement"]
            response += "### 1. Nutrient Requirements (per hectare)\n"
            response += f"- **Nitrogen (N):** {npk['N']} kg\n"
            response += f"- **Phosphorus (P):** {npk['P']} kg\n"
            response += f"- **Potassium (K):** {npk['K']} kg\n\n"
        
        # State Information
        if recommendation["state_info"]:
            info = recommendation["state_info"]
            response += "### 2. Soil Information for Your Region\n"
            response += f"- **Soil Type:** {info['soil_type']}\n"
            response += f"- **Typical pH:** {info['typical_ph']}\n"
            response += f"- **Common Issue:** {info['common_issue']}\n"
            response += f"- **Agro-climatic Zone:** {info['agro_climatic_zone']}\n\n"
        
        # Price Comparison
        if recommendation["price_comparison"]:
            response += "### 3. Price Comparison (Per 50kg Bag)\n\n"
            response += "| Option | Nutrient Value | Approx. Price (₹) | Availability |\n"
            response += "|--------|----------------|-------------------|---------------|\n"
            
            for item in recommendation["price_comparison"]:
                response += f"| {item['brand']} | {item['npk']} | ₹{item['price_per_50kg']} | {item['availability']} |\n"
            response += "\n"
        
        # Eco-Smart Alternatives
        if recommendation["eco_alternatives"]:
            response += "### 4. Eco-Smart Alternatives (Bhoomi Raksha)\n\n"
            response += "**Environmental Stewardship:** We recommend green alternatives first!\n\n"
            
            for name, data in recommendation["eco_alternatives"].items():
                response += f"**{name}**\n"
                if "price_per_50kg" in data:
                    response += f"- Price: ₹{data['price_per_50kg']} per 50kg\n"
                elif "price_per_bottle" in data:
                    response += f"- Price: ₹{data['price_per_bottle']} per bottle\n"
                elif "price_per_ton" in data:
                    response += f"- Price: ₹{data['price_per_ton']} per ton\n"
                elif "cost" in data:
                    response += f"- Cost: {data['cost']}\n"
                    
                if "benefits" in data:
                    response += "- Benefits:\n"
                    for benefit in data["benefits"]:
                        response += f"  - {benefit}\n"
                response += "\n"
        
        # Timing advice
        timing = recommendation["recommended_fertilizers"].get("timing", "")
        if timing:
            response += f"### 5. Application Timing\n"
            response += f"⏰ **Best Time:** {timing}\n\n"
        
        # Sustainability tip
        response += "### 6. Pro-Tip for Long-term Soil Health\n"
        response += "- Always get your **Soil Health Card** to prevent over-fertilization\n"
        response += "- Mix chemical fertilizers with organic manure for better Nitrogen Use Efficiency (NUE)\n"
        response += "- This reduces groundwater contamination and saves costs in the long run\n\n"
        
        # Weather advisory placeholder
        response += "### 7. Weather Advisory\n"
        response += "⚠️ *Check local weather forecast before applying fertilizer*\n"
        response += "- Avoid application if heavy rain is expected within 48 hours\n"
        response += "- This prevents nutrient runoff and wastage\n\n"
        
        response += "---\n"
        response += "*Would you like me to help you find the nearest government fertilizer center (Kendra)?*\n"
        
        return response
    
    def get_system_prompt(self):
        """Returns the complete system prompt for AI integration"""
        with open('system_prompt.md', 'r', encoding='utf-8') as f:
            return f.read()


def main():
    """Example usage of (J)ai Kisan Agent"""
    agent = JaiKisanAgent()
    
    # Example 1: Paddy in Punjab
    print("=" * 80)
    print("Example 1: Paddy farmer in Punjab - Vegetative Phase")
    print("=" * 80)
    response = agent.generate_response(
        crop="Paddy (Rice)",
        state="Punjab",
        growth_stage="Vegetative Phase (Leaves/Stem growth)"
    )
    print(response)
    
    print("\n" + "=" * 80)
    print("Example 2: Cotton farmer in Maharashtra - Field Preparation")
    print("=" * 80)
    response = agent.generate_response(
        crop="Cotton",
        state="Maharashtra",
        growth_stage="Field Preparation (Basal Dose)"
    )
    print(response)


if __name__ == "__main__":
    main()
