#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) is None):
        return (0)

    avg = 0
    weight = 0

    for tup in my_list:
        avg += (tup[0] * tup[1])
        weight += tup[1]

    return (avg / weight)
