'''
Practice Problems Assignments
9/23/21
'''

# 1) Name
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
print(lastName + ", " + firstName)

# 2) 100 years
name = input("What is your name? ")
age = float(input("How old are you? "))
print(name + ", you will turn 100 in the year " + str(2021+(100-age)))

# 3) Remainder
num1 = float(input("What is the number you want to divide? "))
num2 = float(input("What is the number you want to divide by? "))
print(str(num1) + " divided by " + str(num2) + " will leave a remainder of " + str(num1%num2))

# 4) Replication
word = input("Give me a word: ")
num = int(input("How many times do you want me to print it? "))
print((" " + word)*num)

# 5) Rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
print("The perimeter of your rectangle is " + str(((2*length) + (2*width))) + " units.  The area is " + str((length*width)) + " units squared.")

# 6) Circle
import math
diameter = float(input("What is the diameter of the circle? "))
print("The circumference is " + str(2*math.pi*(diameter/2)) + " units and the area is " + str(math.pi*(diameter/2)**2) + " units squared")

# 7) Birthday
year = int(input("What year were you born in? "))
print("Since you were born in " + str(year) + ", you are probably " + str(2021-year) + " years old.")

# 8) Square
root = float(input("Enter a number for me to square: "))
print(str(root) + " squared is " + str(root**2))

# 9) Hours
hours = float(input("Enter the number of hours: "))
print(str(hours) + " hours is " + str(hours*3600) + " seconds")