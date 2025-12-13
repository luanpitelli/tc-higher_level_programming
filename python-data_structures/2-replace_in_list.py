#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Substitui um elemento de uma lista em um índice específico (idx)
    pelo elemento fornecido. Retorna a lista original se o índice for inválido.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
