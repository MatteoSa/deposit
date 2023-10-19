# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:26:57 2023

@author: matsa
"""

Integer=[1,2,3,4]
print(Integer)
smooth=[3.14,7,-2+3j,'water',False,[1,2]]
print(smooth)
print(smooth[:4])
print(smooth[1:])
print(smooth[5][1])
print(smooth[3][4])

chem_sim=["H","Pb","I","F","Cl","Ar","O"]
chem_sim.pop(2)
print(chem_sim.append("He"))

n= int(input("Enter a value of n"))
thelist=[]
for i in range (1,n+1):
    thelist.append(1/i)
Sn=sum(thelist)
print("For n= {} the sum accumulator is equal to {:.2f}".format(n,Sn))

line="Temperature is 298.15 K before combustion"
words=line.split(' ')
print(words)

line=input("Enter, in a single line and separatedby spaces, the desired temperature values")
smooth_txt=line.split()
print("The list is now {}".format(smooth_txt))
temp=[]
for element in smooth_txt:
    value=float (element)
    temp.append(value)
print("The final list is {}".format(temp))

n=int(input("Enter an integer number"))
list=[]
for i in range (1,n+1):
    list.append(i**2)
print("The list is {}".format(list))

stop=True
name=[]
note=[]
while stop==True:
    na=(input("Enter a name : "))
    name.append(na)
    if na=="":
        break
    no=int(input("Enter a number : "))
    note.append(no)
    

sum=0
for i in range (0,len(name)-1):
    sum=sum+note[i]
    print("{}  {}".format(name[i],note[i]))
print("The average is {}".format(sum/(len(name)-1)))



