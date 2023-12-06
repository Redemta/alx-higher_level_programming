#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()
    uniq_sum = 0
    for num in my_list:
        if num not in uniq_int:
            uniq_int.add(num)
            uniq_sum += num
    return uniq_sum
