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
from data.crop_health_data import (
    CROP_PESTS_DISEASES, IPM_RECOMMENDATIONS, BANNED_CHEMICALS,
    WEATHER_DISEASE_ALERTS, DEFICIENCY_VS_DISEASE, SAFETY_TIPS,
    get_pest_disease_info, check_banned_chemical, get_weather_based_alerts,
    diagnose_symptom
)
from data.marketplace_data import (
    find_nearby_shops, get_product_options, get_kifayati_option,
    compare_prices, format_shop_list
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
    
    # ==================== CROP HEALTH & PEST MANAGEMENT ====================
    
    def get_crop_pests_diseases(self, crop):
        """
        Get pest and disease information for a specific crop
        
        Args:
            crop: Name of the crop
            
        Returns:
            Dictionary with pests and diseases information
        """
        return get_pest_disease_info(crop)
    
    def get_ipm_tier1_prevention(self):
        """Get Tier 1 IPM recommendations (Prevention - Bhoomi Raksha)"""
        return IPM_RECOMMENDATIONS.get("Tier1_Prevention", {})
    
    def get_ipm_tier2_organic(self):
        """Get Tier 2 IPM recommendations (Organic & Mechanical - Jugaad)"""
        return IPM_RECOMMENDATIONS.get("Tier2_Organic_Mechanical", {})
    
    def get_ipm_tier3_chemical(self):
        """Get Tier 3 IPM recommendations (Chemical - Last Resort)"""
        return IPM_RECOMMENDATIONS.get("Tier3_Chemical", {})
    
    def check_crop_rotation_compatibility(self, current_crop, previous_crop):
        """
        Check if crop rotation is safe based on plant families
        
        Args:
            current_crop: Crop to be planted
            previous_crop: Previous crop in the field
            
        Returns:
            Dictionary with compatibility status and recommendation
        """
        tier1 = self.get_ipm_tier1_prevention()
        crop_families = {}
        
        for method in tier1.get("methods", []):
            if method.get("method") == "Crop Rotation":
                crop_families = method.get("crop_families", {})
                break
        
        # Find families of both crops
        current_family = None
        previous_family = None
        
        for family, crops in crop_families.items():
            if any(current_crop in c for c in crops):
                current_family = family
            if any(previous_crop in c for c in crops):
                previous_family = family
        
        if current_family and previous_family:
            if current_family == previous_family:
                return {
                    "compatible": False,
                    "reason": f"Both crops belong to {current_family} family",
                    "recommendation": f"Avoid planting {current_crop} after {previous_crop}. Choose a crop from different family."
                }
            else:
                return {
                    "compatible": True,
                    "reason": f"{current_crop} ({current_family}) and {previous_crop} ({previous_family}) are from different families",
                    "recommendation": "Good rotation choice! This will help break pest and disease cycles."
                }
        
        return {
            "compatible": True,
            "reason": "Crop family information not available",
            "recommendation": "Consult with local agriculture officer for best rotation practices."
        }
    
    def check_chemical_ban_status(self, chemical_name):
        """
        Check if a chemical is banned and get safer alternatives
        
        Args:
            chemical_name: Name of the chemical/pesticide
            
        Returns:
            Dictionary with ban status and alternatives
        """
        is_banned, details = check_banned_chemical(chemical_name)
        
        if is_banned:
            return {
                "banned": True,
                "chemical": details["name"],
                "reason": details["reason"],
                "ban_year": details.get("ban_year", "Unknown"),
                "alternative": details.get("alternative", "Consult agriculture department"),
                "warning": f"⚠️ ALERT: {details['name']} is banned! {details['reason']}"
            }
        else:
            return {
                "banned": False,
                "chemical": chemical_name,
                "status": "Approved for use (always follow label instructions and safety protocols)"
            }
    
    def get_weather_disease_alert(self, humidity, temperature, rainfall_forecast=False, cloudy_days=0):
        """
        Get disease risk alerts based on weather conditions
        
        Args:
            humidity: Humidity percentage
            temperature: Temperature in Celsius
            rainfall_forecast: Whether rain is expected soon
            cloudy_days: Number of consecutive cloudy days
            
        Returns:
            List of disease alerts
        """
        return get_weather_based_alerts(humidity, temperature, rainfall_forecast, cloudy_days)
    
    def diagnose_plant_problem(self, symptom_type, crop=None, additional_info=None):
        """
        Diagnose whether plant symptoms are from nutrient deficiency or disease
        
        Args:
            symptom_type: Type of symptom (e.g., "Yellowing_Leaves", "Brown_Spots_Leaves")
            crop: Crop name (optional)
            additional_info: Additional observation details
            
        Returns:
            Diagnostic information with remedies
        """
        diagnosis = diagnose_symptom(symptom_type, crop)
        
        if not diagnosis:
            return {
                "symptom": symptom_type,
                "diagnosis": "Unable to determine cause. Please consult local agriculture extension officer or upload a photo for better diagnosis."
            }
        
        return {
            "symptom": symptom_type,
            "crop": crop,
            "possible_causes": diagnosis,
            "recommendation": "Compare your plant symptoms with descriptions above to identify the correct cause and apply appropriate remedy."
        }
    
    def generate_ipm_recommendation(self, crop, pest_or_disease, pest_count=None):
        """
        Generate 3-tier IPM recommendation for a specific pest/disease
        
        Args:
            crop: Crop name
            pest_or_disease: Name of pest or disease
            pest_count: Actual pest count (for ETL check)
            
        Returns:
            Formatted IPM recommendation with all 3 tiers
        """
        crop_info = self.get_crop_pests_diseases(crop)
        tier1 = self.get_ipm_tier1_prevention()
        tier2 = self.get_ipm_tier2_organic()
        tier3 = self.get_ipm_tier3_chemical()
        
        response = f"{self.greeting}\n\n"
        response += f"## IPM (Integrated Pest Management) for {pest_or_disease} in {crop}\n\n"
        response += "**3-Step Ward-Off Strategy:**\n\n"
        
        # Find specific pest/disease info
        target_info = None
        etl_threshold = None
        
        for pest in crop_info.get("pests", []):
            if pest_or_disease.lower() in pest["name"].lower():
                target_info = pest
                etl_threshold = pest.get("etl_threshold")
                break
        
        if not target_info:
            for disease in crop_info.get("diseases", []):
                if pest_or_disease.lower() in disease["name"].lower():
                    target_info = disease
                    break
        
        if target_info:
            response += f"**Problem Identified:** {target_info['name']}\n"
            if "symptoms" in target_info:
                response += f"**Symptoms:** {target_info['symptoms']}\n\n"
        
        # Tier 1: Prevention
        response += f"### 🛡️ Tier 1: {tier1['name']}\n"
        response += "**Prevention is better than cure! These methods reduce pest/disease occurrence by 60-70%:**\n\n"
        
        for method in tier1.get("methods", [])[:3]:  # Show top 3 prevention methods
            response += f"**{method['method']}**\n"
            response += f"- {method['description']}\n"
            response += f"- Cost: {method.get('cost_estimate', 'Low')}\n"
            if "effectiveness" in method:
                response += f"- Effectiveness: {method['effectiveness']}\n"
            response += "\n"
        
        # Tier 2: Organic & Mechanical
        response += f"### 🌱 Tier 2: {tier2['name']}\n"
        response += "**If pest/disease appears, try these organic methods first:**\n\n"
        
        for method in tier2.get("methods", [])[:3]:  # Show top 3 organic methods
            response += f"**{method['method']}**\n"
            response += f"- {method['description']}\n"
            if "recipe" in method:
                response += f"- How to use: {method['recipe']}\n"
            response += f"- Cost: {method.get('cost_estimate', 'Medium')}\n"
            response += f"- Effectiveness: {method.get('effectiveness', '60-70% control')}\n"
            response += "\n"
        
        # Tier 3: Chemical (with ETL check)
        response += f"### ⚗️ Tier 3: {tier3['name']}\n"
        response += "**⚠️ Use chemicals ONLY as last resort and ONLY if pest count is above Economic Threshold Level (ETL)**\n\n"
        
        if etl_threshold:
            response += f"**ETL for {pest_or_disease}:** {etl_threshold}\n"
            if pest_count:
                response += f"**Your count:** {pest_count}\n"
                # Simple ETL check (simplified - in real implementation would parse threshold properly)
                response += f"**Action:** {'✓ Spray recommended' if 'above' in str(pest_count).lower() else '✗ Below threshold - DO NOT spray yet'}\n\n"
        
        response += "**If spraying is necessary:**\n"
        response += "1. Choose selective chemicals that spare beneficial insects\n"
        response += "2. Always wear protective gear (mask, gloves, full clothes)\n"
        response += "3. Spray in early morning or late evening\n"
        response += "4. Never spray during flowering or if rain is expected\n"
        response += "5. Follow Pre-Harvest Interval (PHI) strictly\n\n"
        
        # Safety tips
        response += "### 🔒 Safety First!\n"
        safety_tips_en = SAFETY_TIPS.get("english", {})
        response += "**Before Spraying:**\n"
        for tip in safety_tips_en.get("before_spray", [])[:3]:
            response += f"- {tip}\n"
        
        response += "\n**During Spraying:**\n"
        for tip in safety_tips_en.get("during_spray", [])[:3]:
            response += f"- {tip}\n"
        
        response += "\n---\n"
        response += "*Would you like me to find nearby shops for organic pest control products?*\n"
        
        return response
    
    # ==================== MARKETPLACE INTEGRATION ====================
    
    def find_shops_for_product(self, product_name, state, district=None):
        """
        Find nearby shops selling a specific product
        
        Args:
            product_name: Product to search for
            state: State name
            district: District name (optional)
            
        Returns:
            Formatted shop list with product availability
        """
        shops = find_nearby_shops(state, district)
        
        response = f"## Shops for {product_name} in {state}\n\n"
        
        if district:
            response += f"**District:** {district}\n\n"
        
        response += format_shop_list(shops, include_distance=False)
        
        response += "\n\n### 💰 Price Comparison:\n\n"
        
        # Try to match product name to known products
        product_keys = {
            "neem": "Neem_Oil",
            "sticky trap": "Yellow_Sticky_Traps",
            "trichoderma": "Trichoderma",
            "pheromone": "Pheromone_Traps",
            "imidacloprid": "Imidacloprid",
            "chlorantraniliprole": "Chlorantraniliprole",
            "mancozeb": "Mancozeb",
            "azoxystrobin": "Azoxystrobin"
        }
        
        matched_key = None
        for key, product_key in product_keys.items():
            if key in product_name.lower():
                matched_key = product_key
                break
        
        if matched_key:
            price_info = compare_prices(matched_key)
            response += price_info
            
            kifayati = get_kifayati_option(matched_key)
            if kifayati:
                response += f"\n\n**💡 Kifayati (Most Economical) Option:**\n"
                response += f"- {kifayati['name']}: ₹{kifayati['price']}\n"
        else:
            response += "Contact shops above for current pricing.\n"
        
        response += "\n\n*📞 Tap phone numbers above to call shops directly and confirm stock availability.*\n"
        
        return response
    
    def get_product_recommendations_with_shops(self, product_category, state):
        """
        Get product recommendations along with shop locations
        
        Args:
            product_category: Category like "organic_pesticide", "bio_fungicide"
            state: State name
            
        Returns:
            Product recommendations with shop information
        """
        response = f"## {product_category.replace('_', ' ').title()} Options\n\n"
        
        # Map categories to products
        category_products = {
            "organic_pesticide": ["Neem_Oil"],
            "bio_fungicide": ["Trichoderma"],
            "pest_trap": ["Yellow_Sticky_Traps", "Pheromone_Traps"],
            "chemical_insecticide": ["Imidacloprid", "Chlorantraniliprole"],
            "fungicide": ["Mancozeb", "Azoxystrobin"]
        }
        
        products = category_products.get(product_category, [])
        
        for product_key in products:
            price_info = compare_prices(product_key, include_description=True)
            response += price_info + "\n\n"
        
        response += "\n---\n\n"
        response += f"### 📍 Where to Buy in {state}:\n\n"
        
        shops = find_nearby_shops(state)
        response += format_shop_list(shops[:3], include_distance=False)  # Show top 3 shops
        
        return response
    
    def check_spray_timing_weather(self, rainfall_forecast_hours=None):
        """
        Check if it's safe to spray based on weather
        
        Args:
            rainfall_forecast_hours: Hours until expected rainfall
            
        Returns:
            Weather advisory for spraying
        """
        response = "## ⛅ Weather Advisory for Spraying\n\n"
        
        if rainfall_forecast_hours is not None:
            if rainfall_forecast_hours < 4:
                response += "🚫 **DO NOT SPRAY NOW!**\n\n"
                response += f"Rain is expected in {rainfall_forecast_hours} hours. Spraying now will:\n"
                response += "- Waste your money (chemicals will wash away)\n"
                response += "- Pollute water sources\n"
                response += "- Not control pests/diseases effectively\n\n"
                response += f"**Recommendation:** Wait until at least 4 hours of dry weather is assured after spraying.\n"
                response += "Better to delay by 1-2 days than to waste chemicals.\n"
            elif rainfall_forecast_hours < 24:
                response += "⚠️ **CAUTION!**\n\n"
                response += f"Rain expected in {rainfall_forecast_hours} hours. You have a narrow window.\n"
                response += "Only spray if:\n"
                response += "- The problem is critical and can't wait\n"
                response += "- You can complete spraying in next 2-3 hours\n"
                response += "- Using systemic chemicals that absorb within 2-3 hours\n"
            else:
                response += "✅ **GOOD TIME TO SPRAY**\n\n"
                response += f"No rain expected for {rainfall_forecast_hours} hours.\n"
                response += "**Best timing:**\n"
                response += "- Early morning (6:00-9:00 AM) - Less wind, cooler temperature\n"
                response += "- Late evening (4:00-6:00 PM) - After heat, before dew\n\n"
                response += "**Avoid:**\n"
                response += "- Mid-day (too hot, chemicals evaporate)\n"
                response += "- Windy conditions (spray drift to other fields)\n"
                response += "- During flowering (harmful to bees)\n"
        else:
            response += "⚠️ **Weather forecast not available**\n\n"
            response += "**General guidelines:**\n"
            response += "- Check local weather forecast before spraying\n"
            response += "- Spray only if 4+ hours of dry weather assured\n"
            response += "- Prefer early morning or late evening\n"
            response += "- Avoid windy days and flowering period\n"
        
        return response


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
