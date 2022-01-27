'''
Isaac Longo
Period 2
Exception Handling
1/26/22
'''

# function to find the perimeter of a rectangle (no error proofing)
def perimeter(x, y):
	return (2 * (x + y))

# error proofed here
while (True):
	try:
		x = float(input("Length of the rectangle: "))
		y = float(input("Height of the rectangle: "))
		
		if (x > 0 and y > 0):
			print(perimeter(x, y))
			break
		else:
			print("Invalid input... pick a positive number\n")
	except:
		print("Invalid input... pick a positive number\n")