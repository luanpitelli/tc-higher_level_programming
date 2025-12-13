#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Imprime todos os inteiros em uma lista.
    """
    for integer in my_list:
        # Usa str.format() para imprimir o inteiro
        print("{:d}".format(integer))
