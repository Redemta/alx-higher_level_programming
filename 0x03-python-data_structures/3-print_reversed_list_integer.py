#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_length = len(my_list)
    if my_list is None:
        return
    for i in range(list_length - 1, -1, -1):
        print("{:d}".format(my_list[i]))
