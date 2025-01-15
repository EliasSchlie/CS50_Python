import pytest
from numb3rs import validate

def test_words():
    assert validate("hallo") == False
    assert validate("not an ip") == False

def test_correct():
    assert validate("1.1.1.1") == True
    assert validate("255.0.225.8") == True

def test_false_num():
    assert validate("275.3.6.28") == False
    assert validate("255.0.67.256") == False

def test_false_alpha():
    assert validate("25.3a.6.28") == False
    assert validate("255.e.67.256") == False

def test_wrong_length():
    assert validate("25.6.28") == False
    assert validate("255.52.67.25.6") == False
