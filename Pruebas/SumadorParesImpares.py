# -*- coding: utf-8 -*-
print("SUMADOR DE PARES E IMPARES")
totalNums = int(raw_input("¿Cuántos números va a escribir? "))

if totalNums > 0:
    
    
    listPares=[]
    listImPares=[]
    
    for num in xrange(totalNums):
        num = int(raw_input("Escriba un número entero: "))
        
        if (num % 2) == 0:
            listPares.append(num)
        else:
            listImPares.append(num)
    print("La suma de los números pares que ha escrito es " + str(sum(listPares)))
    print("La suma de los números impares que ha escrito es " + str(sum(listImPares)))


print("Programa terminado")

