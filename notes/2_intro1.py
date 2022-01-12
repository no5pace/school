'''
Unit 1 Notes
Python Basics
9/22/21
'''

'''
2 Different ways to Concatenate
	1) using the +
		* need to combine the same data type
		* doesn't automatically add spaces
	2) using the ,
		* can combine any data types
		* automatically adds spaces
'''

# different forms of concatenation
print("I am " + "16" + " years old")	# doesn't add spaces automatically; same data type`
print("I am" , 16 , "years old")		# adds spaces automatically; different data types

# concatenating variables
name = "Isaac"
age = 16
print("My name is", name, "and I am", age, "years old") # NOTE: different data types and automatic spaces

'''
You can use typecasting to concatenate different data types using +
	1) int()
		* turns the data type into an integer
	2) str()
		* turns the data type into a string
	3) float()
		* turns the data type into a float

input() function
	* accepts input from the user though the terminal and saves it into a variables
	* uses a prompt provided as a parameter
	* converts any input into a string
'''

# typcasting an integer into a string to concatenate using + 
age = 16
print("My name is Isaac and I am " + str(age) + " years old") # since age was typecasted into a string, we can concatenate with +

# using input() to turn the integer into a string beforehand
age = input("How old are you? ")
print("Hello, you are " + age + " years old")

# doing math with string and integer numbers using typcasting
age = int(age)
timeFrame = 10
print("You will be " + str((age + timeFrame)) + " years old in " + str(timeFrame) + " years")

'''
Escape Characters
	* An escape character is a sequence of characters inside of a string that carry a meaning
	* i.e.
		- \n is a new line
		- \t is a tab
		- \\ is a backslash (since a single backslash initalizes an escape character, you need to use 2 to indicate simply printing a backslash)
		- \' is a single quote
		- \" is a double quote
		- \b is a backspace (why do i need this)
'''

print("this is a\nnew line")
print("\t this is tabbed")
print("this is a backslash \\")
print("\"double quotes within a double quoted string\"")
print('\'single quotes within a single quoted string\'')
print('\'single quotes within a single quoted string\'')
print("hello without backspace\nhello\b with backspace")