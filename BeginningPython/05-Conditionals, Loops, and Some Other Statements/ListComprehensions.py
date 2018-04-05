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