def add(numbers):
    summ = 0
    for num in numbers:
        summ += num
    return summ


def subtract(numbers):
    sub = numbers[0]
    for num in numbers[1:]:
        sub -= num
    return sub


def multiply(num1, num2):
    return num1 * num2

def mult_alot(numbers):
    return reduce(multiply, numbers)


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


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
