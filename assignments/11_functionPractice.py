'''
Isaac Longo
Period 2
Function Practice
1/12/22
'''

# define the function
def squareArea(s):
	area = s**2
	return area

# loop with call to the function
num = int(input("Number of squares: "))
for i in range (num):
	s = float(input(f"What is the sidelength of square #{i+1}? "))
	print(f"The area of a square with sidelength {s} is {squareArea(s)}\n")