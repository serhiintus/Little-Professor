from project import (
    generate_integer, 
    digits, 
    addition, 
    subtraction, 
    multiplication, 
    division,
)
import random


def test_digits():
    assert digits(1) == (1, 1)
    assert digits(4) == (3, 2)
    assert digits(5) == (3, 3)
    assert digits(10) == (6, 5)

def test_generate_integer():
    assert len(str(generate_integer(1))) == 1
    assert len(str(generate_integer(2))) == 2
    assert len(str(generate_integer(3))) == 3

def test_addition_expression():
    random.seed(1000000)
    assert addition(3)["expression"] == "21 + 28"

def test_addition_result():
    random.seed(1000000)
    assert addition(3)["result"] == "49"

def test_subtraction_expression():
    random.seed(1000000)
    assert subtraction(3)["expression"] == "21 - 28"

def test_subtraction_result():
    random.seed(1000000)
    assert subtraction(3)["result"] == "-7"

def test_multiplication_expression():
    random.seed(1000000)
    assert multiplication(3)["expression"] == "21 * 28"

def test_multiplication_result():
    random.seed(1000000)
    assert multiplication(3)["result"] == "588"

def test_division_expression():
    random.seed(1000000)
    assert division(3)["expression"] == "28 / 28"

def test_division_result():
    random.seed(1000000)
    assert division(3)["result"] == "1"