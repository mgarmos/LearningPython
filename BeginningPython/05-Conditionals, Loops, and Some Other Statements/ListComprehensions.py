# -*- coding: utf-8 -*-
"""
List comprehension is a way of making lists from other lists (similar to 
set comprehension, if you know that term from mathematics). It works in 
a way similar to for loops and is actually quite simple.
        >>> [x * x for x in range(10)]
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
square = [x * x for x in range(10)]
print(square)

#Multiplos de 3 al cuadrado
mult = [x*x for x in range(10) if x % 3 == 0]
print(mult)

var1 = [(x, y) for x in range(3) for y in range(3)]
print(var1)

var2 = [(x, x**0.5 +y) for x in range(3) for y in range(3)]
print('var2', var2)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])