#!/usr/bin/bash


'''A module that returns a function'''


from typing import Callable

'''
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by a float'''
    return lambda k: k * multiplier
'''

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier

if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
