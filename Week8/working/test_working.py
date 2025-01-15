import pytest
from working import convert

def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 8:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 8:60 PM")

def test_3():
    assert convert("9:01 AM to 5:01 PM") == "09:01 to 17:01"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"