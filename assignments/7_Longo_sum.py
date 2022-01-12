'''
Isaac Longo
Period 2
Sum of a Series
12/3/21
'''

# get start and end numbers
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
add = 0

# loop to add
for i in range(start,end+1):
	add += i

print(f"The sum of the series {start}-{end} is {add}")