'''
Isaac Longo
Period 2
For Loop Assignment
1/4/22
'''

# ADD RANGE
# variables
start = int(input("Enter a start value: "))
stop = int(input("Enter a stop value: "))
sum = 0

# loop
for i in range(start, stop+1):
	sum = sum + i

# loop
print(f"The sum of {start}-{stop} is {sum}\n")


# FACTORIAL
# variables
pro = 1
while (True):
	num = int(input("Enter a number greater than or equal to 0: "))
	if (num >= 0):
		break
	print("Invalid input...")

# loop
for i in range(num, 0, -1):
	pro *= i		
	
# hard-code to 0
if (num == 0):
	pro=1

# output
print(f"{num} factorial is {pro}\n")


# OPPOSITES
for i in range(1,101):
	print(f"{i}-----{100-i}")