'''
Can I or Can't I Ride the Rollercoaster?
10/27/21
Group Members:
	Isaac Longo, Kamari Hampton, Andrew Fernandes
'''

# get input
height = float(input("What is your height in inches? "))
age = float(input("What is your age? "))
quarters = int(input("How many quarters do you have? "))
PASS = input("Do you have the frequent rider pass (yes or no)? ")

# check if they have enough money
if ((PASS.lower() != 'yes' and quarters >= 4) or (PASS.lower() == 'yes' and quarters >= 2)):
	# check if they are tall enough OR old enough for the loophole
	if (height > 50 or age > 18):
		print("You can ride")
	else:
		print("You can't ride")
else:
	print("You can't ride")