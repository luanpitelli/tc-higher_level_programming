#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    if not a_dictionary:
        return 0, 0
    total_age = reduce(lambda x, y: x + y['age'], a_dictionary, 0)
    total_salary = reduce(lambda x, y: x + y['salary'], a_dictionary, 0)
    count = len(a_dictionary)
    return total_salary / count, total_age / count
