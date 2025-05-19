import pytest # type: ignore
from app import decode_url, check_google_safe_browsing, check_ssl_certificate

# Test for decode_url function
def test_decode_url():
    encoded_url = "aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20="  # Base64 for "https://www.example.com"
    assert decode_url(encoded_url) == "https://www.example.com"

    invalid_encoded_url = "invalid_base64"
    assert decode_url(invalid_encoded_url) == "invalid_base64"  

# Test for check_google_safe_browsing function 
def test_check_google_safe_browsing(monkeypatch):
    def mock_safe_browsing_api(url):
        return url != "http://phishingsite.com"

    monkeypatch.setattr("app.check_google_safe_browsing", mock_safe_browsing_api)

    assert check_google_safe_browsing("http://safe-site.com") == True
    assert check_google_safe_browsing("http://phishingsite.com") == False

# Test for check_ssl_certificate function 
def test_check_ssl_certificate(monkeypatch):
    def mock_ssl_check(url):
        return url.startswith("https")  

    monkeypatch.setattr("app.check_ssl_certificate", mock_ssl_check)

    assert check_ssl_certificate("https://secure-site.com") == True
    assert check_ssl_certificate("http://insecure-site.com") == False
