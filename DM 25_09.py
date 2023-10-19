# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:24:45 2023

@author: matsa
"""

#Exo 1
dico={
      'H': {'Atomic Number': 1, 'Melting point': 14, 'Boiling point': 20},
      'He': {'Atomic Number': 2, 'Melting point': 1, 'Boiling point': 4},
      'Li': {'Atomic Number': 3, 'Melting point': 453, 'Boiling point': 1603},
      'Be': {'Atomic Number': 4, 'Melting point': 1560, 'Boiling point': 2742},
      'B': {'Atomic Number': 5, 'Melting point': 2349, 'Boiling point': 4200},
      'C': {'Atomic Number': 6, 'Melting point': 3915, 'Boiling point': 3915},
      'N': {'Atomic Number': 7, 'Melting point': 63, 'Boiling point': 77},
      'O': {'Atomic Number': 8, 'Melting point': 54, 'Boiling point': 90},
      'F': {'Atomic Number': 9, 'Melting point': 53, 'Boiling point': 85},
      'Ne': {'Atomic Number': 10, 'Melting point': 25, 'Boiling point': 27}}

name=str(input("What is the symbol of your element ? "))
temp=float(input("What is the temperature of your element in °C ? "))
temp=temp+273.15
if dico[name]['Boiling point']==temp and dico[name]['Melting point']==temp:
    print("Your element is between the melting and the boiling point")
elif dico[name]['Melting point']>temp:
    print ("Your element is a solid")
elif dico[name]['Melting point']<=temp and dico[name]['Boiling point']>temp:
    print ("Your element is a liquid")
else:
    print("Your element is a gaz")
    
    
#Exo 2
dico_bank={
    'ANZ': {'Year 1 & 2': 2.3/100, 'Year 3 onwards': 4.1/100},
    'Bank of Australia': {'Year 1 & 2': 0.1/100, 'Year 3 onwards': 5/100},
    'Commonwealth Bank': {'Year 1 & 2': 3.5/100, 'Year 3 onwards': 3.8/100},
    'Westpac': {'Year 1 & 2': 3.7/100, 'Year 3 onwards': 3.7/100}}

name=str(input("What is your bank ?"))
time=int(input("What is the time in month of your mortgage ?"))
total=0.0
if time<=24:
    for i in range (time):
        total=total+(dico_bank[name]['Year 1 & 2']/12)
else:
    total=2*dico_bank[name]['Year 1 & 2']
    for i in range (time-24):
        total=total+(dico_bank[name]['Year 3 onwards']/12)
        
print("Your total rate is {}".format(total))
    



