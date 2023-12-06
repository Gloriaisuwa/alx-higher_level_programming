#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    value = 0
    d_val = 0
    for tup in my_list:
        value += (tup[0] * tup[1])
        d_val += (tup[1])
    return (value/d_val)
