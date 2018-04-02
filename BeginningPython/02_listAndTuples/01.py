# -*- coding: utf-8 -*-
edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward,  john]
print(database)
print(type(database))
#indexing, slicing, adding, multiplying, and checking for membership

#Indexing
cadena = "Hola Mundo"
print(cadena[-2]) # d
print(cadena[2]) # l

#Slicing: you can use slicing to access ranges of elements.
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30]) # http://www.python.org
print(tag[32:-4]) #Python web site

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6]) # [4, 5, 6]
print(numbers[0:1]) #[1]
print(numbers[7:10]) #[8, 9, 10]
print(numbers[-3:-1]) #[8, 9]

print(numbers[0:]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[::-2]) #[10, 8, 6, 4, 2]

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']
mes = int(input("Introduce un mes: "))
print(months[mes-1])

#Adding Sequences
sec1 = [1,2,3]
sec2 = [4,5,6]

print(sec1 + sec2) # Suma las listas

#Multiplication

sec1 = [3,7]
print(sec1 * 4)
