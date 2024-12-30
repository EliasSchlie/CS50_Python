import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("hEllO you") == 0

def test_value_h_start():
    assert value("Hi") == 20
    assert value("holla my friend") == 20

def test_value_no_h():
    assert value("Greetings") == 100
    assert value("What's up?") == 100

def test_value_num():
    assert value("1") == 100