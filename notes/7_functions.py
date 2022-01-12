'''
Isaac Longo
Functions
1/10/22
'''

'''
Modules and Functions:

Some modules that are available -
	* math
	* random
	* ...

To import a modules, use the import keyword with the name of the module
More than one modules can be imported by separating the names with commas
'''

# import random and math
from random import *
from math import *

# generate a random n between 1 and 10
print(randint(1,10))

# print pi
print(pi)

'''
A funciton is like a program within a program
Functions serve as shortcuts to avoid repeating code

First you have to define it, and then you must call it
'''

# create a function to print "hello"
def hello():
	print("hello")
hello()

# create a function to print a personal greeting
name = input("What is your name? ")
def personal(name):
	print(f"Hello {name}")
personal(name)

# create a function that finds the area of a rectangle
l = float(input("Length: "))
w = float(input("Width: "))
def area(l, w):
	print(f"The area of a {l}x{w} rectangle is {l*w}")
area(l, w)

# loop to determine the areas of a bunch of random rectangles
num = int(input("Number of rectangles: "))
for i in range(num):
	l = randint(1, 25)
	w = randint(1, 25)
	area(l, w)

'''
Functions with Return Values:

Funciton can return a value that can be used by the rest of the program
Consists of:
	* the return keyword
	* the value or expression that should be returned
'''

# write a function that finds the radius of a circle given the diamater
d = float(input("What is the diameter of the circle? "))
def radius(d):
	return d/2
r = radius(d)
print(f"The radius of a cirle with diameter {d} is {r}")

# use this info to find the area
a = pi * (r**2)
print(f"The area of this cirlce is {a}")

# ^^^ but as a function
def cArea(r):
	a = pi * (r**2)
	return a
	
# loop to find the area of many circles
num = int(input("Number of circles: "))
for i in range(num):
	d = randint(1, 100)
	r = radius(d)
	a = cArea(r)
	print(f"The radius of a circle with diameter {d} is {r}, and the area is {a}")

# write a program that mimics a magic 8 ball
def magic8ball(n):
	if n == 1:
		return "It is certain"
	elif n == 2:
		return "Yes"
	elif n == 3:
		return "No"
	elif n == 4:
		return "Reply is hazy, try again"
	elif n == 5:
		return "It's not looking good"
	elif n == 6:
		return "Never"
	elif n == 7:
		return "For sure"
	elif n == 8:
		return "It is decidedly so"
	elif n == 9:
		return "Maybe"
input("What is your question? ")
print(magic8ball(randint(1, 9)))