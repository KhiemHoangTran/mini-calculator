def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("6 / 2 =", divide(6, 2))
    print("6 / 0 =", divide(6, 0))