"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
lista = []
for x in range(999,100,-1):
	for y in range(x, 100, -1):
		num = x * y
		if str(num)[:] ==  str(num)[::-1]:
			lista.append(num)
print(max(lista))
	







