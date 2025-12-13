#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Imprime uma matriz (lista de listas) de inteiros.
    """
    for row in matrix:
        for i, integer in enumerate(row):
            print("{:d}".format(integer), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
