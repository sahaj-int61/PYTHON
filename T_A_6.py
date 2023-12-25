"""
Write a program which can accept a number and return the nearest palindromenumber.
Date: 21/12/23
""" 
def test(n):
     result = 0
     while n:
          if str(n-result)==str(n-result)[::-1]:
              return n-result
          elif str(n+result)==str(n+result)[::-1]:
              return n+result
          result+=1

n = 123000
print("Original number: ", n)
print("Closest Palindrome number of the said number: ",test(n))