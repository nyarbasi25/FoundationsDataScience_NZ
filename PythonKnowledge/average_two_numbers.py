#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:59:24 2021

A function finding average of two numbers

@author: nyarbasi
"""

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
def average(num1, num2):
    return (num1 + num2) / 2.0

avg=average(num1,num2)
print(avg) 