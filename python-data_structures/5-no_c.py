#!/usr/bin/python3

def no_c(my_string):
    """
    Remove todos os caracteres 'c' e 'C' de uma string sem usar str.replace().
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
