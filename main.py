def add_numbers(a, b):
    return a + b


def hello_world():
    return "Hello World : 10"


def mortgage(p, r, n):
    x = r / (12 * 100)
    r = 1 + x
    r1 = r ** n
    m = p * x * r1 / (r1 - 1)
    return round(m)


if __name__ == "__main__":
    print(add_numbers(50, 50))
    print(add_numbers(100, -10))
    print(hello_world())
    print(mortgage(800000, 6, 103))
