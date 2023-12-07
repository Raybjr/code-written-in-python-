#######################################################
# Name:       Raymond Bryant Jr.
# Class:      CIS-1400
# Assignment: Week 4 Homework
# File:       Lab 3-4.py
# Purpose:    This program will demonstrate how to use decision
# statements in Python.
#######################################################
# This program determines if a bonus should be awarded

# The main function
def main():
    print('Welcome to the program')
    monthlySales = getSales()  # gets sales
    isBonus(monthlySales)
    dayOff(monthlySales)


# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales

# This function determines if a bonus should be awarded
def isBonus(monthlySales):
    if monthlySales >= 100000:
        print("You have earned a $5,000 bonus!!!")
        return monthlySales

# This bonus determines if a bonus and a day off should be awarded
def dayOff(monthlySales):
    if monthlySales > 110000:
        print("You have earned a $5,000 bonus!!!")
        print("All employees get one day off!!!")
        return monthlySales

# calls main
main()
