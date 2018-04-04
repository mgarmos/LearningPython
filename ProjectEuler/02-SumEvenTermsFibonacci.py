# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Result = 4613732
fib = [0,1]
next = 0
while (next<4000000):
	next = fib[-1] + fib[-2]
	fib.append(next)

print(fib)

sumPar = 0
sumImpar = 0
for num in fib:
	if num%2 == 0:
		sumPar += num
	else:
		sumImpar += num

print('sumPar:   ' , sumPar)
print('sumImpar:' , sumImpar)	
