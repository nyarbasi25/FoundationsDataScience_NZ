# -*- coding: utf-8 -*-
"""
This is a moving average filter with window size of 3 for a random array.
"""

import numpy as np

x=np.random.randint(10, size=(7))
x1=np.array([1,2,5,7,9])

print(x1)

def MoveAvg3(InArry):
    length=len(InArry)
    OutArry=np.zeros(length)
    OutArry[0]=InArry[0]
    OutArry[1]=0.5*(InArry[0]+InArry[1])
    for i in range(2,length):
        print(i)
        OutArry[i]=(InArry[i-2]+InArry[i-1]+InArry[i])/3
        
    print (OutArry)
    
MoveAvg3(x1)
