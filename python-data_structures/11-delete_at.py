#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Exclui o item em uma posição específica (idx) em uma lista.
    Retorna a mesma lista se o índice for inválido.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
