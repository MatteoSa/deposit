# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:24:56 2023

@author: matsa
"""

a=2
b=3
area=a*b
print("The area of the edge rectangle {} and {} is {}". format (a,b,area))


r=10
h=3
pi=3.14
v=(pi*h*r**2)/3
print("The volume is ",v)

num1=float(input("Enter a numerical value :"))
num2=float(input("Enter another numeric value:"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1,num2,sum))
print("the product of {} and is {}".format(num1,num2,product))


num1=float(input("Enter a temperature : "))
print("The temperature is {} °K".format(num1+273.15))


num=float(input("Enter the length :"))
area=6*num*num
volume=num*num*num
print("The {}cm edge cube has an area of {}cm2 and a volume of {}cm3".format(num,area,volume))


num1=int(input("Numbers of tickets of 10 euros ?"))
num2=int(input("Numbers of tickets of 20 euros ?"))
num3=int(input("Numbers of tickets of 50 euros ?"))
sum=num1*10+num2*20+num3*50
print("The user has {} euros".format(sum))


num=float(input("Radius ?"))
import math as m
length=2*m.pi*num
area=m.pi*num**2
print("The length is {}cm, circumference {}cm and the volume {}cm2".format(num,length,area))


import math
num1=float(input("First lenght "))
num2=float(input("Second lenght "))
angle=float(input("Angle ?"))
angle=math.radians(angle)
c=math.sqrt(num1**2+num2**2-2*num1*num2*m.cos(angle))
print("The third side is {}".format(c))