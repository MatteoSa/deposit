# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:33:35 2023

@author: matsa
"""

name=open("names.txt")
for nom in name:
    print("Hello {}".format(nom))
print(name)  


name=open("names.txt")
for nom in name:
    nom=nom.strip()
    print("Hello {}".format(nom))
    
    
f_names=open("names.txt")
for name in f_names:
    if "a" in name:
        name=name.strip()
        print("Hello {}".format(name))
    
        
#f=open("names.txt","r")
f=open("names.txt","w")
#f=open("names.txt","a")
#f=open("names.txt","r+")
print(f.name)
print(f.mode)


with open("test.txt","r") as f:
    pass


with open("test.txt","r") as f:
    f_contents=f.read()
    print(f_contents)
    
    
with open("test.txt","r") as f:
    f_contents=f.readlines()
    print(f_contents)


with open("test.txt","r") as f:
    f_contents=f.readline()
    print(f_contents)
    f_contents=f.readline()
    print(f_contents)
    f_contents=f.readline()
    print(f_contents)



with open("test.txt","w") as f:
    f.write("Test")
    f.seek(2)
    f.write("--")
    
    
with open("test.txt","r") as rf:
    with open("test_copy.txt","w") as wf:
        for line in rf:
            wf.write(line)
            

with open("python.png","r") as rf:
    with open("python_copy.png","w") as wf:
        for line in rf:
            wf.write(line)
            
            
with open("test2.txt","w") as f:
    val='names'
    val1='10'
    val2='niamh'
    f.write(val+'\n'+val1+'\n'+val2)
    f.seek(0)
    f.write("Test")
    f.seek(6)
    f.write('z')
            
            
            


    
    

    






