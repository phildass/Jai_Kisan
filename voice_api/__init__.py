"""
Voice API Package for (J)ai Kisan
Flexible, configurable voice assistant integration supporting multiple providers
"""

from .base import VoiceAPIBase
from .factory import get_voice_api, VoiceAPIFactory, get_factory_instance
from .bharati_voice import BharatiVoiceAPI
from .legacy_voice import LegacyVoiceAPI

__all__ = [
    'VoiceAPIBase',
    'get_voice_api',
    'VoiceAPIFactory',
    'get_factory_instance',
    'BharatiVoiceAPI',
    'LegacyVoiceAPI'
]

__version__ = '1.0.0'
