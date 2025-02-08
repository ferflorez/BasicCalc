import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(1, 5) == -4

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
