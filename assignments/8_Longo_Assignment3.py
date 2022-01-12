'''
Isaac Longo
Period 2
Python Basics Assignment 3
12/2/21
'''

# 1
for i in range(0,6+1):
	if (i%3 != 0 or i == 0):
		print(i)

print("")

# 2
for i in range(1,50+1):
	output = ""
	if (i%3 == 0):
		output += "Fizz"
	if (i%5 == 0):
		output += "Buzz"
	if (output == ""):
		print(i)
	else:
		print(output)

print("")

# 3
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if (a + b >= 15 and a + b <= 21):
	print(20)
else:
	print((a + b))
	
print("")

# 4
x = int(input("Enter side length: "))
y = int(input("Enter side length: "))
z = int(input("Enter side length: "))

if (x == y and y == z):
	print("This triangle is equillaterial")
elif (x == y and y != z):
	print("This triangle is isocele")
elif (x != y and y != z):
	print("This triangle is scalene")

print("")

# 5
msg = input("Enter a message: ")
rep = int(input("How many times do you want it to repeat? "))
for i in range(0,rep):
	print(msg)

print("")

# 6
import math
rad = 6
print(f"The volume of a sphere with radius 6 is {(4/3)*math.pi*rad**3}")

print("")

# 7
a = int(input("First integer: "))
b = int(input("Second integer: "))
high = 0
if (a >= b):
	high = a
else:
	high = b
while(True):
	if (high % a == 0 and high % b == 0):
		print(f"LCM is {high}")
		break
	high += 1

print("")

# 8
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
add = 0
for i in range(start,end+1):
	add += i
print(f"The sum of the series {start}-{end} is {add}")

print("")

# 9
add = 0
for i in range(1,1000):
	if (i%3 == 0 or i%5 == 0):
		add += i
print(f"The sum of all multiples of 3 and 5 under 1000 is {add}")