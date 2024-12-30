import pytest
from fuel import gauge
from fuel import convert

def test_convert():
    assert convert("1/1") == 100
    assert convert("1/5") == 20
    assert convert("2/4") == 50

def test_convert_error():
    with pytest.raises(ValueError): 
        convert("0")
    with pytest.raises(ValueError): 
        convert("cat")
    with pytest.raises(ValueError): 
        convert("cat/dog")
    with pytest.raises(ValueError): 
        convert("1")
    with pytest.raises(ZeroDivisionError): 
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_gauge_percent():
    assert gauge(40) == "40%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"

