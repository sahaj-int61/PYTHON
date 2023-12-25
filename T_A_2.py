"""
Write a program to swap comma and dot in string.
Date: 21/12/23
"""
number = "32.054,23"
swap = number.maketrans
number = number.translate(swap(',.','.,'))
print(number)