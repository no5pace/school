'''
Isaac Longo
Calculator
1/14/22
'''

# define the functions
def add(a, b):
	return (a + b)
	
def sub(a, b):
	return (a - b)
	
def mult(a, b):
	return (a * b)
	
def div(a, b):
	return (a / b)

def gcf(a, b):
	temp = None
	for i in range(a, 0, -1):
		if (a % i == 0):
			temp = i
		for j in range(b, 0, -1):
			if (b % j == 0 and temp == j):
				return temp

def exp(a, b):
	return (a**b)
	
# calculator loop logic
while (True):
	# print the menu and get input
	print("1) addition\n2) subtraction\n3) multiplication\n4) division\n5) greatest common factor\n6) exponent\n")
	a = int(input("First number: "))
	b = int(input("Second number: "))
	op = int(input("Which operation (number)? "))
	
	# calculator logic
	if (op == 1):
		print(f"\nThe result of the operation {a} + {b} is {add(a, b)}\n")
	elif (op == 2):
		print(f"\nThe result of the operation {a} - {b} is {sub(a, b)}\n")
	elif (op == 3):
		print(f"\nThe result of the operation {a} * {b} is {mult(a, b)}\n")
	elif (op == 4):
		print(f"\nThe result of the operation {a} / {b} is {div(a, b)}\n")
	elif (op == 5):
		print(f"\nThe greatest common factor of {a} and {b} is {gcf(a, b)}\n")
	elif (op == 6):
		print(f"\nThe result of the operation {a}^{b} is {exp(a, b)}\n")