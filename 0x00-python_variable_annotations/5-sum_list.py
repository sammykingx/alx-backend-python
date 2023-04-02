#!/usr/bin/env python3


'''A module for returning the sum of a list'''


def sum_list(input_list: list[float]) -> float:
    '''A function thst returns the sum of a list'''

    total = 0.0
    for i in input_list:
        total += i
    return total


if __name__ == '__main__':
    sum_list = __import__('5-sum_list').sum_list

    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}"
          .format(floats_sum, type(floats_sum)))