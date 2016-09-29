def add(num1, num2):
    return num1 + num2

"""def add(numbers):
    summ = 0
    for num in numbers:
        summ += num
    return summ"""

def my_reduce(my_function, my_list):
    result = my_list[0]
    for i in range(1,len(my_list)):
        result = my_function(result, my_list[i])
    return result


def add_multiple(numbers):
    return my_reduce(add, numbers)

def sub(num1, num2):
    return num1 - num2

def sub_multiple(numbers):
    return my_reduce(sub, numbers)


"""def subtract(numbers):
    sub = numbers[0]
    for num in numbers[1:]:
        sub -= num
    return sub"""


def multiply(num1, num2):
    return num1 * num2

def multiply_multiple(numbers):
    return my_reduce(multiply, numbers)


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 

def divide_multiple(numbers):
    return my_reduce(divide, numbers)


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
