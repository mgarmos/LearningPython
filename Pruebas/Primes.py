#!/usr/bin/python
import time, math


def prime_1(num):
	for div in range(2, num):
		if num % div == 0:
			return True
	else:
		return False
		
def prime_2(num):
	RMAX = int(math.sqrt(num))
	for div in range(2, RMAX):
		if num % div == 0:
			return True
	else:
		return False
		
def prime_2_1(num):
	RMAX = int(math.sqrt(num))
	for div in range(3, RMAX,3):
		if num % div == 0:
			return True
	else:
		return False		

def prime_3(num):
	if num%2 == 0 or num%3 == 0 or num%5== 0:
		return True
	
	RMAX = int(math.sqrt(num-1))	
	lista = [x for x in range(2,RMAX) if x % 5 != 0 and (x % 6 == 1 or x % 6 == 5)]
	# print(lista)
	for div in lista:
		if num % div == 0:
			return True 
	else:
		return False		

INT = 200000

# print(prime_3(23))
# print(prime_3(17))
# print(prime_3(14))
# print(prime_3(12))
# print(prime_3(6))
# print(prime_3(5))
# print(prime_3(2))	
		
# measure process time
t0 = time.clock()
for num in range(1,INT):
	prime_3(num)
print ("prime_3: " , time.clock() - t0, "seconds time")

t0 = time.clock()
for num in range(1,INT):
	prime_2_1(num)
print ("prime_2_1: " , time.clock() - t0, "seconds time")

t0 = time.clock()
for num in range(1,INT):
	prime_2(num)
print ("prime_2: " , time.clock() - t0, "seconds time")

# t0 = time.clock()
# for num in range(1,INT):
	# prime_1(num)
# print ("prime_1: " , time.clock() - t0, "seconds time")