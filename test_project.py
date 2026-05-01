from logic.game import (
    generate_integer,
    digits,
    addition,
    subtraction,
    multiplication,
    division,
)


def test_digits():
    assert digits(1) == (1, 1)
    assert digits(4) == (3, 2)
    assert digits(5) == (3, 3)
    assert digits(10) == (6, 5)


def test_generate_integer():
    num = generate_integer(3)
    assert isinstance(num, int)
    assert 100 <= num <= 999


def test_addition():
    result = addition(3)
    expr = result["expression"]
    value = int(result["result"])

    x, y = map(int, expr.split(" + "))
    assert x + y == value


def test_subtraction():
    result = subtraction(3)
    expr = result["expression"]
    value = int(result["result"])

    x, y = map(int, expr.split(" - "))
    assert x - y == value


def test_multiplication():
    result = multiplication(3)
    expr = result["expression"]
    value = int(result["result"])

    x, y = map(int, expr.split(" * "))
    assert x * y == value


def test_division():
    result = division(3)
    expr = result["expression"]
    value = int(result["result"])

    x, y = map(int, expr.split(" / "))
    assert y != 0
    assert x % y == 0
    assert x // y == value