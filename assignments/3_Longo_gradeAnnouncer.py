'''
Grade Announcer
10/25/21
'''

# get input
grade = float(input("What is your number grade? "))

# large disgusting if statement
if (grade >= 97 and grade <= 100):
	print("You have an A+, and you’re an amazing CS student!")
elif (grade >= 95 and grade < 97):
	print("You have an A, and you’re a great CS student!")
elif (grade >= 90 and grade < 95):
	print("You have an A-, and you’re a good CS student!")
elif (grade >= 87 and grade < 90):
	print("You have an B+, and you’re an above average CS student!")
elif (grade >= 85 and grade < 87):
	print("You have an B, and you’re an average CS student!")
elif (grade >= 80 and grade < 85):
	print("You have an B-, and you’re a slightly below average CS student!")
elif (grade >= 77 and grade < 80):
	print("You have an C+, and your CS grade needs a boost.")
elif (grade >= 75 and grade < 77):
	print("You have an C, and your CS grade needs a big boost.")
elif (grade >= 70 and grade < 75):
	print("You have an C-, and your CS grade needs a huge boost.")
elif (grade >= 65 and grade < 70):
	print("You have an D, and you're almost failing CS.")
elif (grade >= 0 and grade < 65):
	print("You have an F, and you're failing CS.")
else:
	print("That's not a valid number grade.")