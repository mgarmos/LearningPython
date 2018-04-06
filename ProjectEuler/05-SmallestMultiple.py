"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def div(num):
	for x in range(2,21):
		if num % x > 0:
			return False
	else:
		return True

	
num = 20
while div(num) == False:
	num += 1
	
print(num)
	
"""	
import math
mul=1
for i in range(2,21):
	mul=int(mul*i/math.gcd(mul,i))

print(mul)



















































