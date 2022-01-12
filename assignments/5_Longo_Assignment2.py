'''
Isaac Longo
Period 2
Python Basics Assignment 2
11/10/21
'''

# 1) F ot C
far = float(input("What is the temperature in Faranheit? "))
cel = (5.0/9.0) * (far - 32)
print("Celcius: " + str(cel))

# 2) C ot F
cell = float(input("What is the temperature in Celcius? "))
far = cel / (5.0/9.0) + 32
print("Faranheit: " + str(far))

# 3) vowel
letter = input("Input a letter: ")
if (letter == 'a'):
	print(letter + " is a vowel.")
elif (letter == 'e'):
	print(letter + " is a vowel.")
elif (letter == 'i'):
	print(letter + " is a vowel.")
elif (letter == 'o'):
	print(letter + " is a vowel.")
elif (letter == 'u'):
	print(letter + " is a vowel.")
elif (letter == 'y'):
	print(letter + " is sometimes a vowel.")
else:
	print(letter + " is a consonant.")

# 4) month
month = input("Input a month: ").lower()
if (month == "april" or month == "june" or month == "september" or month == "november"):
	print(month + " has 30 days")
elif (month == "february"):
	print(month + " can have 28 or 29 days")
elif (month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "decemeber"):
	print(month + " has 31 days")

# 5) zodiac
month = input("What month were you born in? ").lower()
day = int(input("What day of the month were you born? "))
if ((month == "march" and day >= 21) or (month == "april" and day <= 20)):
	print("You are an Aires")
elif ((month == "april" and day >= 21) or (month == "may" and day <= 20)):
	print("You are a Taurus")
elif ((month == "may" and day >= 21) or (month == "june" and day <= 21)):
	print("You are a Gemini")
elif ((month == "june" and day >= 22) or (month == "july" and day <= 22)):
	print("You are a Cancer")
elif ((month == "july" and day >= 23) or (month == "august" and day <= 22)):
	print("You are a Leo")
elif ((month == "august" and day >= 23) or (month == "september" and day <= 22)):
	print("You are a Virgo")
elif ((month == "september" and day >= 23) or (month == "october" and day <= 22)):
	print("You are a Libra")
elif ((month == "october" and day >= 23) or (month == "november" and day <= 22)):
	print("You are a Scorpio")
elif ((month == "november" and day >= 23) or (month == "december" and day <= 21)):
	print("You are a Sagittarius")
elif ((month == "december" and day >= 22) or (month == "january" and day <= 22)):
	print("You are a Capricorn")
elif ((month == "january" and day >= 21) or (month == "february" and day <= 19)):
	print("You are a Aquarius")
elif ((month == "february" and day >= 20) or (month == "march" and day <= 20)):
	print("You are a Pisces")

# 6) leap year
year = int(input("Input a year: "))
if (year % 4 == 0):
	print(str(year) + " is a leap year.")

# 7) average
num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
print("The average of " + str(num1) + " and " + str(num2) + " is " + str((num1 + num2) / 2))

# 8) 
y = float(input("Input y: "))
m = float(input("Input m: "))
b = float(input("Input b: "))
x = (y - b) / m
print("x is " + str(x))

# 9) 
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
xint = c / a
yint = c / b
print("x-int is " + str(xint) + " and y-int is " + str(yint))