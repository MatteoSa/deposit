# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:20:39 2023

@author: matsa
"""

message='good morning'
print(message[:-1])

num=int(input("Enter the number :"))
if num%2==0:
  print("The number {} is an even number".format(num))
else:
  print(f"The number {num} is an odd number")
  
marks=float(input("Enter your marks : "))
if marks<40:
  print("The student has failed and got a F grade")
elif marks>=40 and marks<50:
  print("The student has passed marginaly and got a E grade")
elif marks>=50 and marks <75:
  print("The student has passed with a C grade")
elif marks>=75 and marks<=90:
  print("The student has done well and has scored B grade")
else :
  print("The student has done excellent and passed with Distinct")
  
  
weigh=float(input("Enter your weigh in kg"))
length=float(input("Enter your length in meters"))
BMI=weigh/length**2
if BMI<18.5:
  print("Underweigh with {} BMI".format(BMI))
elif BMI>=18.5 and BMI <25:
  print("Normal with {} BMI".format(BMI))
elif BMI>=25 and BMI <30:
  print("Overweigh with {} BMI".format(BMI))
else:
  print("Obesity with {} BMI".format(BMI))
  
  
temp=input("Input the temperature you like to convert ? (e.g., 45F, 10C)")
degree=int(temp[:-1])
i_convention=temp[-1]

if i_convention.upper()=="C":
  result=int(round((9*degree)/5+32))
  o_convention="Fahrenheit"
elif i_convention.upper()=="F":
  result=int(round((degree-32)*5/9))
  o_convention="Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees")


n1=int(input("Enter a natural number"))
n2=int(input("Enter another natural number"))
if n1%n2==0:
  result=n1//n2
  print("The numbers are divisibles and the result is ",result)
else :
  result=n1%n2
  print("The numbers aren't divisibles and the rest is", result)


n=int(input("Enter the unit"))
if n<=100:
  print("The bill is 0")
elif n>100 and n<=200:
  n2=n-100
  price=5*n2
  print("The bill is ", price)
else:
  n2=n-200
  price=n2*10+500
  print("The bill is ", price)
  
  