# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:00:43 2023

@author: matsa
"""

num=int(input("Enter an integer value"))
while num >0:
    res=num//3
    print("The integer division of {} by 3 gives {}".format(num, res))
    num=int(input("Enter an integer value"))
    
    
print("We are done")

num=int(input("Enter an integer value"))
ndiv=1
while ndiv<num:
    res=num//ndiv
    print("The integer division of {} by {} gives {}".format(num,ndiv,res))
    ndiv=ndiv+1

print("We are done")
print("Total number of divisions {}".format(ndiv))


num=1
ndiv=0
while num>0 and num<211:
    if num%3==0:
        print(f"The number is {num}")
    num=num+1
    ndiv=ndiv+1
print("Total number of iteration {}".format(ndiv))
print("We are done")

sum=0
i=10
while i>0:
    sum=sum+i
    i=i-1
print("The sum is {}".format(sum))

sum=0
i=10
while i>0:
    num=int(input("Enter a value"))
    sum=sum+num
    i=i-1
res=sum/10.0
print("The average is {}".format(res))
    
res=1
num=int(input("Enter an integer value"))
a=num
while num>0:
    res=res*num
    num=num-1
print("The factorial of {} is {}".format(a,res))

name='Jesaa29Roy'
size=len(name)
i=-1
while i<size-1:
    i=i+1
    if not name[i].isalpha():
        continue
    print(name[i],end=' ')

n=int(input("Enter the value of n "))
for i in range (n):
    q_i=i**2
    print(q_i)