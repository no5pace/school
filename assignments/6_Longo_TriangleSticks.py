'''
Isaac Longo
Period 2
Triangle Sticks
10/27/21

Purpose: To write a program to determine whether or not a triangle is possible given 3 side lengths.
'''

# get input
a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))

# check if all pairs of side lengths are larger than the remaining side length
if (a + b > c and a + c > b and b + c > a):
	print("These side lengths will form a triangle")
else:
	print("These side lengths will not form a triangle")