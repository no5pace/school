'''
Unit 2 Notes
Loops
11/18/21
'''

'''
Loop - something that gets executed repeatedly until something tells it to stop
	1) while loop -> will execute the code block as long as the conditional is true
		while (conditional):
			code block
	2) for loop -> will execute the code block for a given range OR iterate over a table
		for i in range(i, j, k):
			code block
		for i in table:
			code block
'''

# # while loop
# i = 0
# while (i < 10):
# 	print(i)
# 	i += 1

# # for loop with range()
# for i in range(0,10,1):
# 	print(i)

# # for loop with table
# tab = [0,1,2,3,4,5,6,7,8,9]
# for i in tab:
# 	print(i)

# # name verification
# name = input("Enter my name: ").lower()
# while (name != "isaac"):
# 	print("That is not my name, try again")
# 	name = input("Enter your name: ").lower()

# import time
# # count-up
# bot = int(input("Enter a minimum: "))
# top = int(input("Enter a maximum: "))
# while (bot <= top):
# 	print(bot)
# 	time.sleep(1)
# 	bot += 1

# # count-down
# top = int(input("Enter a maximum: "))
# bot = int(input("Enter a minimum: "))
# while (top >= bot):
# 	print(top)
# 	time.sleep(1)
# 	top -= 1

''''
break statement - forces a loop to close
continue keywords - jumps back to beginning of the loop
'''

# break
while (True):
	name = input("Please type your name: ")
	if (name == "Isaac"):
		break
print("Thanks, " + name)

# continue
while (True):
	name = input("Please type your name: ")
	if (name != "John"):
		continue
	password = input("Hello John, what is your password? ")
	if (password == "ilovecs"):
		break
print("Access granted")