#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program checks if a person chose the right number between 0 and 9

import random


def main():
    # This function checks if the person chose right or wrong

    # Input

    chosen_number = input("Enter a number between 0 and 9: ")
    generated_number = random.randint(0, 9)  # A number between 0 and 9
    print("")

    # process
    try:
        if generated_number == int(chosen_number):
            # Output
            print("Correct!")
        else:
            print("The correct number is {}".format(generated_number))
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
