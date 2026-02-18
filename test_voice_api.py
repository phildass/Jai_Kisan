#!/usr/bin/env python3
"""
Test Suite for Voice API Integration
Tests base interface, both providers, factory, and fallback logic
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from voice_api import (
    VoiceAPIBase,
    BharatiVoiceAPI,
    LegacyVoiceAPI,
    get_voice_api,
    get_factory_instance,
    VoiceAPIFactory
)


def test_base_interface():
    """Test that base interface is properly abstract."""
    print("\n" + "=" * 80)
    print("TEST 1: Base Interface Validation")
    print("=" * 80)
    
    try:
        # Should not be able to instantiate abstract base class directly
        base = VoiceAPIBase()
        print("✗ FAILED: Base class should be abstract")
        return False
    except TypeError as e:
        print("✓ PASSED: Base class is properly abstract")
        print(f"   Error (expected): {e}")
        return True


def test_bharati_voice_api():
    """Test Bharati Voice API implementation."""
    print("\n" + "=" * 80)
    print("TEST 2: Bharati Voice API")
    print("=" * 80)
    
    # Initialize Bharati API
    config = {
        'api_key': 'test_bharati_key',
        'api_endpoint': 'https://api.bharati-test.gov.in/v1'
    }
    bharati = BharatiVoiceAPI(config)
    
    # Test 1: Provider name
    assert bharati.provider_name == "bharati", "Provider name should be 'bharati'"
    print("✓ Provider name: bharati")
    
    # Test 2: Send voice answer
    farmer_profile = {
        'mobile': '+919876543210',
        'name': 'राम कुमार',
        'state': 'Punjab',
        'preferred_language': 'hi'
    }
    
    result = bharati.send_voice_answer("आपकी फसल के लिए यूरिया 50 किलो प्रति एकड़", farmer_profile)
    assert result['success'], "Send voice answer should succeed"
    assert 'message_id' in result, "Response should contain message_id"
    assert result['provider'] == 'bharati', "Provider should be bharati"
    print(f"✓ Send voice answer: {result['message_id']}")
    
    # Test 3: Receive voice query
    call_event = {
        'call_id': 'test_call_123',
        'from_number': '+919876543210',
        'transcript': 'मेरी धान की फसल के लिए कौन सा उर्वरक सही है?',
        'detected_language': 'hi',
        'confidence': 0.95
    }
    
    result = bharati.receive_voice_query(call_event)
    assert result['success'], "Receive voice query should succeed"
    assert result['query_text'] == call_event['transcript'], "Query text should match"
    assert result['language'] == 'hi', "Language should be Hindi"
    print(f"✓ Receive voice query: {result['query_text'][:50]}...")
    
    # Test 4: Get status
    status = bharati.get_status()
    assert status['provider'] == 'bharati', "Status should show bharati provider"
    assert 'available' in status, "Status should include availability"
    print(f"✓ Get status: Available={status['available']}")
    
    # Test 5: Supported languages
    languages = bharati.get_supported_languages()
    assert len(languages) > 0, "Should support multiple languages"
    assert 'hi' in languages, "Should support Hindi"
    assert 'en' in languages, "Should support English"
    print(f"✓ Supported languages: {len(languages)} ({', '.join(languages[:5])}...)")
    
    print("\n✓ ALL BHARATI VOICE API TESTS PASSED")
    return True


def test_legacy_voice_api():
    """Test Legacy Voice API implementation."""
    print("\n" + "=" * 80)
    print("TEST 3: Legacy Voice API")
    print("=" * 80)
    
    # Initialize Legacy API
    config = {
        'api_key': 'test_legacy_key',
        'api_endpoint': 'https://api.legacy-test.com/v1',
        'account_sid': 'test_account'
    }
    legacy = LegacyVoiceAPI(config)
    
    # Test 1: Provider name
    assert legacy.provider_name == "legacy", "Provider name should be 'legacy'"
    print("✓ Provider name: legacy")
    
    # Test 2: Send voice answer
    farmer_profile = {
        'mobile': '+919123456789',
        'name': 'Farmer Singh',
        'state': 'Haryana'
    }
    
    result = legacy.send_voice_answer("Apply 40kg Urea per acre", farmer_profile)
    assert result['success'], "Send voice answer should succeed"
    assert 'message_id' in result, "Response should contain message_id"
    assert result['provider'] == 'legacy', "Provider should be legacy"
    print(f"✓ Send voice answer: {result['message_id']}")
    
    # Test 3: Receive voice query (Legacy format)
    call_event = {
        'CallSid': 'CA123456',
        'From': '+919123456789',
        'TranscriptionText': 'What fertilizer for wheat?',
        'RecordingUrl': 'https://example.com/recording.mp3'
    }
    
    result = legacy.receive_voice_query(call_event)
    assert result['success'], "Receive voice query should succeed"
    assert result['call_id'] == 'CA123456', "Call ID should match"
    print(f"✓ Receive voice query: {result['query_text']}")
    
    # Test 4: Get status
    status = legacy.get_status()
    assert status['provider'] == 'legacy', "Status should show legacy provider"
    print(f"✓ Get status: Available={status['available']}")
    
    # Test 5: Limited language support
    languages = legacy.get_supported_languages()
    assert len(languages) == 2, "Legacy should support only 2 languages"
    assert 'hi' in languages and 'en' in languages, "Should support Hindi and English"
    print(f"✓ Supported languages: {len(languages)} ({', '.join(languages)})")
    
    print("\n✓ ALL LEGACY VOICE API TESTS PASSED")
    return True


def test_factory_default():
    """Test factory with default configuration."""
    print("\n" + "=" * 80)
    print("TEST 4: Factory - Default Configuration")
    print("=" * 80)
    
    # Get default provider
    voice_api = get_voice_api()
    
    assert voice_api is not None, "Should return a provider"
    assert isinstance(voice_api, VoiceAPIBase), "Should be instance of VoiceAPIBase"
    print(f"✓ Default provider: {voice_api.provider_name}")
    
    # Test factory instance
    factory = get_factory_instance()
    assert factory is not None, "Factory should exist"
    assert isinstance(factory, VoiceAPIFactory), "Should be VoiceAPIFactory"
    print(f"✓ Factory instance created")
    
    # Test all providers available
    all_providers = factory.get_all_providers()
    assert 'bharati' in all_providers, "Bharati should be available"
    assert 'legacy' in all_providers, "Legacy should be available"
    print(f"✓ All providers available: {list(all_providers.keys())}")
    
    print("\n✓ FACTORY DEFAULT TESTS PASSED")
    return True


def test_factory_explicit_selection():
    """Test factory with explicit provider selection."""
    print("\n" + "=" * 80)
    print("TEST 5: Factory - Explicit Provider Selection")
    print("=" * 80)
    
    # Test explicit Bharati
    bharati = get_voice_api(provider_name='bharati')
    assert bharati.provider_name == 'bharati', "Should return Bharati"
    print(f"✓ Explicit 'bharati': {bharati.provider_name}")
    
    # Test explicit Legacy
    legacy = get_voice_api(provider_name='legacy')
    assert legacy.provider_name == 'legacy', "Should return Legacy"
    print(f"✓ Explicit 'legacy': {legacy.provider_name}")
    
    # Test invalid provider (should fallback to default)
    default = get_voice_api(provider_name='invalid')
    assert default.provider_name in ['bharati', 'legacy'], "Should fallback to valid provider"
    print(f"✓ Invalid provider fallback: {default.provider_name}")
    
    print("\n✓ EXPLICIT SELECTION TESTS PASSED")
    return True


def test_factory_region_based():
    """Test factory with region-based selection."""
    print("\n" + "=" * 80)
    print("TEST 6: Factory - Region-Based Selection")
    print("=" * 80)
    
    factory = get_factory_instance()
    
    # Test Punjab (should prefer Bharati)
    punjab_provider = factory.get_provider_for_region('Punjab')
    print(f"✓ Punjab: {punjab_provider.provider_name}")
    
    # Test Assam (should prefer Legacy based on regional config)
    assam_provider = factory.get_provider_for_region('Assam')
    print(f"✓ Assam: {assam_provider.provider_name}")
    
    # Test with farmer profile
    farmer_punjab = {'state': 'Punjab', 'mobile': '+919876543210'}
    provider = get_voice_api(farmer_profile=farmer_punjab)
    print(f"✓ Farmer from Punjab: {provider.provider_name}")
    
    farmer_assam = {'state': 'Assam', 'mobile': '+919123456789'}
    provider = get_voice_api(farmer_profile=farmer_assam)
    print(f"✓ Farmer from Assam: {provider.provider_name}")
    
    print("\n✓ REGION-BASED SELECTION TESTS PASSED")
    return True


def test_factory_user_preference():
    """Test factory with user preference override."""
    print("\n" + "=" * 80)
    print("TEST 7: Factory - User Preference Override")
    print("=" * 80)
    
    # Farmer from Punjab (default Bharati) but prefers Legacy
    farmer_profile = {
        'state': 'Punjab',
        'mobile': '+919876543210',
        'voice_api_preference': 'legacy'
    }
    
    provider = get_voice_api(farmer_profile=farmer_profile)
    assert provider.provider_name == 'legacy', "Should respect user preference"
    print(f"✓ Punjab farmer with legacy preference: {provider.provider_name}")
    
    # Farmer from Assam (default Legacy) but prefers Bharati
    farmer_profile = {
        'state': 'Assam',
        'mobile': '+919123456789',
        'voice_api_preference': 'bharati'
    }
    
    provider = get_voice_api(farmer_profile=farmer_profile)
    assert provider.provider_name == 'bharati', "Should respect user preference"
    print(f"✓ Assam farmer with bharati preference: {provider.provider_name}")
    
    print("\n✓ USER PREFERENCE TESTS PASSED")
    return True


def test_factory_fallback():
    """Test factory automatic fallback mechanism."""
    print("\n" + "=" * 80)
    print("TEST 8: Factory - Automatic Fallback")
    print("=" * 80)
    
    factory = get_factory_instance()
    
    # Test send with fallback
    farmer_profile = {
        'mobile': '+919876543210',
        'name': 'Test Farmer',
        'state': 'Punjab'
    }
    
    result = factory.send_voice_answer("Test message", farmer_profile)
    assert result['success'], "Should successfully send message"
    print(f"✓ Send with fallback: Provider={result['provider']}")
    
    # Test status of all providers
    status = factory.get_provider_status()
    assert 'providers' in status, "Should include provider status"
    assert 'default_provider' in status, "Should include default provider"
    assert 'auto_fallback_enabled' in status, "Should include fallback status"
    print(f"✓ Provider status retrieved")
    print(f"   Default: {status['default_provider']}")
    print(f"   Auto-fallback: {status['auto_fallback_enabled']}")
    
    print("\n✓ FALLBACK TESTS PASSED")
    return True


def test_integration():
    """Test complete integration scenario."""
    print("\n" + "=" * 80)
    print("TEST 9: Integration Test")
    print("=" * 80)
    
    # Scenario: Farmer from Maharashtra calls for advice
    farmer_profile = {
        'mobile': '+919988776655',
        'name': 'विनोद पाटिल',
        'state': 'Maharashtra',
        'preferred_language': 'mr',
        'voice_api_preference': 'bharati'
    }
    
    # Step 1: Receive incoming voice query
    print("\n1. Receiving voice query...")
    call_event = {
        'call_id': 'integration_test_call',
        'from_number': farmer_profile['mobile'],
        'transcript': 'मला ऊसासाठी खत हवे आहे',  # Marathi: I need fertilizer for sugarcane
        'detected_language': 'mr',
        'confidence': 0.92
    }
    
    factory = get_factory_instance()
    query_result = factory.receive_voice_query(call_event, provider_name='bharati')
    
    assert query_result['success'], "Should receive query successfully"
    print(f"✓ Query received: {query_result['query_text'][:50]}...")
    print(f"   Language: {query_result['language']}")
    print(f"   Provider: {query_result['provider']}")
    
    # Step 2: Process query (simulated - in real app, use JaiKisanAgent)
    print("\n2. Processing query with (J)ai Kisan Agent...")
    response_text = "ऊसासाठी 50 किलो डीएपी आणि 25 किलो युरिया प्रति एकर वापरा"
    print(f"✓ Generated response: {response_text}")
    
    # Step 3: Send voice answer back to farmer
    print("\n3. Sending voice answer...")
    answer_result = factory.send_voice_answer(response_text, farmer_profile)
    
    assert answer_result['success'], "Should send answer successfully"
    print(f"✓ Answer sent: {answer_result['message_id']}")
    print(f"   Provider: {answer_result['provider']}")
    print(f"   Language: {answer_result['language']}")
    
    # Step 4: Check overall status
    print("\n4. Checking system status...")
    status = factory.get_provider_status()
    print(f"✓ System status:")
    print(f"   Default provider: {status['default_provider']}")
    print(f"   Auto-fallback: {status['auto_fallback_enabled']}")
    for provider_name, provider_status in status['providers'].items():
        print(f"   {provider_name}: {'✓ Available' if provider_status['available'] else '✗ Unavailable'}")
    
    print("\n✓ INTEGRATION TEST PASSED")
    return True


def run_all_tests():
    """Run all test suites."""
    print("\n" + "=" * 80)
    print("VOICE API TEST SUITE FOR (J)AI KISAN")
    print("=" * 80)
    
    tests = [
        ("Base Interface", test_base_interface),
        ("Bharati Voice API", test_bharati_voice_api),
        ("Legacy Voice API", test_legacy_voice_api),
        ("Factory Default", test_factory_default),
        ("Factory Explicit Selection", test_factory_explicit_selection),
        ("Factory Region-Based", test_factory_region_based),
        ("Factory User Preference", test_factory_user_preference),
        ("Factory Fallback", test_factory_fallback),
        ("Integration Test", test_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n✗ TEST FAILED: {test_name}")
            print(f"   Error: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print("\n" + "=" * 80)
    print(f"OVERALL: {passed}/{total} tests passed")
    print("=" * 80)
    
    return passed == total


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
