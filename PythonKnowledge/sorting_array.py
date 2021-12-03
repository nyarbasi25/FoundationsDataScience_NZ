#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:06:16 2021

Finding sorted array

@author: nyarbasi
"""

#Initialize array     
array = [6,7,4,7,2];     
k = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(array)):    
    print(array[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(array)):    
    for j in range(i+1, len(array)):    
        if(array[i] > array[j]):    
            k = array[i];    
            array[i] = array[j];    
            array[j] = k;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(array)):    
    print(array[i], end=" "); 