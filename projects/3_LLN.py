'''
Isaac Longo
Law of Large Numbers
1/24/22
'''

import random
import os

while (True):
	verbose = input("Verbose mode (y/n)? ")
	if (verbose == "y"):
		verbose = True
		break
	elif (verbose == "n"):
		verbose = False
		break
	else:
		print("Invalid input...\n")

while (True):
	try:
		num = int(input("How many flips? "))
		break
	except ValueError:
		print("Invalid Input...\n")

head = 0
tail = 0
coin = 0

for i in range(1, num+1):
	coin = random.randint(1,2)
	
	if (coin == 1):
		head += 1
	else:
		tail += 1

	# verbose
	if (verbose == True):
		os.system("cls" if os.name == "nt" else "clear")
		print(f"Total Flips: {i}\nHeads: {head}\nTails: {tail}\n\nHeads%: {(head / i) * 100}%\nTails%: {(tail / i) * 100}%\n")

# silent
if (verbose == False):
	print(f"Total Flips: {i}\nHeads: {head}\nTails: {tail}\n\nHeads%: {(head / i) * 100}%\nTails%: {(tail / i) * 100}%\n")