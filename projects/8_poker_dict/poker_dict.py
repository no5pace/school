'''
Isaac Longo
Poker Urban Dictionary
4/13/22
'''

# functions
def sortdict(dict):
	keys = list(dict.keys())
	keys.sort()
	dict2 = {}
	for i in keys:
		dict2[i] = dict[i]
	return dict2

def gloss(dict):
	print("")
	for i in dict:
		print(i)

def define(query, dict):
	add = input("This word is not defined...\nWould you like to add a definition? (y/n) ")
	if (add.lower() == "y"):
		definition = input(f"\nDefinition of {query}: ")
		dict[query] = definition
		dict = sortdict(dict)
		with open("dict.txt", "w") as dictionary:
			dictionary.write(str(dict))
	return dict

def delete(query):
	dict.pop(query)
	with open("dict.txt", "w") as dictionary:
		dictionary.write(str(dict))	

# open dictionary
with open("dict.txt", "r") as dictionary:
	dict = eval(dictionary.read())

# main loop
print("Welcome to the Poker dictionary!")
while (True):
	print("\n1) glossary\n2) search\n3) remove")
	choice = int(input("Input: "))
	if (choice == 1):
		gloss(dict)
	elif (choice == 2):
		query = input("Enter a word you would like defined: ")
		status = dict.get(query)
		if (status == None):
			dict = define(query, dict)
		else:
			print(f"{query}: {status}")
	elif (choice == 3):
		query = input("Enter a word you would like to delete: ")
		delete(query)