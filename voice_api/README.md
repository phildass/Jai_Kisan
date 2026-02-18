# Voice API Integration for (J)ai Kisan

## Overview

The Voice API system provides a flexible, configurable voice assistant integration that supports multiple voice service providers. It enables (J)ai Kisan to deliver agricultural advice via voice calls in multiple Indian languages, with automatic provider selection, user preferences, and fallback mechanisms.

## Architecture

### Components

1. **Base Interface** (`base.py`)
   - Abstract base class defining the common interface
   - All providers must implement: `send_voice_answer()`, `receive_voice_query()`, `get_status()`

2. **Provider Implementations**
   - **Bharati Voice API** (`bharati_voice.py`) - New Bharat-VISTAAR 2026 platform
   - **Legacy Voice API** (`legacy_voice.py`) - Traditional voice platform

3. **Factory Pattern** (`factory.py`)
   - Provider selection logic
   - Region-based routing
   - User preference override
   - Automatic fallback

## Quick Start

### Basic Usage

```python
from voice_api import get_voice_api

# Get default provider
voice_api = get_voice_api()

# Send voice answer to farmer
farmer_profile = {
    'mobile': '+919876543210',
    'name': 'राम कुमार',
    'state': 'Punjab',
    'preferred_language': 'hi'
}

result = voice_api.send_voice_answer(
    "आपकी धान की फसल के लिए 50 किलो यूरिया प्रति एकड़",
    farmer_profile
)
print(result)  # {'success': True, 'message_id': '...', ...}
```

### Provider Selection

#### 1. Explicit Provider Selection

```python
from voice_api import get_voice_api

# Explicitly use Bharati
bharati = get_voice_api(provider_name='bharati')

# Explicitly use Legacy
legacy = get_voice_api(provider_name='legacy')
```

#### 2. Region-Based Selection

```python
# Provider automatically selected based on farmer's state
farmer_profile = {
    'mobile': '+919876543210',
    'state': 'Punjab'  # Punjab uses Bharati by default
}

voice_api = get_voice_api(farmer_profile=farmer_profile)
```

#### 3. User Preference Override

```python
# Farmer from Punjab (default Bharati) prefers Legacy
farmer_profile = {
    'mobile': '+919876543210',
    'state': 'Punjab',
    'voice_api_preference': 'legacy'  # User override
}

voice_api = get_voice_api(farmer_profile=farmer_profile)
```

### Factory API

For advanced usage, use the factory directly:

```python
from voice_api import get_factory_instance

factory = get_factory_instance()

# Send with automatic fallback
result = factory.send_voice_answer(message, farmer_profile)

# Get status of all providers
status = factory.get_provider_status()

# Get provider for specific region
provider = factory.get_provider_for_region('Tamil Nadu')
```

## Configuration

### Environment Variables

Add these to your `.env` file:

```bash
# Default provider selection
VOICE_API_PROVIDER=bharati

# Bharati Voice API Configuration
BHARATI_API_KEY=your-bharati-api-key
BHARATI_API_ENDPOINT=https://api.bharati-vistaar.gov.in/v1

# Legacy Voice API Configuration
LEGACY_API_KEY=your-legacy-api-key
LEGACY_API_ENDPOINT=https://api.voice-legacy.example.com/v1
LEGACY_ACCOUNT_SID=your-legacy-account-sid
```

### Programmatic Configuration

```python
from voice_api import VoiceAPIFactory

config = {
    'default_provider': 'bharati',
    'auto_fallback': True,
    'bharati': {
        'api_key': 'your-bharati-key',
        'api_endpoint': 'https://api.bharati.gov.in/v1',
        'default_language': 'hi'
    },
    'legacy': {
        'api_key': 'your-legacy-key',
        'api_endpoint': 'https://api.legacy.com/v1'
    }
}

factory = VoiceAPIFactory(config)
```

## Regional Preferences

The system includes pre-configured regional preferences optimized for network coverage and language support:

| Region | States | Preferred Provider | Reason |
|--------|--------|-------------------|--------|
| North India | Punjab, Haryana, UP, etc. | Bharati | Excellent coverage, multi-language |
| South India | TN, Karnataka, Kerala, etc. | Bharati | Better regional language support |
| Northeast | Assam, Meghalaya, etc. | Legacy | Better infrastructure in remote areas |
| East India | West Bengal, Bihar, etc. | Bharati | Multi-language transcription |
| West India | Maharashtra, Gujarat, etc. | Bharati | Modern features |

Users can override these defaults through their profile preferences.

## API Reference

### VoiceAPIBase (Abstract)

Base class that all providers must implement.

#### Methods

**`send_voice_answer(query: str, farmer_profile: Dict) -> Dict`**

Send a voice message to the farmer.

Parameters:
- `query` (str): Message text to be spoken
- `farmer_profile` (dict): Farmer information
  - `mobile` (str): Phone number
  - `name` (str): Farmer's name
  - `state` (str): State name
  - `preferred_language` (str, optional): Language code

Returns:
- `success` (bool): Whether message was sent
- `message_id` (str): Unique message identifier
- `status` (str): Message status
- `provider` (str): Provider name
- `error` (str, optional): Error message if failed

**`receive_voice_query(call_event: Dict) -> Dict`**

Process incoming voice call/query.

Parameters:
- `call_event` (dict): Call event information
  - `call_id` (str): Call identifier
  - `from_number` (str): Caller's phone
  - `transcript` (str): Transcribed text
  - `audio_url` (str, optional): Recording URL

Returns:
- `success` (bool): Whether query was processed
- `query_text` (str): Transcribed query
- `farmer_mobile` (str): Caller's number
- `language` (str): Detected language
- `provider` (str): Provider name

**`get_status() -> Dict`**

Get provider health status.

Returns:
- `provider` (str): Provider name
- `available` (bool): Whether operational
- `last_query_time` (str): ISO timestamp of last query
- `last_error` (str, optional): Last error message

### BharatiVoiceAPI

Implementation for Bharat-VISTAAR 2026 platform.

**Features:**
- 15+ Indian language support (hi, en, bn, te, mr, ta, gu, kn, ml, pa, or, as, mai, ur, sa)
- Natural TTS (Text-to-Speech)
- High-accuracy transcription
- Government-backed infrastructure

**Additional Methods:**

**`get_supported_languages() -> List[str]`**

Returns list of supported language codes.

**`translate_query(query: str, from_lang: str, to_lang: str) -> str`**

Translate query between languages.

### LegacyVoiceAPI

Implementation for legacy/traditional voice platform.

**Features:**
- Basic IVR (Interactive Voice Response)
- 2 language support (Hindi, English)
- Recording capabilities
- Established infrastructure

**Additional Methods:**

**`get_supported_languages() -> List[str]`**

Returns list of supported language codes (only 'hi' and 'en').

### VoiceAPIFactory

Factory for managing providers with fallback logic.

**`get_provider(provider_name=None, farmer_profile=None, use_fallback=True) -> VoiceAPIBase`**

Get a provider instance with automatic selection.

**`send_voice_answer(query, farmer_profile, provider_name=None) -> Dict`**

Send voice answer with automatic fallback on failure.

**`receive_voice_query(call_event, provider_name=None) -> Dict`**

Process incoming query with appropriate provider.

**`get_provider_status() -> Dict`**

Get status of all providers.

**`get_all_providers() -> Dict[str, VoiceAPIBase]`**

Get all available provider instances.

## Flask API Endpoints

The voice API is integrated into the (J)ai Kisan web application with these endpoints:

### POST `/api/voice/send`

Send voice message to farmer.

**Request:**
```json
{
    "message": "आपकी फसल के लिए 50 किलो यूरिया प्रति एकड़"
}
```

**Response:**
```json
{
    "success": true,
    "message_id": "bharati_1234567890",
    "status": "queued",
    "provider": "bharati"
}
```

### POST `/api/voice/query`

Process incoming voice query (webhook endpoint).

**Request:**
```json
{
    "call_id": "call_123",
    "from_number": "+919876543210",
    "transcript": "धान के लिए कौन सा खाद?",
    "detected_language": "hi"
}
```

**Response:**
```json
{
    "success": true,
    "query_received": "धान के लिए कौन सा खाद?",
    "provider": "bharati"
}
```

### GET `/api/voice/status`

Get status of voice API system.

**Response:**
```json
{
    "providers": {
        "bharati": {"available": true, "provider": "bharati"},
        "legacy": {"available": true, "provider": "legacy"}
    },
    "default_provider": "bharati",
    "auto_fallback_enabled": true,
    "user_preference": "bharati",
    "user_state": "Punjab"
}
```

### POST `/api/voice/preference`

Update user's voice provider preference.

**Request:**
```json
{
    "preference": "legacy"
}
```

**Response:**
```json
{
    "success": true,
    "preference": "legacy",
    "message": "Voice API preference updated successfully"
}
```

## Fallback Mechanism

The system automatically falls back to an alternative provider if the primary fails:

```python
# Auto-fallback is enabled by default
factory = get_factory_instance()

# If Bharati fails, automatically tries Legacy
result = factory.send_voice_answer(message, farmer_profile)

if result.get('fallback_used'):
    print(f"Fallback used: {result['primary_provider']} -> {result['provider']}")
```

### Disabling Fallback

```python
factory = VoiceAPIFactory({'auto_fallback': False})
```

## Testing

Run the comprehensive test suite:

```bash
python test_voice_api.py
```

Test coverage includes:
- Base interface validation
- Both provider implementations
- Factory provider selection
- Region-based routing
- User preference override
- Automatic fallback
- End-to-end integration

## Adding New Providers

To add a new voice API provider:

### 1. Create Provider Class

```python
# voice_api/new_provider.py
from .base import VoiceAPIBase

class NewProviderAPI(VoiceAPIBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.provider_name = "newprovider"
        # Initialize provider-specific configuration
    
    def send_voice_answer(self, query, farmer_profile):
        # Implement sending voice message
        pass
    
    def receive_voice_query(self, call_event):
        # Implement receiving voice query
        pass
    
    def get_status(self):
        # Implement status check
        pass
```

### 2. Register in Factory

```python
# voice_api/factory.py
from .new_provider import NewProviderAPI

class VoiceAPIFactory:
    def _initialize_providers(self):
        # ... existing providers ...
        new_config = self.config.get('newprovider', {})
        self._providers['newprovider'] = NewProviderAPI(new_config)
```

### 3. Update __init__.py

```python
# voice_api/__init__.py
from .new_provider import NewProviderAPI

__all__ = [
    # ... existing ...
    'NewProviderAPI'
]
```

### 4. Add Configuration

```bash
# .env
NEWPROVIDER_API_KEY=your-key
NEWPROVIDER_API_ENDPOINT=https://api.newprovider.com/v1
```

### 5. Add Tests

Create tests in `test_voice_api.py` for the new provider.

## Language Support

### Bharati Voice API

Supports 15+ Indian languages:
- Hindi (hi)
- English (en)
- Bengali (bn)
- Telugu (te)
- Marathi (mr)
- Tamil (ta)
- Gujarati (gu)
- Kannada (kn)
- Malayalam (ml)
- Punjabi (pa)
- Odia (or)
- Assamese (as)
- Maithili (mai)
- Urdu (ur)
- Sanskrit (sa)

### Legacy Voice API

Limited to 2 languages:
- Hindi (hi)
- English (en)

## Best Practices

1. **Always provide farmer_profile**: Include state and language preferences for optimal routing
2. **Use the factory**: `get_voice_api()` or `get_factory_instance()` for automatic management
3. **Handle errors gracefully**: Check `result['success']` and handle `result['error']`
4. **Monitor provider status**: Regularly check `get_provider_status()` for health monitoring
5. **Enable fallback**: Keep auto-fallback enabled (default) for reliability
6. **Respect user preferences**: Always check for `voice_api_preference` in user profile
7. **Test both providers**: Ensure your application works with both Bharati and Legacy

## Troubleshooting

### Provider Unavailable

```python
status = factory.get_provider_status()
for name, info in status['providers'].items():
    if not info['available']:
        print(f"Provider {name} is down: {info.get('last_error')}")
```

### Fallback Not Working

Check configuration:
```python
factory = get_factory_instance()
print(f"Auto-fallback enabled: {factory.auto_fallback}")
```

### Wrong Provider Selected

Check selection priority:
1. Explicit provider_name parameter
2. User voice_api_preference
3. Regional preference (state-based)
4. Default from configuration

## Production Deployment

### Security

1. **Never commit API keys** - Use environment variables
2. **Secure webhook endpoints** - Validate incoming requests
3. **Use HTTPS** - Always use secure connections

### Monitoring

Track these metrics:
- Provider availability
- Response times
- Failure rates
- Fallback frequency
- Language distribution

### Scaling

- Both providers support concurrent requests
- Factory pattern allows easy horizontal scaling
- Consider request queuing for high volumes

## Support

For issues or questions:
- Check this documentation
- Run test suite: `python test_voice_api.py`
- Review provider status: `/api/voice/status`
- Contact development team

## License

Part of (J)ai Kisan - Agricultural Consultant System
