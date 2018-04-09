# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
def isPythagoreanTriplet(a,b,c):
	if (a**2 + b**2) == c**2:
		return True
	else:
		return False
		
def main():
	for a in range(1,1001):
		for b in range(a,1001):
			for c in range(b,1001):
				if (a+b+c == 1000) and isPythagoreanTriplet(a,b,c):
					#return (str(a) + " " + str(b) + " " + str(c)).split(" ")
					return a*b*c
					
def main_1():
	for a in range(1000,0,-1):
		for b in range(1000,a,-1):
			for c in range(1000,b,-1):
				if (a+b+c == 1000) and isPythagoreanTriplet(a,b,c):
					#return (str(a) + " " + str(b) + " " + str(c)).split(" ")
					return a*b*c
	else:
		return "NotFound"

					# measure process time
t0 = time.clock()

print(main_1())
print ("Seconds time: " , time.clock() - t0)					

