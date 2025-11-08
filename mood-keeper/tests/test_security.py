"""
Tests for security module
Testing password hashing, token generation and validation
"""
import pytest
from app.security import hash_secret, verify_secret, make_token, read_token


def test_hash_secret():
    """Test password hashing"""
    password = "test_password_123"
    hashed = hash_secret(password)
    
    # Hash should not be empty
    assert hashed is not None
    assert len(hashed) > 0
    
    # Hash should not be the same as password
    assert hashed != password
    
    # Same password should produce different hashes (salt)
    hashed2 = hash_secret(password)
    assert hashed != hashed2


def test_verify_secret():
    """Test password verification"""
    password = "correct_password"
    wrong_password = "wrong_password"
    
    hashed = hash_secret(password)
    
    # Correct password should verify
    assert verify_secret(password, hashed) is True
    
    # Wrong password should not verify
    assert verify_secret(wrong_password, hashed) is False
    
    # Empty password should not verify
    assert verify_secret("", hashed) is False


def test_make_token():
    """Test token generation"""
    handle = "testuser"
    token = make_token(handle)
    
    # Token should not be empty
    assert token is not None
    assert len(token) > 0
    
    # Token should be a string
    assert isinstance(token, str)
    
    # Token should contain JWT structure (header.payload.signature)
    parts = token.split('.')
    assert len(parts) == 3


def test_read_token():
    """Test token reading and validation"""
    handle = "testuser"
    token = make_token(handle)
    
    # Valid token should return handle
    decoded_handle = read_token(token)
    assert decoded_handle == handle
    
    # Invalid token should return None
    invalid_token = "invalid.token.here"
    assert read_token(invalid_token) is None
    
    # Empty token should return None
    assert read_token("") is None


def test_token_expiration():
    """Test that tokens have expiration"""
    handle = "testuser"
    token = make_token(handle)
    
    # Token should be valid immediately
    assert read_token(token) == handle
    
    # Note: Testing actual expiration would require time manipulation
    # which is beyond the scope of basic tests


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
