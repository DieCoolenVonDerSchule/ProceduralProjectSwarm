
import sys
import random




x = 10

if len(sys.argv) == 1 and x == 10:
	print("NO ARGUMENT")
	x=0

if len(sys.argv) > 1:
	print("Argument List: ", str(sys.argv))

if x==0:
	x = random.randrange(10,20)

print('X: ', x)
 	
