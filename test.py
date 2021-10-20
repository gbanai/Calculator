from Code.calculator import Calculator
"""Calculator class testing"""
test_obj = Calculator()

def test_addition():
    assert test_obj.reset() == 0
    assert test_obj.addition(5) == 5
    assert test_obj.addition(5) == 10
    assert test_obj.addition(-9.5) == 0.5
    assert test_obj.addition('5') == 0.5

def test_subtraction():
    assert test_obj.reset() == 0
    assert test_obj.subtraction(5) == -5
    assert test_obj.subtraction(-20) == 15
    assert test_obj.subtraction(5.5) == 9.5
    assert test_obj.subtraction('12') == 9.5

def test_multiplication():
    assert test_obj.reset() == 0
    assert test_obj.addition(5) == 5
    assert test_obj.multiplication(2) == 10
    assert test_obj.multiplication(0) == 0
    assert test_obj.addition(10) == 10
    assert test_obj.multiplication(-2) == -20
    assert test_obj.multiplication(1.5) == -30
    assert test_obj.multiplication('four') == -30

def test_division():
    assert test_obj.reset() == 0
    assert test_obj.addition(5) == 5
    assert test_obj.division(2) == 2.5
    assert test_obj.division(0) == False
    assert test_obj.division(1.25) == 2
    assert test_obj.division('2') == 2

def test_root():
    assert test_obj.reset() == 0
    assert test_obj.addition(81) == 81
    assert test_obj.root(2) == 9
    assert test_obj.multiplication(-1) == -9
    assert test_obj.root(3) == False