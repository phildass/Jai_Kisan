"""
Legacy Voice API Implementation for (J)ai Kisan
Traditional voice assistant platform (pre-2026)
"""

import os
from typing import Dict, Any, Optional
from datetime import datetime
from .base import VoiceAPIBase


class LegacyVoiceAPI(VoiceAPIBase):
    """
    Implementation for Legacy Voice API.
    
    This represents the earlier voice assistant platform used before
    Bharati/Bharat-VISTAAR. Provides basic voice call and IVR functionality.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Legacy Voice API provider.
        
        Args:
            config: Configuration dictionary with keys:
                - api_key: Legacy API authentication key
                - api_endpoint: Legacy API base URL
                - account_sid: Account SID (for Twilio-like APIs)
                - timeout: Request timeout in seconds (default: 30)
        """
        super().__init__(config)
        self.provider_name = "legacy"
        
        # Load configuration from environment or config dict
        self.api_key = self.config.get('api_key') or os.getenv('LEGACY_API_KEY', '')
        self.api_endpoint = self.config.get('api_endpoint') or os.getenv(
            'LEGACY_API_ENDPOINT',
            'https://api.voice-legacy.example.com/v1'
        )
        self.account_sid = self.config.get('account_sid') or os.getenv('LEGACY_ACCOUNT_SID', '')
        self.timeout = self.config.get('timeout', 30)
        
        # Legacy system supports limited languages
        self.supported_languages = ['hi', 'en']
    
    def send_voice_answer(self, query: str, farmer_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send voice answer via Legacy Voice API.
        
        Args:
            query: The farmer's query/answer text to be spoken
            farmer_profile: Farmer information including mobile, name, state
        
        Returns:
            Response dictionary with success status and message details
        """
        try:
            # Extract farmer details
            mobile = farmer_profile.get('mobile', '')
            name = farmer_profile.get('name', 'Farmer')
            language = farmer_profile.get('preferred_language', 'hi')
            
            # Legacy only supports Hindi and English
            if language not in self.supported_languages:
                language = 'hi'
            
            # In a real implementation, this would make an HTTP request to Legacy API
            # For now, we'll simulate the API call
            
            # Prepare request payload (simulated)
            payload = {
                'to': mobile,
                'from': self.config.get('caller_id', '+911234567890'),
                'text': query,
                'language': language,
                'voice': 'female' if language == 'hi' else 'male'
            }
            
            # Simulate API call (in production, use requests library)
            # response = requests.post(
            #     f"{self.api_endpoint}/calls",
            #     auth=(self.account_sid, self.api_key),
            #     json=payload,
            #     timeout=self.timeout
            # )
            
            # Simulated successful response
            message_id = f"legacy_{datetime.utcnow().timestamp()}"
            
            self.last_query_time = datetime.utcnow()
            self.clear_error()
            
            return {
                'success': True,
                'message_id': message_id,
                'status': 'initiated',
                'provider': self.provider_name,
                'recipient': mobile,
                'language': language,
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            error_msg = f"Legacy Voice API error: {str(e)}"
            self.set_error(error_msg)
            return {
                'success': False,
                'error': error_msg,
                'provider': self.provider_name
            }
    
    def receive_voice_query(self, call_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming voice query from Legacy platform.
        
        Args:
            call_event: Call event data from Legacy system
        
        Returns:
            Processed query information
        """
        try:
            # Extract call details (Legacy format)
            call_id = call_event.get('CallSid') or call_event.get('call_id', '')
            from_number = call_event.get('From') or call_event.get('from_number', '')
            
            # Legacy may have basic transcription or require manual processing
            transcript = call_event.get('TranscriptionText') or call_event.get('transcript', '')
            recording_url = call_event.get('RecordingUrl') or call_event.get('audio_url', '')
            
            # Legacy has limited language detection
            language = call_event.get('language', 'hi')
            
            self.last_query_time = datetime.utcnow()
            self.clear_error()
            
            return {
                'success': True,
                'query_text': transcript,
                'call_id': call_id,
                'farmer_mobile': from_number,
                'language': language,
                'recording_url': recording_url,
                'provider': self.provider_name,
                'timestamp': datetime.utcnow().isoformat(),
                'note': 'Legacy API - may require manual transcription review'
            }
            
        except Exception as e:
            error_msg = f"Legacy Voice API receive error: {str(e)}"
            self.set_error(error_msg)
            return {
                'success': False,
                'error': error_msg,
                'provider': self.provider_name
            }
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get Legacy Voice API status.
        
        Returns:
            Status information dictionary
        """
        try:
            # In production, this would check the Legacy API health
            # response = requests.get(
            #     f"{self.api_endpoint}/status",
            #     auth=(self.account_sid, self.api_key),
            #     timeout=5
            # )
            
            # Simulated health check
            is_configured = bool(self.api_key and self.api_endpoint)
            
            return {
                'provider': self.provider_name,
                'available': is_configured and self.is_available,
                'last_query_time': self.last_query_time.isoformat() if self.last_query_time else None,
                'last_error': self.last_error,
                'endpoint': self.api_endpoint,
                'configured': is_configured,
                'supported_languages': len(self.supported_languages),
                'additional_info': {
                    'platform': 'Legacy Voice System',
                    'features': ['basic_tts', 'ivr', 'recording'],
                    'limitations': 'Limited language support and transcription accuracy'
                }
            }
            
        except Exception as e:
            return {
                'provider': self.provider_name,
                'available': False,
                'error': str(e)
            }
    
    def get_supported_languages(self) -> list:
        """
        Get list of languages supported by Legacy platform.
        
        Returns:
            List of language codes
        """
        return self.supported_languages
