"""
Write a program to reverse middle words of string.
Date: 21/12/23
"""
def reverse_middle_words(string):
	words = string.split()              
	n = len(words)
	if n <= 1:
		return string
	else:
		words[1:-1] = [w[::-1] for w in words[1:-1]]
		return ' '.join(words)

string = "Hi how are you python"           
print("The original string is: ",string)  
print("The string with reversed middle word is: ",reverse_middle_words(string))