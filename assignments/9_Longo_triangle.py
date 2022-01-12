'''
Isaac Longo
Period 2
Triangles
12/14/21
'''

for i in range(5):
	for j in range(5-i):
		print("*", end="")
	print("")

print("")

for i in range(5):
	for j in range(i+1):
		print("*", end="")
	print("")

print("")

for i in range(0,5,1):
	for j in range(i):
		print(" ", end="")
	for j in range(5-i):
		print("*", end="")
	print("")

print("")

for i in range(5,0,-1):
	for j in range(i-1):
		print(" ", end="")
	for j in range(6-i):
		print("*", end="")
	print("")

print("")

height = 5
maxWidth = 1 + (2*(height-1))
for i in range(1,height+1,1):
	width = 1 + (2*(i-1))
	for j in range(int((maxWidth-width)/2)):
		print(" ", end="")
	for j in range(int(width)):
		print("*", end="")
	for j in range(int((maxWidth-width)/2)):
		print(" ", end="")
	print("")