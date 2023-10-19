# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:16:51 2023

@author: matsa
"""

#TD6 
#for i in range (1,n+1,2):

#Accumulation becarful start with 1!=0
sum=0
for i in range (6):
    sum=sum+i
    print(f"The value of the sum is :{sum}")
print("The final value is {}".format(sum))

for i in range(4):
    for j in range (3):
        print("i= {} , j= {}".format(i,j))

n=int(input("Enter an integer value"))
sum=0
for i in range (n+1):
    sum=sum+i
print("The sum is {}".format(sum))

n=int(input("Enter an integer value"))
sum=0
for i in range (1,n+1):
    sum=sum+((i+1)/(i**2))
print("The sum of i+1/i**2 is {: .2f}".format(sum))

n=int(input("Enter a positive number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("The factorial of {} is {}".format(n,fact))

for i in range (1,10):
    for j in range (1,10):
        print("{}{}".format(i,j))

for i in range (1,10):
    for j in range (1,10):
        if i!=j:
            print("{}{}".format(i,j))
            
a=int(input("Enter the number of triangular numbers you want"))
for i in range(a+1):
    t=i*(i+1)/2
    print(t)
    
for i in range (1,10):
    for j in range (1,10):
        for k in range(1,10):
            print("{}{}{}".format(i,j,k))
            
            
for i in range (0,10):
    for j in range (0,10):
        for k in range(0,10):
            if i+j+k==22:
                print("{}{}{}".format(i,j,k))
                
for i in range (0,10):
    for j in range (0,10):
        for k in range(0,10):
            if i**3+j**3+k**3==i*100+j*10+k:
                print("{}{}{}".format(i,j,k))
                
n=int(input("Enter a positive number"))
for i in range (1,n+1):
    if n%i==0:
        print("{}".format(i))
        
n=int(input("Enter an integer number"))
sum=0
a=0
for i in range (0,n):
    a=2*i+1
    print(a)
    sum=sum+a
print(sum)

n=int(input("Enter an integer value"))
rep=True
for i in range (2,(n+1//2)+1):
    if n%i==0:
        rep=False
if rep==True:
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
    

