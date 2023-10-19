# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:18:52 2023

@author: matsa
"""

#create the dictionnary
country_capitals={"United States": "Washington D.C.",
                  "Italy": "Rome", "England": "London"}
#print the dictionnary
print(country_capitals)


Dict={}
print("Empty dictionnary :")
print(Dict)

Dict=dict({1: 'Greeks', 2: 'For',3: 'Greeks'})
print("\nDictionnary with the use of dict() : ")
print(Dict)

Dict=dict([(1, 'Greeks'), (2, 'For')])
print("\nDictionnary with each items as a pair: ")
print(Dict)


Dict={1: 'Geeks', 2: 'For',
      3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)


my_list={1: "Hello", "Hi": 25, "Howdy":100}
print(1 in my_list)
print("Howdy" not in my_list)
print("Hello" in my_list)


country_capitals={
    "United States": "Washington D.C.",
    "Italy": "Naples"}
for country in country_capitals:
    print(country)
    capital=country_capitals[country]
    print(capital)
    

for keys,values in country_capitals.items():
    print(country_capitals.keys())
    print(country_capitals.values())
    
    
cities=('Paris','Athens','Madrid')
continent='Europe'
my_dictionnary=dict.fromkeys(cities,continent)
print(my_dictionnary)


keys=['Ten', 'Twenty', 'Thirty']
values=[10,20,30]
dico=dict(zip(keys, values))
print(dico)


dict1={'Ten': 10 , 'Twenty': 20, 'Thirty': 30}
dict2={'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
dict1.update(dict2)
print(dict1)
print(dict3)


simpleDict={
    "class" : {
        "student" : {
            "name": "Mike",
            "marks": {
                "Physics": 70,
                "history": 80
                }
            }
        }
    }
print(simpleDict.values)


employees=['Kelly', 'Emma']
defaults={"designation": 'Developer', "salary": 8000}
dict1=dict.fromkeys(employees,defaults)
print(dict1)
print(dict1["Kelly"])


sample_dict={
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"}
sample_dict.pop("name")
sample_dict.pop("salary")
keys=["name", "salary"]
print(sample_dict)


sample_dict={'a':100, 'b':200, 'c':300}
if 200 in sample_dict.values():
    print("200 is a value")
    

sample_dicts={
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary':500}}
sample_dicts['emp3']['salary']=8500
print(sample_dicts)
    

