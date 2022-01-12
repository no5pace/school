'''
Unit 2 Notes
Python Basics
10/12/21
'''

'''
Booleans are used to allow computers to make complex decisions (binary)
When true or false statements are embedded within eachother (nested), complex reactive behavior is possible

Comparison Operators (return true)
	1) == -> if equal to
		* as opposed to the assignment operator =
	2) != -> if not equal
	3) >  -> if greater than
	4) >= -> if greater than or equal to
	5) <  -> if less than
	6) <= -> if less than or equal to
'''

# compare a number to 1
num = float(input("Pick a number: "))
if (num == 1):
	print(str(num) + " is equal to 1")
elif (num > 1):
	print(str(num) + " is greater than 1")
elif (num < 1):
	print(str(num) + " is less than 1")

# can also be used with strings
word = input("Type a phrase: ")
if (word == "hello"):
	print(word + " is the same as hello")
elif (word != "hello"):
	print(word + " is not the same as hello")

'''
Binary Boolean Operators 
	1) and
		* compares two comparisons, returns true if BOTH are true
	2) or
		* compares two comparisons, returns true if EITHER is true
	3) not
		* looks at one comparison, returns true if it is NOT true
		
Truth Tables:

	TABLE FOR AND
	_________________________
	|       | TRUE  | FALSE |
	|_______|_______|_______|
	| TRUE  | true  | false |
	|_______|_______|_______|
	| FALSE | false | false |
	|_______|_______|_______|
	
	TABLE FOR OR
	_________________________
	|       | TRUE  | FALSE |
	|_______|_______|_______|
	| TRUE  | true  | true  |
	|_______|_______|_______|
	| FALSE | true  | false |
	|_______|_______|_______|
	
	TABLE FOR NOT
	_________________________
	|       | TRUE  | FALSE |
	|_______|_______|_______|
	|  NOT  | false | true  |
	|_______|_______|_______|
'''

# lololol
print(not not not not not not not not True)

# not False == True, and since its all ors -> return is True
print("dog"=="cat" or not False or 3>2 or 2==4)

# 4==4 is True, but the not makes it False -> return is False 
print(not(4==4))

# 4==4.0 is True, and since its or the entire expression in the () is True, combined with the and True -> return is True
print(((2>4)or(4==4.0)) and True)

# 2<4 and 5.0==5 is True, but the not makes it False, and since 5==5 -> return is False
print(not(2<4 and 5.0==5) or (5!=5))

# not ("cat"=="Cat") is True, 4 is equal to 4 and the two nots cancel out giving True, and not (6=="6") is True; all True -> return is True
print(not("cat"=="Cat") and not not (4<=4) and not (6=="6"))

'''
Conditionsals - control the flow of the program using conditions that evaluate to Boolean values
	* decides what to do based on whether it's condition is true or false

There are a variety of conditionals, and each of them has their own syntax
	* indentations indicates the beginning/end of a block of code
	
Keep in mind...
	1) blcoks begin where there is an indentations
	2) block can contain other blocks (nested conditionals)

If/Else Statement
	* starts with if, followed by a condition within parentheses, and a colon
	* indented code afterwards will be run IF the condition is TRUE
	* after the statement, elif can be used to provide an alternate conditional OR else can be used to provide a default in the case that no conditions are satisfied
	
Elif Statement
	* used when you want other specific conditionals instead of just an else
	* has the same syntax as an if statement, with if replaced with elif
	* as a result, it is only checked if previous if/elif statements are false
	
'''

# if statement
name = input("What is your name? ")
if (name == "Isaac"):
	print("We've been waiting for you, Isaac")
elif (name == "Sam"):
	print("Tell Isaac we're waiting for him")
else:
	print("Get lost poser")
	
# ...with multiple conditions
username = input("Enter your username: ")
password = input("Enter your password: ")
if (username == "isaaclongo" and password == "root"):
	print("Access granted")
else: 
	print("Access denied")
	
# ...or with nested conditionals
username = input("Enter your username: ")
if (username == "isaaclongo"):
	password = input("Enter your password: ")
	if (password == "root"):
		print("Access granted")
	else:
		print("Access denied: wrong password")
else:
	print("Access denied: wrong username")
	
# other example
x = int(input("Enter and x value: "))
y = int(input("Enter and y value: "))

if (x < y):
	print(str(x) + " is less than " + str(y))
elif (x > y):
	print(str(x) + " is greater than " + str(y))
elif (x == y):
	print(str(x) + " is equal to " + str(y))