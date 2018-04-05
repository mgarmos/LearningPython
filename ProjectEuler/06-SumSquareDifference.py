# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""
NUM = 100

squares = sum([x**2 for x in  range(NUM+1)])
natural = sum(range(1,NUM+1))**2
print(natural - squares)

