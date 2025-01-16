import pytest
from jar import Jar

def test_Jar_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_Jar_assign():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_Jar_fill():
    jar = Jar(10)
    jar.deposit(10)
    assert jar.size == 10

def test_Jar_fill_and_take():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0

def test_Jar_print():
    jar = Jar(10)
    jar.deposit(5)
    cookies = str(jar)
    assert cookies == "🍪🍪🍪🍪🍪"

def test_Jar_take_too_many():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(10)

def test_Jar_deposit_too_many():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)