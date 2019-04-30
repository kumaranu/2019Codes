import random
import sys
import os

print("Hello World")

name = "\nDerek"
print(name)

print("\n2 + 3 - 4 * 5 =", 2+3-4*5)

grocery_List = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print(grocery_List)

#print("Second element of grocery list is",grocery_List[1])
#print ("First to third items in grocery list are",grocery_List[0:3])

grocery_List.append('Apples')
print (grocery_List)

grocery_List.insert(1,'Milk')
print (grocery_List)

age = 15

if age > 16:
    print ("You are old enough to drive")
else:
    print ("You are not old enough to drive")

if age >= 21:
    print ("You are old enough to drive")
elif age >=16:
    print ("You are old enough to drive a car")
else:
    print ("You are not old enough to drive")

def addNumber(a, b):
    sumNum = a+b
    return sumNum
print (addNumber(1,5))