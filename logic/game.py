import random


def generate_integer(n, divisor=False):
    """Generate a pseudo random number with n digits."""
    if n == 1 and divisor == True:
        return random.randrange(1, 10)
    if n == 1:
        return random.randrange(10)
    if n > 1:
        return random.randrange(10 ** (n - 1), 10**n)

def digits(n):
    """Calculate the number of digits depending on the level, and return it for two numbers."""
    m = 1
    if (n + m) % 2 == 0:
        n = m = (n + m) // 2
    else:
        m = n // 2
        n = m + 1
    return n, m

def addition(level):
    """Generate an addition expression and its result."""
    a, b = digits(level)
    x, y = generate_integer(a), generate_integer(b)
    return {"expression": f"{x} + {y}", "result": str(x + y)}

def subtraction(level):
    """Generate an substraction expression and its result."""
    a, b = digits(level)
    x, y = generate_integer(a), generate_integer(b)
    return {"expression": f"{x} - {y}", "result": str(x - y)}

def multiplication(level):
    """Generate an multiplication expression and its result."""
    a, b = digits(level)
    x, y = generate_integer(a), generate_integer(b)
    return {"expression": f"{x} * {y}", "result": str(x * y)}

def division(level):
    """Generate an division expression and its result."""
    a, b = digits(level)
    x, y = generate_integer(a), generate_integer(b, True)
    while x % y != 0:
        x = generate_integer(a)
        y = generate_integer(b, True)
    return {"expression": f"{x} / {y}", "result": str(x // y)}