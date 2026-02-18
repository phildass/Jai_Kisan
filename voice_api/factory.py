"""
Voice API Factory and Provider Selection for (J)ai Kisan
Implements factory pattern with configurable provider selection, fallback logic
"""

import os
from typing import Dict, Any, Optional, List
from .base import VoiceAPIBase
from .bharati_voice import BharatiVoiceAPI
from .legacy_voice import LegacyVoiceAPI


# Regional preferences for voice providers
# Some regions may have better coverage with specific providers
REGIONAL_PREFERENCES = {
    # North India - Bharati has excellent coverage
    'Punjab': 'bharati',
    'Haryana': 'bharati',
    'Delhi': 'bharati',
    'Himachal Pradesh': 'bharati',
    'Uttarakhand': 'bharati',
    'Uttar Pradesh': 'bharati',
    'Rajasthan': 'bharati',
    
    # East India - Bharati preferred for multi-language support
    'West Bengal': 'bharati',
    'Bihar': 'bharati',
    'Jharkhand': 'bharati',
    'Odisha': 'bharati',
    
    # West India - Both providers work well
    'Maharashtra': 'bharati',
    'Gujarat': 'bharati',
    'Goa': 'bharati',
    
    # South India - Bharati better for regional languages
    'Karnataka': 'bharati',
    'Tamil Nadu': 'bharati',
    'Kerala': 'bharati',
    'Andhra Pradesh': 'bharati',
    'Telangana': 'bharati',
    
    # Northeast - Legacy has better infrastructure in some remote areas
    'Assam': 'legacy',
    'Meghalaya': 'legacy',
    'Tripura': 'legacy',
    'Mizoram': 'legacy',
    'Manipur': 'legacy',
    'Nagaland': 'legacy',
    'Arunachal Pradesh': 'legacy',
    'Sikkim': 'legacy',
    
    # Central India
    'Madhya Pradesh': 'bharati',
    'Chhattisgarh': 'bharati',
}


class VoiceAPIFactory:
    """
    Factory class for creating and managing voice API provider instances.
    
    Supports:
    - Configuration-based provider selection
    - Region-based provider selection
    - User preference override
    - Automatic fallback on provider failure
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Voice API Factory.
        
        Args:
            config: Configuration dictionary containing provider settings
        """
        self.config = config or {}
        self._providers = {}
        self._primary_provider = None
        self._fallback_provider = None
        
        # Load default provider from environment or config
        self.default_provider = (
            self.config.get('default_provider') or 
            os.getenv('VOICE_API_PROVIDER', 'bharati')
        ).lower()
        
        # Enable/disable automatic fallback
        self.auto_fallback = self.config.get('auto_fallback', True)
        
        # Initialize available providers
        self._initialize_providers()
    
    def _initialize_providers(self):
        """Initialize all available voice API providers."""
        # Initialize Bharati provider
        bharati_config = self.config.get('bharati', {})
        self._providers['bharati'] = BharatiVoiceAPI(bharati_config)
        
        # Initialize Legacy provider
        legacy_config = self.config.get('legacy', {})
        self._providers['legacy'] = LegacyVoiceAPI(legacy_config)
    
    def get_provider(
        self,
        provider_name: Optional[str] = None,
        farmer_profile: Optional[Dict[str, Any]] = None,
        use_fallback: bool = True
    ) -> VoiceAPIBase:
        """
        Get a voice API provider instance.
        
        Selection priority:
        1. Explicit provider_name parameter
        2. User/farmer preference from profile
        3. Region-based selection from farmer's state
        4. Default provider from configuration
        5. Fallback to alternative if primary fails
        
        Args:
            provider_name: Explicit provider name ('bharati' or 'legacy')
            farmer_profile: Farmer profile containing state and preferences
            use_fallback: Whether to use fallback provider if primary fails
        
        Returns:
            VoiceAPIBase instance (BharatiVoiceAPI or LegacyVoiceAPI)
        """
        # 1. Check explicit provider name
        selected_provider = None
        if provider_name:
            selected_provider = provider_name.lower()
        
        # 2. Check farmer profile for voice API preference
        elif farmer_profile and 'voice_api_preference' in farmer_profile:
            selected_provider = farmer_profile['voice_api_preference'].lower()
        
        # 3. Check region-based preference
        elif farmer_profile and 'state' in farmer_profile:
            state = farmer_profile['state']
            selected_provider = REGIONAL_PREFERENCES.get(state, self.default_provider)
        
        # 4. Use default provider
        else:
            selected_provider = self.default_provider
        
        # Validate provider name
        if selected_provider not in self._providers:
            selected_provider = self.default_provider
        
        # Get the provider instance
        provider = self._providers[selected_provider]
        
        # 5. Check if provider is available, use fallback if needed
        if use_fallback and self.auto_fallback:
            if not provider.check_availability():
                # Try fallback provider
                fallback_name = 'legacy' if selected_provider == 'bharati' else 'bharati'
                fallback_provider = self._providers[fallback_name]
                
                if fallback_provider.check_availability():
                    # Log fallback usage (in production, use logging module)
                    import logging
                    logger = logging.getLogger(__name__)
                    logger.info(f"Primary provider '{selected_provider}' unavailable, using fallback '{fallback_name}'")
                    return fallback_provider
        
        return provider
    
    def get_provider_for_region(self, state: str) -> VoiceAPIBase:
        """
        Get the recommended voice API provider for a specific state/region.
        
        Args:
            state: State name
        
        Returns:
            VoiceAPIBase instance
        """
        provider_name = REGIONAL_PREFERENCES.get(state, self.default_provider)
        return self._providers[provider_name]
    
    def get_all_providers(self) -> Dict[str, VoiceAPIBase]:
        """
        Get all available voice API providers.
        
        Returns:
            Dictionary mapping provider names to instances
        """
        return self._providers.copy()
    
    def get_provider_status(self) -> Dict[str, Any]:
        """
        Get status of all voice API providers.
        
        Returns:
            Dictionary with status of each provider
        """
        status = {}
        for name, provider in self._providers.items():
            status[name] = provider.get_status()
        
        return {
            'providers': status,
            'default_provider': self.default_provider,
            'auto_fallback_enabled': self.auto_fallback
        }
    
    def send_voice_answer(
        self,
        query: str,
        farmer_profile: Dict[str, Any],
        provider_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send voice answer using appropriate provider with automatic fallback.
        
        Args:
            query: Query/answer text to send
            farmer_profile: Farmer profile information
            provider_name: Optional specific provider to use
        
        Returns:
            Response dictionary from the provider
        """
        # Get primary provider
        provider = self.get_provider(provider_name, farmer_profile, use_fallback=False)
        
        # Try sending with primary provider
        result = provider.send_voice_answer(query, farmer_profile)
        
        # If failed and auto-fallback is enabled, try fallback
        if not result.get('success') and self.auto_fallback:
            fallback_name = 'legacy' if provider.provider_name == 'bharati' else 'bharati'
            fallback_provider = self._providers[fallback_name]
            
            # Log fallback attempt (in production, use logging module)
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Primary provider failed, attempting fallback to '{fallback_name}'")
            
            result = fallback_provider.send_voice_answer(query, farmer_profile)
            result['fallback_used'] = True
            result['primary_provider'] = provider.provider_name
        
        return result
    
    def receive_voice_query(
        self,
        call_event: Dict[str, Any],
        provider_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process incoming voice query using appropriate provider.
        
        Args:
            call_event: Call event data
            provider_name: Provider that received the call (if known)
        
        Returns:
            Processed query information
        """
        # Determine which provider received the call
        if not provider_name:
            # Try to detect from call_event metadata
            provider_name = call_event.get('provider', self.default_provider)
        
        provider = self._providers.get(provider_name.lower(), self._providers[self.default_provider])
        return provider.receive_voice_query(call_event)


# Global factory instance (singleton pattern)
_factory_instance = None


def get_voice_api(
    provider_name: Optional[str] = None,
    farmer_profile: Optional[Dict[str, Any]] = None,
    config: Optional[Dict[str, Any]] = None
) -> VoiceAPIBase:
    """
    Convenience function to get a voice API provider instance.
    
    This is the main entry point for getting voice API providers in the application.
    
    Args:
        provider_name: Explicit provider name ('bharati' or 'legacy')
        farmer_profile: Farmer profile for region/preference-based selection
        config: Optional configuration dictionary (only needed on first call)
    
    Returns:
        VoiceAPIBase instance
    
    Example:
        # Get default provider
        voice_api = get_voice_api()
        
        # Get specific provider
        voice_api = get_voice_api(provider_name='bharati')
        
        # Get based on farmer profile
        voice_api = get_voice_api(farmer_profile={'state': 'Punjab'})
        
        # Get with user preference
        voice_api = get_voice_api(farmer_profile={
            'state': 'Maharashtra',
            'voice_api_preference': 'legacy'
        })
    """
    global _factory_instance
    
    # Initialize factory if not already done
    if _factory_instance is None:
        _factory_instance = VoiceAPIFactory(config)
    
    return _factory_instance.get_provider(provider_name, farmer_profile)


def get_factory_instance(config: Optional[Dict[str, Any]] = None) -> VoiceAPIFactory:
    """
    Get the global VoiceAPIFactory instance.
    
    Args:
        config: Optional configuration (used only on first initialization)
    
    Returns:
        VoiceAPIFactory instance
    """
    global _factory_instance
    
    if _factory_instance is None:
        _factory_instance = VoiceAPIFactory(config)
    
    return _factory_instance
