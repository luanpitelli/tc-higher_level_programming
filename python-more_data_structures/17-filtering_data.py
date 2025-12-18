#!/usr/bin/python3
def filtering_data(a_dictionary):
    high_earners = filter(lambda x: x['salary'] > 10000, a_dictionary)
    return list(map(lambda x: x['name'], high_earners))
