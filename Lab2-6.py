#######################################################
# Name:       Raymond Bryant Jr.
# Class:      CIS-1400
# Date:       02/14/21
# Assignment: Lab 2-6
# File:       Lab 2-6.py
# Description: Write a program that will calculate a 20% tip and a 6% tax on a meal price.
# The user will enter the meal price and the program will calculate tip, tax, and the total.
# The total is the meal price plus the tip plus the tax.
#######################################################
# This program uses functions and variables

# the main function
def main():
    print('Welcome to the meal calculator program')
    print()   #prints a blank line
    mealprice = input_meal()
    tip = calc_tip(mealprice)
    tax = calc_tax(mealprice)
    total = calc_total(mealprice, tip, tax)
    print_info(mealprice, tip, tax, total)

# this function will input meal price
def input_meal():
    mealprice = input('Enter the meal price $')
    mealprice = float(mealprice)
    return mealprice

# this function will calculate tip at 20%
def calc_tip(mealprice):
    tip = mealprice * .20
    return tip

# this function will calculate tax at 6%
def calc_tax(mealprice):
    tax = mealprice * .06
    return tax

# this function will calculate tip, tax, and the total # cost
def calc_total(mealprice, tip, tax):
    total = mealprice + tip + tax
    return total

# this function will print tip, tax, the mealprice,
# and the total
def print_info(mealprice, tip, tax, total):
    print('The meal price is $', mealprice)
    print('The tip is $', tip)
    print('The tax is $', tax)
    print('The total is $', total)

# Main Function Called
main()
