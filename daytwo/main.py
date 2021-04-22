import string


def trim_hello_world():
    return "Hello World"[8]


def slice_string():
    return "thinker"[2:5]


def sammy():
    return "Sammy"[2:]


def to_set():
    return set("Mississippi")


def palindrome(inputs):
    response = list()
    for str_input in inputs:
        str_input = ''.join(c for c in str_input if c not in string.punctuation).lower()
        result = 'Y' if (str_input == str_input[::-1]) else 'N'
        response.append(result)
    return response


def my_list():
    return [1, "my word", 0.5]


def my_nested_list():
    return [2, my_list()]


def list_slice():
    return ['a', 'b', 'c'][1:]


def dict_week():
    my_dict = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7,
    }

    return my_dict


def list_in_dict():
    D = {
        'k1': [1, 2, 3]
    }
    return D


def add_to_set():
    my_set = to_set()
    my_set.add("X")
    return my_set


def dup_in_set():
    return set([1, 1, 2, 3])


def div_by_7_not_5():
    my_set = set()
    for num in range(2000, 3200):
        if num % 5 == 0:
            continue
        if num % 7 == 0:
            my_set.add(num)
    return my_set


def get_factorial(num):
    if num == 0:
        return 1
    return num * get_factorial(num - 1)


def my_factorials(nums):
    result = list()
    for num in nums:
        result.append(get_factorial(num))
    return result


def my_integrals(num):
    return {i: i ** 2 for i in range(1, num + 1)}


if __name__ == "__main__":
    print(trim_hello_world())
    print(slice_string())
    print(sammy())
    print(to_set())
    print(palindrome({"tacoca't", "tacocan't"}))
    print(my_list())
    print(my_nested_list())
    print(list_slice())
    print(dict_week())
    print(list_in_dict()['k1'][1])
    print(to_set().add("X"))
    print(add_to_set())
    print(dup_in_set())
    print(div_by_7_not_5())
    print(my_factorials({8, 7, 6}))
    print(my_integrals(8))
