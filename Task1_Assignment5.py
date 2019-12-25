#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:07:18 2019

@author: saurabh

Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA
"""

inp = input("Enter String :- ")
print("Original String - ",inp)

rev = inp[::-1]
print("Reverse Of the String :- ",rev)
