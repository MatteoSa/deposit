# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:36:02 2023

@author: matsa
"""

def my_function(fname="Luis",lname="xyz"):
    print(fname+" "+lname)
my_function("Emil")


def f(a,b):
    if(a>b):
        print("{} est plus grand que {}".format(a,b))
    elif (a==b):
        print("Les deux nombres sont égaux")
    else:
        print("{} est plus grand que {}".format(b,a))
f(2,2)


def function():
    liste=[]
    for i in range (5):
        a=int(input("Enter a number : "))
        liste.append(a)
    print("the list created was {}".format(liste))
    min=liste[0]
    max=liste[0]
    for i in range (1,5):
        if liste[i]<min:
            min=liste[i]
        if liste[i]>max:
            max=liste[i]
    print("the largest number is {} and the smallest is {}".format(max,min))
function()

try:
    num=float(input("Enter a number : "))
except ValueError as e:
    print(e)
else :
    if (num%2)==0:
        print("{0} is even".format(num))
    else:
        print("{0} is odd".format(num))


while True:
    try:
        num=int(input("Enter a number : "))
        if (num%2)==0:
            print("{0} is even".format(num))
            break
        else:
            print("{0} is odd".format(num))
            break
    except ValueError as e:
            print(e)
            

while True:
    try:
        num=int(input("Enter a number : "))
        for i in range(2,num):
            if (num%i)==0 and num>0:
                print("{0} is not prime".format(num))
                break
            else:
                print("{0} is prime".format(num))
                break
    except ValueError as e:
            print(e)
            
