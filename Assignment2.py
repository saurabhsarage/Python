#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:40:11 2019

@author: saurabh

Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""
import math
d = 12
r = d/2
V = (4/3)*math.pi*r*r*r
print("Volume of Sphere : - ",V)