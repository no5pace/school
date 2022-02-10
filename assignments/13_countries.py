'''
Isaac Longo
Period 2
Country List
2/10/22
'''

# initalize countries list
countries = []

# get countries
while (True):
	country = input("Name a country you have been to (q to quit): ")
	if (country.lower() == "q"):
		break
	countries.append(country)

# print countries
for i in range(len(countries)):
	print(f"{i+1}) {countries[i]}")