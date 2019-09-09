#!/usr/bin/env python3
s = input("Enter a string:")
a = s[::-1]
if s == a:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
