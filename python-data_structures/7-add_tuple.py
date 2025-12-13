#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Retorna uma tupla com a soma dos dois primeiros elementos
    de cada tupla (tuple_a e tuple_b).
    Se uma tupla tiver menos de 2 elementos, o valor ausente é 0.
    Se uma tupla tiver mais de 2 elementos, apenas os 2 primeiros são usados.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
