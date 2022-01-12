'''
Unit 1 Notes
Python Basics
9/20/21

Vocab
	IDE: (Integrated Development Environment) somehwere where you can write and run code
	Comment: text of characters to be ignored when running your code
		* ctrl + / to autocomment

Operations
	Addition: +
	Subtraction: -
	Multiplication: *
	Division: /
	Floored Division: //
	Modulus/Remainder: %
	Exponent: **
'''

# string literal vs arithmetic
print("2+2")
print(2+2)

# different operations
print(3+6)	# addition
print(3-6)	# subtraction
print(3*6)	# multiplication
print(3/6)	# divison
print(7%6)	# remainder
print(3//6) # floor
print(3**6) # exponent

'''
Math operators follow the same order of operations (precedence) as in math

Parentheses
Exponents
Muliplication/Division/Floored Division/Modulus from left to right
Addiction/Subtraction from left to right
'''

# (5-1) * ((7+1)/(3-1))
# 4 * (8 / 2)
# 4 * 4
# 16
print((5-1) * ((7+1)/(3-1)))

'''
Data Types:
In math, a variable holds number values

In CS, a variable holds different kinds of data; data types

Major data types:
1) Integers (whole numbers + and -)
2) Float (decimal)
3) Strings (combination of characters, letters, and/or punctuation)
	* Keep in mind that strings will not be interpretted like numbers
4) Boolean (true [1] or false [0] valeu)
5) etc... more will be covered later in class
'''

'''
String Concatentation and Replication
	Concatentation: combining things together (i.e. 2 or more strings)
		* In Python, use +
		* Be aware of spacing, there is flexibility in regards to where you can put the space
	Replication: replicating a string
		* In Python, use *
		* Only works with integers, not floats
'''

# Concatenate 2 strings
print("John " + "Smith")

# Concatenate 2 different data types
''' print("John is " + 15)  --->  DOESN'T WORK, YOU CAN'T CONCATENATE DIFFERENT DATA TYPES W/O TYPECASTING (learn later) '''

# String replication (not an error since it's not "math" multiplication)
print("John" * 5)

# String replication with a float
''' print("John" * 5.0)     --->  DOESN'T WORK, YOU CAN'T REPLICATE BY A FLOAT '''