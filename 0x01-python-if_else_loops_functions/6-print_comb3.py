#!/usr/bin/python3
for first_number in range(0, 9):
    for second_number in range(first_number + 1, 10):
        if first_number != 8:
            print("{}{}".format(first_number, second_number), end=", ")
