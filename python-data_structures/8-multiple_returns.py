#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Retorna uma tupla com o comprimento de uma string e seu primeiro caractere.
    Se a string estiver vazia, o primeiro caractere deve ser None.
    """
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
