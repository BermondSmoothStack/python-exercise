def func():
    print("Hello World")


def func1(name):
    print("Hi my name is {}".format(name))


def func3(x, y, z):
    if z:
        return x
    else:
        return y


def func4(x, y):
    return x * y


def is_even(x):
    return x % 2 == 0


def is_greater(x, y):
    return x > y


def which_even(*args):
    return [x for x in args if x % 2 == 0]


def zigzag_str(x):
    lst = list(x.upper())
    return ''.join([c.lower() if i % 2 == 0 else c for i, c in enumerate(lst)])


def give_num_back(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return y - 1 if x > y else x - 1
    else:
        return x + y


def start_string(x, y):
    return x[0].lower() == y[0].lower()


def double(x):
    return x**2


def cap_first_fourth(x):
    return ''.join([c.upper() if i == 0 or i == 3 else c for i, c in enumerate(x)])


def get_bookshop():
    return [
        {
            "order_number": 34587,
            "book_title_and_author": ("Learning Python", "Mark Lutz"),
            "quantity": 4,
            "price_per_item": 40.95
        },
        {
            "order_number": 98762,
            "book_title_and_author": ("Programming Python", "Mark Lutz"),
            "quantity": 5,
            "price_per_item": 56.80
        },
        {
            "order_number": 77226,
            "book_title_and_author": ("Head First Python", "Paul Barry"),
            "quantity": 3,
            "price_per_item": 32.95
        },
        {
            "order_number": 88112,
            "book_title_and_author": ("Einführung in Python3", "Bernd Klein"),
            "quantity": 3,
            "price_per_item": 24.99
        }
    ]


def get_bookshop_lst2():
    return [
        34587,
        (1, 4, 40.95),
        98762,
        (2, 5, 56.80),
        77226,
        (3, 3, 32.95),
        88112,
        (4, 3, 24.99)
    ]


def bookshop_get_order_price():
    return [(shop["order_number"],
             (lambda x, y: x * y if x * y > 100 else (x * y) + 10)(shop["price_per_item"], shop["quantity"])) for shop
            in get_bookshop()]


def get_order_amount():
    lst = get_bookshop_lst2()
    return [(lst[i], lst[i + 1][1]) for i in range(0, len(lst), 2)]


def get_bmi(x, y):
    return x / y ** 2


def evaluate_bmi(x):

    if x < 18.5:
        return "underweight"
    elif 18.5 <= x < 25:
        return "normal"
    elif 25 <= x < 30:
        return "overweight"
    else:
        return "obesity"


def process_bmi_line(*args):
    lst = list()
    for i in range(1, args[0] * 2, 2):
        lst.append(evaluate_bmi(get_bmi(args[i], args[i + 1])))
    return lst


if __name__ == "__main__":
    '''
    #8
    '''
    func()
    func1("google")
    print(func3(1, 2, 0))
    print(func4(4, 5))
    print(is_even(1))
    print(is_greater(100, 1000))
    print(which_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(zigzag_str("test"))
    print(give_num_back(3, 3))
    print(give_num_back(3000, 30))
    print(start_string("yes", "Yes"))
    print(start_string("yes", "no"))
    print(double(7))
    print(cap_first_fourth("longword"))
    '''
    #9
    '''
    print(bookshop_get_order_price())
    print(get_order_amount())
    '''
    #10
    '''
    print(process_bmi_line(3, 80, 1.73, 55, 1.58, 49, 1.91))
