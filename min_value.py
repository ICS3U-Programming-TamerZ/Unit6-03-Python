#!/usr/bin/env python3

# Created by: Tamer Zreg
# Created on: Dec 20, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the smallest value


import random


# function calculates the min value in the list of elements
def find_min_value(random_nums):

    min = random_nums[0]

    # calculate the min value
    for counter in random_nums:
        if min > counter:
            min = counter

    return min


def main():
    # initializing counter
    counter = 0

    # declaring variable
    random_nums_user = []

    # displays random numbers and calculates average
    for counter in range(0, 10):
        random_nums_user.append(random.randint(0, 100))
        print(
            "{} added to the list at "
            "position {}".format(random_nums_user[counter], counter)
        )

    min_user = find_min_value(random_nums_user)
    print("")
    print("The min value is: {}".format(min_user))


if __name__ == "__main__":
    main()
