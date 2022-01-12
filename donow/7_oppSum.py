'''
Isaac Longo
Extra Credit
12/9/21
'''

# initialize
sums = 0
i = -1

# loop starting at -1 and going to 1000
while (i != 1000):
	# add
	sums += i
	
	# increment
	if (i < 0):
		i = -(i - 1)
	elif (i > 0):
		i = -(i + 1)

# print 4 times that sum
print((4*sums))