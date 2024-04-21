# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:03:10 2024

@author: UltimateStarCoder
"""
import math


def divide_or_square (number):
    if (number % 5) == 0:
        return "{:.2f}".format(math.sqrt(number))
    else:
        return number % 5

print(divide_or_square(10))
print(divide_or_square(7))



"""
Extra Challenge
"""

def longest_value (args):
    my_iter = iter(args.values())
    for value in my_iter:
        next_value = next(my_iter, None)
        if len(value) >= len(next_value):
            return value
        else:
            return next_value
         
dictionary = {'fruit':'apple','color':'green'}
dictionary2 = {'fruit':'apple','color':'greenlight'}     
print(longest_value(dictionary))
print(longest_value(dictionary2))