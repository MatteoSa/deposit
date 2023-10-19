# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:35:45 2023

@author: matsa
"""

import numpy as np
a=np.array([1,2,3],dtype='int')
print(a)
print(np.random.randint(-4,8, size=(3,3)))
print(np.identity(5))


arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


arr=np.array([[1,0,1]])
print(arr)

r1=np.repeat(arr,3,axis=0)
print(r1)

r1[1,1]=2
print(r1)


output.zeros((5,5))
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4]=z
print(output)


f=np.random.randint(-10,10,size=(4,4))
print(f)
print(np.min(f))
print(np.min(f,axis=0))
sum(f)


stats=np.array([[-1,2,3],[4,5,0]])
stats


arr=np.array([[2,0,1]])
r1=np.repeat(arr,3,axis=1)
print(r1)


import numpy
npoints=12
values=numpy.linspace(-2.0,2.0,npoints)
print(values)


import numpy as np
y=np.linspace(10,30,21)
y[4]=1
print (y)





