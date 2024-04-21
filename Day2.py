# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:45:31 2024

@author: UltimateStarCoder
"""
def convert_add(args):
    convert = [int(arg) for arg in args]
    return sum(convert)

str_numbers = ['1', '2','3']

print (convert_add(str_numbers))



"""
Extra Challenge
"""


def check_duplicates (args):
    duplicate_value = [];
    counter = 1
    for value in args:
        for duplicates in args[counter:(len(args) + 1)]:
            if value == duplicates and value not in duplicate_value:
                duplicate_value.append(value)
        counter += 1
    if duplicate_value:
        return duplicate_value
    else:
        return "no duplicates"

fruits = ['apple', 'orange', 'banana','apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', "Mark"]

print (check_duplicates(fruits))
print (check_duplicates(names))  