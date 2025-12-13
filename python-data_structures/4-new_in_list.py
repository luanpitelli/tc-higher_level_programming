#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Substitui um elemento em uma posição específica em uma CÓPIA da lista.
    Retorna a lista original se o índice for inválido.
    """
    new_list = my_list[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
