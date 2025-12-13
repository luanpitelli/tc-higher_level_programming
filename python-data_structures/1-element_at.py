#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Recupera um elemento de uma lista em um índice específico.
    Retorna None se o índice for negativo ou estiver fora do alcance.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
