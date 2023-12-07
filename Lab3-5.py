#######################################################
# Name:       Raymond Bryant Jr.
# Class:      CIS-1400
# Assignment: Week 4 Homework
# File:       Lab 3-5.py
# Purpose:    This program will guess the secrets using
# statements in Python.
#######################################################

# The main function
def main():
    print('Guess the Secrets')

# This module allows user to enter age
def getAge(age):
    age = input(int("Please enter age: "))
    if age <= 25:
        print("Congratulations, the age is 25 or less! ")
        return age

# This module allows user to enter weight
def getWeight(weight):
    weight = input(int("Please enter weight: "))
    if weight >= 128:
        print("Congratulations, the weight is 128 or more! ")
        return weight

# This module allows user to enter birth month
def getMonth(birthMonth):
    birthMonth = input(string("Please enter birth month: "))
    if birthMonth == 'April':
        print("Congratulations, the birth month is April! ")
        return birthMonth

# This module displays correct answers
def correctAnswers(age, weight, birthMonth):
    print("The correct age is: ", age)
    print("The correct weight is: ", weight)
    print("The correct birth month is: ", birthMonth)

# The main module called
main()
