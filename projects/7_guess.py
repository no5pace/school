'''
Isaac Longo
Guessing Game
4/1/22
'''

# modules
import random

# init
while (True):
	try:
		print("1) Easy\n2) Medium\n3) Hard")
		diff = int(input("Choose your game difficulty: "))
		if (diff < 1 or diff > 3):
			print("Invalid input, try again...\n")
			continue
		break
	except:
		print("Invalid input, try again...\n")

if (diff == 1):
	guesses = 15
	range = 100
elif (diff == 2):
	guesses = 10
	range = 300
elif (diff == 3):
	guesses = 5
	range = 500
num = random.randint(1, range+1)

print(f"{guesses} guesses with a range of 1-{range}")

# game loop
i = 0
while (i < guesses):
	while (True):
		try:
			guess = int(input("\nGuess a number: "))
			if (guess > range or guess < 1):
				print("Guess out of range, try again...")
				continue
			break
		except:
			print("Invalid guess, try again...")
	
	if (guess > num):
		print("Too High!")
	elif (guess < num):
		print("Too Low!")
	else:
		print("Correct!")
		break
	i += 1
	print(f"{guesses-i} guess(es) left")

print(f"\nThe number was {num}")