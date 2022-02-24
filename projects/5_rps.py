'''
Isaac Longo
Rock Paper Scissors
2/24/22
'''

# modules
import random

# functions
def choice(num):
	if (num == 1):
		return "Rock"
	elif (num == 2):
		return "Paper"
	elif (num == 3):
		return "Scissors"

# rock (1) - rock (1) = 0 (tie)
# rock (1) - paper (2) = -1 (ai wins)
# rock (1) - scissors (3) = -2 (player wins)

# paper (2) - rock (1) = 1 (player wins)
# paper (2) - paper (2) = 0 (tie)
# paper (2) - scissors (3) = -1 (ai wins)

# scissors (3) - rock (1) = 2 (ai wings)
# scissors (3) - paper (2) = 1 (player wins)
# scissors (3) - scissors (3) = 0 (tie)

def round():
	while (True):
		try:
			userNum = int(input("1) rock\n2) paper\n3) scissors\nChoice: "))
			if (userNum < 1 or userNum > 3):
				print("Invalid input, try again...\n")
				continue
			userStr = choice(userNum)
			break
		except:
			print("Invalid input, try again...\n")
	
	aiNum = random.randint(1,3)
	aiStr = choice(aiNum)

	diff = userNum - aiNum
	
	if (diff == 0):
		# tie
		print(f"\nYou chose {userStr} and the AI chose {aiStr}\nIt's a tie!")
		return [0, 0]
	elif (diff == -2 or diff == 1):
		# player wins
		print(f"\nYou chose {userStr} and the AI chose {aiStr}\nYou win this round!")
		return [1, 0]
	elif (diff == -1 or diff == 2):
		# ai wins
		print(f"\nYou chose {userStr} and the AI chose {aiStr}\nThe AI wins this round!")
		return [0, 1]

# globals
while (True):
	try:
		rounds = int(input("How many rounds do you want to play? "))
		break
	except:
		print("Invalid input, try again...\n")

# game loop
i = 0
totalScore = [0, 0]
while (i < rounds):
	print(f"\nRound {i+1}:")
	roundScore = round()
	for j in range(2):
		totalScore[j] += roundScore[j]
	i += 1

print(f"\nThe final score is {totalScore[0]}:{totalScore[1]}")

# tie breaker or end the game
if (totalScore[0] == totalScore[1]):
	print("It's a tie! One more tiebreaker round...\n")
	tiebreaker = round()
	if (tiebreaker[0] == 1):
		print("\nYou win the game!")
	else:
		print("\nThe AI wins the game!")
elif (totalScore[0] > totalScore[1]):
	print("You win the game!")
elif (totalScore[0] < totalScore[1]):
	print("The AI wins the game!")