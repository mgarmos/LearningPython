# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th 
prime is 13.

What is the 10 001st prime number?
"""
# Devuelve true si el número es primo
def esPrimo(num):
    for x in range(num-1,int(sqrt(num)),-1):
        if num % x == 0:
            return False
    else:
        return True

# Se buscan primos únicamente los numeros impares a partir del 2
# Se        
num = 3
cont = 2
while cont <= 7:
    num +=2
    if(esPrimo(num)) == True:
        cont +=1
   
    
print(num)