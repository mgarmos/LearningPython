"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
RES: 
 [5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639, 13195]
 Lista:  [71, 839, 1471, 6857]
"""

def mult(lista):
	res = 1
	for i in lista:
		res *= i
	print('res:', res)
	return res

listPrimeFactors = []
num = 600851475143
prime = 1
while True:
	prime += 1
	if num % prime == 0:
		listPrimeFactors.append(prime)
		if mult(listPrimeFactors) == num: break

	
print("Lista: ", listPrimeFactors)







