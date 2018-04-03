fib = [0,1]
for cont in range(2,90):
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
