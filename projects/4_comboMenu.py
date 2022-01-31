'''
Isaac Longo
Law of Large Numbers
1/24/22
'''

# libraries
import math
import random
import os

# functions
def item(item, price):
	return (f"{item} - ${price:.2f}")

def buy(item, price):
	items.append(item)
	prices.append(price)

while (True):
	# variables
	order = random.randint(100,999)
	items = []
	prices = []
	
	# sandwich
	while (True):
		chicken = item("Chicken", 5.25)
		beef = item("Beef", 6.25)
		fish = item("Fish", 5.75)

		print(f"What type of sandwich would you like?\n1) {chicken}\n2) {beef}\n3) {fish}")
		sandwich = input("Selection: ")

		if (sandwich == "1"):
			buy("Chkn Sandwich", 5.25)
			break
		elif (sandwich == "2"):
			buy("Beef Sandwich", 6.25)
			break
		elif (sandwich == "3"):
			buy("Fish Sandwich", 5.75)
			break
		else:
			print("Invalid selection... try again\n")

	print("")

	# beverage
	while (True):
		beverage = input("Would you like a beverage (y/n)? ")
		
		if (beverage != "y" and beverage != "n"):
			print("Invalid selection... try again\n")
		else:
			break

	if (beverage.lower() == "y"):
		small = item("Small Beverage", 1.00)
		medium = item("Medium Beverage", 1.75)
		large = item("Large Beverage", 2.25)

		while (True):
			print(f"What size would you like?\n1) {small}\n2) {medium}\n3) {large}")
			size = input("Selection: ")

			if (size == "1"):
				buy("Sml. Beverage", 1.00)
				break
			elif (size == "2"):
				buy("Med. Beverage", 1.75)
				break
			elif (size == "3"):
				buy("Lrg. Beverage", 2.25)
				break
			else:
				print("Invalid selection... try again\n")

	print("")

	# fries
	while (True):
		fries = input("Would you like fries (y/n)? ")
		
		if (fries != "y" and fries != "n"):
			print("Invalid selection... try again\n")
		else:
			break

	if (fries.lower() == "y"):
		small = item("Small", 1.00)
		medium = item("Medium", 1.50)
		large = item("Large", 2.00)

		while (True):
			print(f"What size would you like?\n1) {small}\n2) {medium}\n3) {large}")
			size = input("Selection: ")

			if (size == "1"):
				meg = input("Would you like to Mega-Size your fries (y/n)? ")
				if (meg.lower() == "y"):
					size = "3"
			
			if (size == "1"):
				buy("Sml.   Fries", 1.00)
				break
			elif (size == "2"):
				buy("Med.   Fries", 1.50)
				break
			elif (size == "3"):
				buy("Lrg.   Fries", 2.00)
				break
			else:
				print("Invalid selection... try again\n")

	print("")

	# ketchup
	while (True):
		try:
			packets = float(input("How many ketchup packets would you like? "))
			packets = int(math.ceil(packets))
			buy(f"Ketchup Pkts: {packets}", (packets*0.25))
			break
		except:
			print("Invalid input... enter a positive number\n")

	# discount
	discount = 0.00
	if (beverage == "y" and fries == "y"):
		discount = -1.00
		buy("Combo Discount", discount)

	# order info
	os.system("clear")
	print("You ordered: ")
	for i in range(len(items)):
		if (items[i] == "Discount"):
			break
		print(f"{items[i]}\t\t-\t${prices[i]:.2f}")

	while (True):
		final = input("\nWould you like to finalize your order (y/n)? ")
		
		if (final != "y" and final != "n"):
			print("Invalid selection... try again\n")
		else:
			break

	os.system("clear")

	if (final.lower() == "y"):
		break

# receipt
print(f"Burger Boys\n1/27/22\nHoboken, NJ 01902\n")

print(f"Order #{order}\n")

for i in range(len(items)):
	print(f"{items[i]}\t\t-\t${prices[i]:.2f}")

subtotal = 0
for price in prices:
	subtotal += price
tax = (subtotal * 0.07)
print(f"\nSubtotal:\t${subtotal:.2f}\nTax:\t\t${tax:.2f}\nTotal:\t\t${(subtotal + tax):.2f}")

print(f"\nThank you for ordering at Burger Boys!\n\n------ Check Closed ------")

# payment
while (True):
	tendered = float(input("\nHow much will you be paying? "))
	if (tendered > (subtotal + tax)):
		print(f"\nAmount Tendered: {tendered:.2f}\nChange: {-((subtotal + tax) - tendered):.2f}")
		break
	else:
		print("You have to pay fully...")