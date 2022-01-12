'''
Unit 2 Notes
For Loops
12/13/21
'''

# while loop to print 1-10
inc = 1
while (inc <= 10):
	print(inc)
	inc += 1

# while loop that prints 10-1
inc = 10
while (inc >= 1):
	print(inc)
	inc -= 1

'''
For Loops:
- for keyword
- variable name
- in keyword
- range() method with relevant parameters
	* (start, stop (not including), increment value)
- an indent for the code block
'''

# repetition with for loop
name = input("Enter your name: ")
for i in range (5):
	print(name)

# same thing with while loops
inc = 1
while (inc <= 5):
	print(name)
	inc += 1

# visualization of index
for i in range(5): # i is an index (0,1,2,3,4 in this case)
	print(i)

# print 1-10 in for loop
for i in range(10):
	print(i+1)

# print 10-1 in for loop
for i in range(10,0,-1):
	print(i)

'''
range() method:
	* takes 3 parameters (start, stop (not including), and increment)
	* if you give one parameter, it is assumed that it is the stop (default start is 0 and increment is 1)
	* if you give two parameters, it is assumed that they are start and stop (default increment is 1)
	
Examples:
	range(5) - will go from 0-4
	range(12,16) - will go from 12-15
	range(100,10,-10) - will go from 100-20 by 10s
'''

# example (5 to 0 by -1)
for i in range(5,-1,-1):
	print(i)

'''
Nested Loops - Loops within other loops
	* kind of like a clock, the minute hand only moves when the second hand moves 60 times
'''

# clock example
# import time
# for i in range(24):
# 	for j in range(60):
# 		for k in range(60):
# 			time.sleep(1)
# 			print(f"{i:02d}:{j:02d}:{k:f}")

# another example
for i in range(6):
	for j in range(i):
		print("*", end=" ")
	print("")