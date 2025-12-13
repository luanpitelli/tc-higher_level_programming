#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Encontra o maior inteiro de uma lista sem usar a função max() embutida.
    Retorna None se a lista estiver vazia.
    """
    if not my_list:
        return None
    max_value = my_list[0]
    for integer in my_list[1:]:
        if integer > max_value:
            max_value = integer
    return max_value
