"""
Write a program to find two string Anagram or Not.
Date: 21/12/23
"""
def anagram(string1, string2):
    return sorted(string1) == sorted(string2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if anagram(string1, string2):
    print("The two strings are anagram of each other.")
else:
    print("The two strings are not anagram of each other.")