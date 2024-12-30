import pytest
from plates import is_valid

def test_is_valid_too_long():
    assert is_valid("H1") == False
    assert is_valid("HEN1111") == False

def test_is_valid_no_letter_in_front():
    assert is_valid("1111") == False
    assert is_valid("E1185") == False

def test_is_valid_leter_in_end():
    assert is_valid("EE11E") == False
    assert is_valid("EE1E11") == False

def test_is_valid_start_with_0():
    assert is_valid("EE011") == False
    assert is_valid("EE01") == False

def test_is_valid_characters():
    assert is_valid("EE&111") == False
    assert is_valid("ËA11") == False
    assert is_valid("EE11.") == False

def test_is_valid():
    assert is_valid("EE11") == True
    assert is_valid("EE1") == True
    assert is_valid("EE111") == True