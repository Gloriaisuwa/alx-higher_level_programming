#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = []

    try:
        for i in range(list_length):
        try:
            if (isinstance(my_list_1[i], (int, float))
                    and isinstance(my_list_2[i], (int, float))):
                count.append(my_list_1[i] / my_list_2[i])
            else:
                count.append(0)
                print("wrong type")
        except ZeroDivisionError:
            count.append(0)
            print("division by 0")
        except IndexError:
            count.append(0)
            print("out of range")
    finally:
        return count
