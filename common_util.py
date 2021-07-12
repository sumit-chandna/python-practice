import random


def print_list(list):
    for data in list:
        print(str(data), end=" ")


def get_divisors(number):
    divisors = []
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            divisors.append(num)
    return divisors


def add_to_list_unique(input1, input2, output):
    for num in input1:
        if num in input2 and num not in output:
            output.append(num)


def add_to_list(input1, input2, output):
    for num in input1:
        if num in input2:
            output.append(num)


def even_list(input_list):
    output_list = []
    for num in input_list:
        if num % 2 == 0:
            output_list.append(num)
    return output_list


def list_ends(a_list):
    return [a_list[0], a_list[len(a_list) - 1]]


def gen_fibonacci():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    elif count > 2:
        fib = [1, 1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib


def list_remove_duplicates(input):
    output = set()
    for num in input:
        output.add(num)
    return output;


def gen_password(password_len):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(s, password_len))
    return password
