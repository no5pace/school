'''
Isaac Longo
Period 2
Exception Handling
1/26/22
'''

# error-proof function to find the perimeter of a rectangle

def perimeter(x, y):
	try:
		if (x > 0 and y > 0):
			return (2*x + 2*y)
		else:
			print("Invalid input... pick a positive number")
	except:
		print("Invalid input... pick a positive number")

x = float(input("Length of the rectangle: "))
y = float(input("Height of the rectangle: "))

print(perimeter(x, y))