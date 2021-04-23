import random


def crowd_test(room):
    if len(room) == 0:
        print("The room is empty")
    elif len(room) > 5:
        print("This is a mob")
    elif len(room) > 2:
        print("The room is crowded")
    else:
        print("The room has space")


def my_room():
    room = ["Jenny", "Benny", "Henny", "Lenny"]
    crowd_test(room)
    room.pop()
    room.pop()
    crowd_test(room)
    room.append("Danny")
    room.append("Billy")
    room.append("Sonny")
    room.append("Ginny")
    crowd_test(room)
    room.pop()
    room.pop()
    room.pop()
    room.pop()
    room.pop()
    room.pop()
    crowd_test(room)


def div_by_7_and_5():
    lst = list()
    for num in range(1500, 2700):
        if (num % 7 == 0) & (num % 5 == 0):
            lst.append(num)
    return lst


def temp_conversion(fc, cf):
    c = (fc * 1.8) + 32
    f = (cf - 32) * (5 / 9)
    print("{}°C is {:.0f} in Fahrenheit".format(fc, c))
    print("{}°F is {:.0f} in Celsius".format(cf, f))


def guess_number():
    num = random.randrange(1, 9)
    usr_input = input("Please guess the number: ")
    while int(usr_input) != num:
        usr_input = input("Please guess the number again: ")
    print("Congratulations, you guessed the number!")


def triangle(num):
    for i in range(1, num + 1):
        star = '*'
        print(star * i)
    for j in range(num - 1, 0, -1):
        star = '*'
        print(star * j)


def reverse(usr_str):
    return usr_str[::-1]


def odd_even_count(lst):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [odd, even]


def type_check_list(data):
    lst = list()
    for d in data:
        lst.append(type(d))
    return lst


def no_3_or_6():
    nums = ''
    for i in range(1, 6):
        if i == 6 or i == 3:
            continue
        nums += ('{} '.format(i))
    return nums


if __name__ == "__main__":
    print("Day three: ")
    my_room()
    print(div_by_7_and_5())
    temp_conversion(60, 45)
    guess_number()
    triangle(5)
    print(reverse("Hello world"))
    print(odd_even_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11]))
    print(type_check_list([1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]))
    print(no_3_or_6())
