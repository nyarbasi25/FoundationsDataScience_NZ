#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:08:18 2021


maximum of two numbers
@author: nyarbasi
"""

# Python program to find the
# maximum of two numbers


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
print(maximum(a, b))



# or 


maximum = max(a, b)
print(maximum)