import pytest
from um import count

def test_1():
    assert count("um, I'm um not sure äm.") == 2
    assert count("um") == 1
    assert count("um um") == 2

def test_too_many():
    assert count("uh this is jummy") == 0
    assert count("ummy jummy jum") == 0

def test_punctutation():
    assert count("um. um, um: um; um? um!") == 6

def test_case():
    assert count("UM um Um uM") == 4
