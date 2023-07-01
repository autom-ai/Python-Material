# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:20:37 2023

@author: Mini Einstein
"""
"""
number=[5,2,5,2,2]
for i in number:
    temp=''
    for j in range(i):
        temp+='x'
    print(temp)

list_num=[1,2,3,4,5,6]
max_num=0
for i in list_num:
    if i > max_num:
        max_num=i
print(max_num)

list_num=[1,2,3,4,5,6,2,2,2]
list_num1=[]
for i in list_num:
    if i not in list_num1:
        list_num1.append(i)
print(list_num1)

phone_number=input("enter phone number please")
digit={
       "1":"one",
       "2":"two",
       "3":"three",
       "4":"four",
       "5":"five",
       "6":"six",
       "7":"seven",
       "8":"eight",
        "9":"nine",
        "10":"ten"
       }
output=""
for i in phone_number:
    output+=digit.get(i, '!')+" "
print(output)

class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'hi {self.name} talk')
obj=Person("farhan")
obj.talk()
    
"""
import random
class Dice:
    def roll(self):
        first= random.randint(1,6)
        second= random.randint(1,6)
        print(first, second)
obj=Dice()
obj.roll()