"""
Base Voice API Interface for (J)ai Kisan
Abstract base class defining the common interface for all voice assistant providers
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime


class VoiceAPIBase(ABC):
    """
    Abstract base class for voice assistant API providers.
    
    All voice API implementations must inherit from this class and implement
    the required methods to ensure compatibility with the (J)ai Kisan system.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the voice API provider.
        
        Args:
            config: Optional configuration dictionary containing API credentials,
                   endpoints, and other provider-specific settings
        """
        self.config = config or {}
        self.provider_name = "base"
        self.is_available = True
        self.last_error = None
        self.last_query_time = None
        
    @abstractmethod
    def send_voice_answer(self, query: str, farmer_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a voice answer/response to the farmer.
        
        Args:
            query: The farmer's original query text
            farmer_profile: Dictionary containing farmer information:
                - mobile: Farmer's mobile number
                - name: Farmer's name
                - state: Farmer's state
                - preferred_language: Language preference (optional)
                - other farmer details
        
        Returns:
            Dictionary containing:
                - success: Boolean indicating if the answer was sent
                - message_id: Unique identifier for the voice message
                - status: Status of the voice call/message
                - error: Error message if success is False
        """
        pass
    
    @abstractmethod
    def receive_voice_query(self, call_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process an incoming voice query from a farmer.
        
        Args:
            call_event: Dictionary containing call/voice event information:
                - call_id: Unique call identifier
                - from_number: Caller's phone number
                - audio_url: URL to recorded audio (if available)
                - transcript: Text transcript of the voice query
                - timestamp: Time of the call
                - other provider-specific fields
        
        Returns:
            Dictionary containing:
                - success: Boolean indicating if query was processed
                - query_text: Transcribed query text
                - call_id: Call identifier
                - farmer_mobile: Identified farmer's mobile number
                - error: Error message if success is False
        """
        pass
    
    @abstractmethod
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status and health of the voice API provider.
        
        Returns:
            Dictionary containing:
                - provider: Name of the voice API provider
                - available: Boolean indicating if provider is operational
                - last_query_time: Timestamp of last query (if any)
                - last_error: Last error message (if any)
                - additional_info: Provider-specific status information
        """
        pass
    
    def check_availability(self) -> bool:
        """
        Check if the voice API provider is currently available.
        
        Returns:
            Boolean indicating provider availability
        """
        try:
            status = self.get_status()
            self.is_available = status.get('available', False)
            return self.is_available
        except Exception as e:
            self.is_available = False
            self.last_error = str(e)
            return False
    
    def get_provider_name(self) -> str:
        """
        Get the name of this voice API provider.
        
        Returns:
            String name of the provider
        """
        return self.provider_name
    
    def set_error(self, error_msg: str):
        """
        Record an error for this provider.
        
        Args:
            error_msg: Error message to record
        """
        self.last_error = error_msg
        self.is_available = False
    
    def clear_error(self):
        """Clear the last error and mark provider as available."""
        self.last_error = None
        self.is_available = True
