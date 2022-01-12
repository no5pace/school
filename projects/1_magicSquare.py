'''
Magic Square
Assigned: 9/30/21
'''

# title and prompt
print("Welcome to Magic Square")
num = input("Enter an integer from 21 to 65: ")

# check if the input is a digit using the isdigit() function
if (num.isdigit()):
	# if it is, then convert to an integer
	num = int(num)
	
	# check if given number is within the range
	if (num < 21 or num > 65):
		# if it isn't, then quit
		print(str(num) + " is outside of the range")
	else:
		# if it is, then make the magic square
		print("You have entered " + str(num) + "\n\nHere is your Magic Square:\n")
		
		# print the magic square (\t instead of spaces to have even spacing)
		# line 1
		print(str(num - 20) + "\t" + str(1) + "\t" + str(12) + "\t" + str(7))
		
		# line 2
		print(str(11) + "\t" + str(8) + "\t" + str(num - 21) + "\t" + str(2))
		
		# line 3
		print(str(5) + "\t" + str(10) + "\t" + str(3) + "\t" + str(num - 18))
		
		# line 4
		print(str(4) + "\t" + str(num - 19) + "\t" + str(6) + "\t" + str(9))
else:
	# if it isn't, then quit
	print(num + " is not an integer")