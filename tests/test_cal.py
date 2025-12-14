from src.calculator import Calculator
import pytest

def test_cal_add():
    assert Calculator.add(5,10)==15
    assert Calculator.add(-75,10)==-65
    assert Calculator.add(10,10)==20

def test_cal_sub():
    assert Calculator.sub(5,10)==-5
    assert Calculator.sub(-75,10)==-85
    assert Calculator.sub(10,10)==0

def test_cal_multiply():
    assert Calculator.multiply(5,10)==50
    assert Calculator.multiply(-75,10)==-750
    assert Calculator.multiply(10,0)==0

def test_cal_div():
    assert Calculator.div(10,5)==2
    assert Calculator.div(75,10)==7.50
    with pytest.raises(ZeroDivisionError):
        assert Calculator.div(10,0)