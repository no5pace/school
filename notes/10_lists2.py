'''
Isaac Longo
Lists 2
2/9/22
'''

# working with lists
# grovery list without a loop
item1 = input("First item: ")
item2 = input("Second item: ")
item3 = input("Third item: ")
item4 = input("Fourth item: ")
item5 = input("Fifth item: ")

# with a loop
end = False
counter = 1
items = []
while (end != True):
	item = input(f"Item {counter} (input q to quit): ")
	if (item.lower() == "q"):
		break
	items.append(item)
	counter += 1

print(items)

'''
in and not in Operators
	* determine whether a value is or isn't in a list
	* return True or False
'''

# greetings list
greet = ["Hello", "Hi", "Howdy", "Yo"]
print("Howdy" in greet)
print("Heyo" in greet)

# pet names
pets = ["Zoe", "Pookie", "Sophie"]
name = input("Enter a pet name: ")

if (name not in pets):
	print(f"I do not have a pet named {name}")
else:
	print(f"{name} is my pet.")

'''
Multiple Assignment Trick: shortcut to assign multuple variables in one line of code
'''

# isntead of doing this
cat = ["Fat", "Black", "Loud"]
size = cat[0]
color = cat[1]
disp = cat[2]
print(size, color, disp)

# do this
size, color, disp = cat
print(size, color, disp)

'''
Augmented Assignment Operators:
Statement			Shortcut
num = num + 1		num += 1
num = num - 1		num -= 1
num = num * 1		num *= 1
num = num / 1		num /= 1
num = num % 1		num %= 1
'''

greeting = "Hello"
greeting += " there"
print(greeting)

'''
Built-in Methods for lists:
	* index() -> takes a value and returns its index
	* append() -> adds a new value to the list
	* insert() -> adds a new value to the list at a specific index and shift other values right
	* remove() -> removes a specified element
	* sort() -> sorts a list alphabetically or numerically
		- if reverse is True, it sorts in the opposite direction
'''

# index()
colors = ["Red", "White", "Blue"]
print(colors.index("Red"))

# append()
colors.append("Green")
print(colors)

# insert()
colors.insert(1, "Orange")
print(colors)

# remove()
colors.remove("Blue")
print(colors)

# sort()
colors.sort()
print(colors)

numbers = [100, -5, 8, 5, 3, 0]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)