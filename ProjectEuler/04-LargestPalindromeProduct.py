"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

for x in range(99,10,-1):
	for y in range(x, 10, -1):
		num = x * y
		if str(num)[:] ==  str(num)[::-1]:
			print("es pal ", num)
			break;
	







