'''
Isaac Longo
Exception Handling
1/25/22
'''

'''
Exceptions must be caught and dealt with in the program or else the program will crash
This is done with "try" and "except"
'''

# create a function that needs 2 numbers
def divide(x, y):
	return x / y

# error proofing for user inputs
while (True):
	try:
		x = float(input("Enter a number: "))
		y = float(input("Enter another number: "))
		# error proofing for zero division
		try:
			print(divide(x, y))
			break
		except:
			print("That division is not allowed\n")
	except:
		print("You did not enter valid numbers\n")

'''
Where might there be errors?
	* dividing by zero
	* integers not given for x and y

Try/Except:
	* program will "try" the try block, and if an error is thrown, then the except block will run
	* specific types of errors can also be specified after the "except"
'''

# program to ask the user how many ketchup packets they want
'''
What could cause an error:
	* entering characters
	* entering a negative number
	* entering a float
'''

while (True):
	try:
		packets = int(input("How many ketchup packets do you want? "))
		if (packets < 0):
			print("Invalid input... please enter a positive integer\n")
		else:
			print(f"You ordered {packets} packets")
			break
	except:
		print("Invalid input... please enter a positive integer\n")