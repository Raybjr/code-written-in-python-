#######################################################
# Name:       Raymond Bryant Jr.
# Class:      CIS-1400
# Date:       02/14/21
# Assignment: Lab 2-7
# File:       Lab 2-7.py
# Description: A retail company must file a monthly sales tax report listing the total sales for the month and the
# amount of state and county sales tax collected.
# The state sales tax rate is 4 percent and the county sales tax rate is 2 percent.
# This program uses functions and variables
#######################################################
def main():
    print('Welcome to the Tax Calculator Program ')
    print() #prints a blank line
    totalSales = inputData()
    cTax = calcCounty(totalSales)
    sTax = calcState(totalSales)
    total = calcTotal(cTax, sTax)
    printTotal(totalSales, cTax, sTax, total)


#Prompts user to input data
def inputData():
    totalSales = input('Enter the total number of sales for the month: ')
    totalSales = float(totalSales)
    return totalSales

#Calculate County Tax
def calcCounty(totalSales):
    cTax = totalSales * .02
    return cTax

#Calculate State Tax
def calcState(totalSales):
    sTax = totalSales * .04
    return sTax

#Calculate Total Tax
def calcTotal(cTax, sTax):
    total = cTax + sTax
    return total

#Print Totals
def printTotal(totalSales, cTax, sTax, total):
    print('Number of Total Sales ', totalSales)
    print('County Tax ', cTax)
    print('State Tax ', sTax)
    print('Total with Taxes ', total)

#Main Function Called
main()
