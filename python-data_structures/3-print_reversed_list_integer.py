#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Imprime todos os inteiros em uma lista em ordem inversa.
    """
    if my_list:
        for integer in my_list[::-1]:
            print("{:d}".format(integer))
