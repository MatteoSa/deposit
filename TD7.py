# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:51:58 2023

@author: matsa
"""

file=[]
value="1"
sum=0
while value!="":
    value=input("Enter a value")
    if value=="":
        print("The list is stopped")
    else :
        value=float(value)
        file.append(value)
        sum=sum+value
        
average=sum/(len(file))
print("The mean is {}".format(average))


names=input("Enter some names separated by spaces")
list_names=names.split(" ")
for name in list_names:
    print("Hi "+name)
print("Welcome all of you ")


element=['H','C','N','O','S','Cl']
atomic_mass=[1.008,12.011,14.007,15.999,32.065,35.453]
sum=0
for i in range (0,6):
    a=int(input("Number of {} in your molecule".format(element[i])))
    sum=sum+a*atomic_mass[i]
print("Your molecule have a mass of {}".format(sum))


degree=int(input("Maximum degree of your function ?"))
liste=[]
for i in range(0,degree+1):
    coef=float(input("What is the coefficient of degree {}".format(i)))
    liste.append(coef)
value=float(input("What is your value of x ?"))
answer=0
answer=answer+liste[0]
for i in range(1,degree+1):
    answer=answer+(liste[i]*(value**i))
print("At the point {} the value is {}".format(value,answer))


