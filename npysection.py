# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""""Numpy section"""
import numpy as np
import scipy

a = np.array([1, 2, 3])
a = [1,2,3]
print(a+a)
print(a*3)

e = np.array([[1,2],[3,4]])
c = np.array([[1,2,3],[0,0,1],[2,0,0]])
d = np.array([[2,0,0],[0,2,0],[0,0,2]])

f = np.array([10,20])
def syslin(M,b):
    invM = np.linalg.inv(M)
    print(invM @ b)
    
    

syslin(e,f)
