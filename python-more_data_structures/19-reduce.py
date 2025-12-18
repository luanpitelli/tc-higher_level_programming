#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return 0, 0
    # Somamos os valores extraindo-os de cada dicionário 'y'
    total_age = reduce(lambda x, y: x + y.get('age', 0), a_dictionary, 0)
    total_salary = reduce(lambda x, y: x + y.get('salary', 0), a_dictionary, 0)
    count = len(a_dictionary)
    return total_salary / count, total_age / count
