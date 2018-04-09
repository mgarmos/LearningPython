# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th 
prime is 13.

What is the 10 001st prime number?
"""
import time, math

# Devuelve true si el número es primo
def esPrimo(num):
	RMAX = int(math.sqrt(num))
	for div in range(2, RMAX+1):
		if num % div == 0:
			return False
	else:
		return  True	

# measure process time
t0 = time.clock()

INTER = 10001
   
num = 0
cont = 0
while cont <= INTER:
    num +=1
    if(esPrimo(num)) == True:
        cont +=1

print(num)
print ("Seconds time: " , time.clock() - t0)

