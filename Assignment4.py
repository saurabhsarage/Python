#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:53:30 2019

@author: saurabh


Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
j=0
for i in range(1,11):
  if i < 6:
    for j in range(1,i):
      print(j,end="")
  else:
    for j in range(1,i):
      print(j-1,end="")
  print()