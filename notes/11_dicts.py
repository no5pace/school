'''
Isaac Longo
Dictionary Notes
4/8/22
'''

'''
A dictionary is a data type in python that provides a way to access organized data
Contains a key-value pair
	* similar to a list; a collection of many values
	* instead of using indices, keys are used
	* order of keys does not matter as the order of indices matters in a list
		- as long as the key-value pairs are the same, the dictionaries are equal

Value can be found from key using [] like an array, or with the .get() method
	* .get() takes up to 2 parameters
	* .get(key, fallback)
'''

# list review
colors = ["Orange", "Blue", "Red"]
for i in range(len(colors)):
	print(colors[i])

# dictionary
birthdays = {"Isaac":"11/11/04", "Ms. Ghazali":"2/1/01", "Bryan":"11/30/04", "Jason":"4/16/05"}
birthdays2 = {"Ms. Ghazali":"2/1/01", "Isaac":"11/11/04", "Bryan":"11/30/04", "Jason":"4/16/05"}
for i in birthdays:
	print(f"{i}: {birthdays[i]}")

if (birthdays == birthdays2):
	print("These two dictionaries ordered differently are still equal!")

# .get() method, similar to just using [] but can catch errors
print(birthdays.get("Isaac"))
print(birthdays["Isaac"])
print(birthdays.get("Not a key"))
# print(birthdays["Not a key"])

'''
in and not in
	* in will return True if a key/value is in the dictionary (also works for lists)
	* not in will return True if a key/value is not in the dictionary (also works for lists)
'''

# in and not in
print(birthdays)
print(birthdays.values())
print("Isaac" in birthdays)
print("11/11/04" in birthdays.values())
print("Gabe" not in birthdays)
print("10/1/07" not in birthdays.values())