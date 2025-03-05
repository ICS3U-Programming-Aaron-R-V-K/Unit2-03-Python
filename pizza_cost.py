#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: Feb 27, 2025
# The code calculates and displays the area and perimeter
# of a pizza for a given user input
# Then calculates the total price of the pizza with tax
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches):"))

    # process
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL + constants.INGREDIENTS * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
