'''
Isaac Longo
Lists
2/7/22
'''

'''
A list contains multiple values in an ordered sequence

A data type (just like integer, boolean, string, etc.)

Example:
["Looks", "like", "this"]

Values inside are called items or elements; always separated by commas
Each element has a position called an index (starts at 0)
You cannot access an index that is out of the range of the list
Indices must be integers

Negative indexing refers to accessing the list backwards (from the last element)
'''

# animal list
animalList = ["cat", "dog", "elephant", "rat"]
print (animalList)

# indexing
first = animalList[0]
print(first)

# nested lists
namesAndAges = [["John", "George", "Andre"], [15, 16, 17]]

for i in range(3):
	print(namesAndAges[0][i], namesAndAges[1][i])

# negative index
names = ["John", "George", "Andre", "Nick"]

for i in range(1, 5):
	print(names[-i])

'''
Sublists with slices

Just as an index can get a single value, a slice can get several

names[2] == element at index 2
names[1:4] == slice of index 1 to index 4 (not including 4)

len() function:
	* returns the length of the list
'''

# slice
colors = ["Orange", "Red", "Pink", "Green", "Yellow"]
print(colors[0:3])	#index 0 -> 2
print(colors[:2])	#index 0 -> 1
print(colors[-2:])	#index 3 -> 4
print(colors[:-2])	#index 0 -> 2
print(colors[:])	#all indices

# len()
print(len(colors))

# change values in a list
groceryList = ["Milk", "Eggs", "Cheese", "Cereal"]
print(groceryList)

groceryList[0] = "Steak"
print(groceryList)

groceryList[0] = groceryList[1]
print(groceryList)

'''
+ operator can combine two lists to create a new one
* operator can duplicate a list
'''

# list concatenation and duplication
list1 = ["A", "B", "C"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list4 = list3 * 3
print(list4)

# removing a value from a list
grades = ["A", "B", "C", "D", "F"]
del grades[0]
print(grades)

del grades[-1]
print(grades)