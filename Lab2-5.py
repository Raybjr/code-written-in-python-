#######################################################
# Name:       Raymond Bryant Jr.
# Class:      CIS-1400
# Date:       02/14/21
# Assignment: Lab 2-5
# File:       Lab 2-5.py
# This program demonstrates how to use variables and
# functions.
#######################################################
# This program uses functions and variables

# the main function
def main():
    print('Welcome to the variable program')
    print()   # prints a blank line
    name = inputName()
    age = inputAge()
    print('Hello', name)
    print('Your age is',  age)

# this function allows user to input their name
def inputName():
    name = input('Enter your name: ')
    return name

# this function allow user to input their age
def inputAge():
    age = input('Enter your age: ')
    return age

# calls main
main()

