'''
Isaac Longo
Quadratic Equations w/ Graphing
3/11/22
'''

## graphing lib
import matplotlib.pyplot as plt

## get input
while (True):
	try:
		a = float(input("What is a? "))
		if (a == 0):
			print("a cannot be 0...\n")
			continue
		b = float(input("What is b? "))
		c = float(input("What is c? "))
		break
	except:
		print("Please enter a number...\n")

## solutions
neg = False
disc = b**2 - 4*a*c
discSim = 0

# equation
print(f"\n{a}x^2 + {b}x + {c}")

# discriminant (the **0.5 may cause some problems, look here if theres issues)
if (disc < 0):
	print("2 imaginary solutions")
	discSim = (-disc)**0.5
	neg = True
elif (disc > 0):
	print("2 real solutions")
	discSim = disc**0.5
else:
	print("1 real solution")
	discSim = 0

# find solutions
if (neg == False):
	# if disc is positive or zero, then just simplify fully
	posSol = str((-b + discSim) / (2*a))
	negSol = str((-b - discSim) / (2*a))
	print(f"x = {negSol}, {posSol}")
else:
	# if disc is negative, see if the terms simplify
	# if not, then print the fraction solution, if 
	# they do, then print the simplified term
	term1 = str(-b)
	term2 = str(discSim) + "i"
	term3 = str(2*a)

	if (-b % (2*a) == 0 and discSim % (2*a) == 0):
		term1 = str(-b / (2*a))
		term2 = str(discSim / (2*a)) + "i"

		posSol = f"{term1} + {term2}"
		negSol = f"{term1} - {term2}"
	else: 
		posSol = f"({term1} + {term2}) / {term3}"
		negSol = f"({term1} - {term2}) / {term3}"

	print(f"x = {negSol}, {posSol}")

## GRAPHING
# vars
ymin = 0
ymax = 100
xmin = -20
xmax = 20
step = 1

# fill axes
yaxis = []
xaxis = []
for i in range(ymin, ymax+1, step):
	yaxis.append(i)
for i in range(xmin, xmax+1, step):
	xaxis.append(i)

# find f(x)
yvalues = []
for x in xaxis:
	yvalues.append(a*(x**2) + b*x + c)

# for i in range (len(xaxis)):
# 	print(xaxis[i], yvalues[i])

# plot
plt.xlabel("x")
plt.ylabel("y")
plt.axis([xmin,xmax, ymin,ymax])
plt.plot(xaxis, yvalues)
plt.show()