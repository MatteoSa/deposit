# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:12:56 2023

@author: matsa
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,101)
y=x**2
print(x)
print(y)

plt.plot(x,y)
plt.title("Graph of x^2 vs x")
plt.show()


x=np.linspace(0,3*np.pi,500)
plt.plot(x, np.sin(x**2))
plt.title("A simple chirp")


x=np.linspace(-2,2,101)
y=x**2
plt.plot(x)
plt.show()


x=np.linspace(-2,2,101)
y=x**2
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.title("Chart Title")
plt.plot(x,y)
plt.show()



x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y, label="x**2")
y2=x**4
plt.plot(x,y2, label="x**4")
plt.legend()
plt.show()


a=int(input("Enter an integer value"))
x=np.linspace(-1,1,a)
y=np.cos(2*np.pi*x)
plt.title("Body function cos(2pix)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.savefig("cos2pix.png")
plt.show()


a=int(input("Enter an integer value"))
x=np.linspace(-1,1,a)
y=np.cos(2*np.pi*x)
plt.plot(x,y, label="cos (2pix)")
y2=np.sin(2*np.pi*x)
plt.plot(x,y2, label="sin(2pix)")
plt.title("")
plt.legend()
plt.savefig("trigonometric.png")
plt.show()


a=int(input("Enter an integer value"))
x=np.linspace(0,4,a)
y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()


number=int(input("How many value do you want ?"))
x=np.linspace(2,10,number)
temp=float(input("What is the temperature in Kelvin?"))
p=(0.08206*temp)/x
plt.xlabel("Molar value (L/mol)")
plt.ylabel("Pressure (atm)")
plt.title("Isotherm (ideal gas)")
plt.savefig("isotherm.jpg")
plt.plot(x,p)
plt.show()


n=int(input("Enter a number of points"))
a=int(input("Enter a number of temperature"))
r=0.08206
plt.xlabel("Vm")
plt.ylabel("p")
x=np.linspace(2,10,n)
for i in range (a):
    t=int(input("Enter a temperature in kelvin"))
    plt.plot(x,r*t/x,label=t)
plt.title("Isotherms(ideal gas)")
plt.savefig("isotherms.jpg")
plt.legend()
plt.show()


n=int(input("How many value do you want ?"))
min=int(input("minimal value ?"))
max=int(input("maximal value ?"))
x0=float(input("X0 ?"))
s=float(input("s ?"))
x=np.linspace(min,max,n)
y=np.exp(-0.5*(((x-x0)**2)/s**2))/(2*np.pi)**0.5
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian function")
plt.plot(x,y)
plt.show()


a=int(input("Enter an integer value"))
x=np.linspace(0,3,a)
y=np.exp(-x)
plt.plot(x,y, label="e-x")
y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y2, label="sin(3pix)e-x")
plt.title("Functions")
plt.legend()
plt.show()


n=int(input("How many value do you want ?"))
courb=int(input("How many graph do you want ?"))
min=int(input("minimal value ?"))
max=int(input("maximal value ?"))
plt.xlabel("x")
plt.ylabel("f(x)")
x=np.linspace(min,max,n)
for i in range (courb):
    x0=float(input("X0 ?"))
    s=float(input("s ?"))
    y=np.exp(-0.5*(((x-x0)**2)/s**2))/(2*np.pi)**0.5
    plt.plot(x,y,label="x0={} ,s={}".format(x0,s))
plt.title("Gaussian function")
plt.savefig("gaussianes.png")
plt.legend()
plt.show()



