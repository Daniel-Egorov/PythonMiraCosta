#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Guido van Rossum
# Date:          Sept. 1, 2010
#
# Problem Statement: Ask the user to enter two numbers, calculate the sum of 
# these two numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add two number for you")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input("Enter one whole numbers(Ex. 52): "))
    num2 = eval(input("Enter another whole number(Ex. 41): "))
    num3 = eval(input("Enter another whole number(Ex. 23): "))

    #Here is the processing that is needed
    summed = num1 + num2 + num3
    multiplied = num1 * num2 * num3


    # Output the results
    print("The sum of the three numbers is", summed)
    print("The multiplied result of the three numbers is", multiplied)

main()

