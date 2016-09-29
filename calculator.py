"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
run = True

while run:
    user_input = raw_input('> ')
    tokens = user_input.split(' ')
    args = map(int, tokens[1:])
    if tokens[0] == "q":
        run = False
    elif tokens[0] == "+":
        print add(args[0], args[1])
    elif tokens[0] == "-":
        print subtract(args[0], args[1])
    elif tokens[0] == "*":
        print multiply(args[0], args[1])
    elif tokens[0] == "/":
        print divide(args[0], args[1])
    elif tokens[0] == "square":
        print square(args[0])
    elif tokens[0] == "cube":
        print cube(args[0])
    elif tokens[0] == "pow":
        print power(args[0], args[1])
    elif tokens[0] == "mod":
        print mod(args[0], args[1])
    else:
        print "Bad input"

    
