'''
Do Now
10/20/21
'''

# get input
age = int(input("How old are you? "))
resident = int(input("How long have you been a resident of the US? "))
citizen = input("Are you a natural born citizen? Yes or no. ")

# check individually first to display what requirements they don't meet later
if (not age >= 35):
	print("False: you are not 35 years old")
	
if (not resident >= 14):
	print("False: you have not been a resident for 14 years")

if (not citizen.lower() == "yes"):
	print("False: you are not a natural born citizen")

# check all to see if they qualify for the presidency
if (age >= 35 and resident >= 14 and citizen.lower() == "yes"):
	print("True")


# with nested conditionals
age = int(input("How old are you? "))
if (age >= 35):
	resident = int(input("How long have you been a resident of the US? "))
	if (resident >= 14):
		citizen = input("Are you a natural born citizen? Yes or no. ")
		if (citizen.lower() == "yes"):
			print("True")
		else:
			print("False: you are not a natural born citizen")
	else:
		print("False: you have not been a resident for 14 years")
else:
	print("False: you are not 35 years old")