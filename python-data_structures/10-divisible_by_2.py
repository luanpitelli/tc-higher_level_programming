#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Retorna uma nova lista com True ou False, indicando se o inteiro
    na mesma posição na lista original é divisível por 2.
    """
    new_list = [num % 2 == 0 for num in my_list]
    return new_list
