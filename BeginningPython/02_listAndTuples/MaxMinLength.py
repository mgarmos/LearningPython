"""
Length, Minimum, and Maximum
The built-in functions len, min, and max can be quite useful. 
The function len returns the number of elements a sequence 
contains. min and max return the smallest and largest elements 
of the sequence, respectively.
"""
numbers = [100, 34, 678]
print(len(numbers)) # 3
print(max(numbers))
print(min(numbers))

print(max(2, 3))
print(min(9, 3, 2, 5))

#The list Function
cadena = 'Hello'
print(cadena)
print(type(cadena))

myList = list('Hello') #Convierte a lista
print(myList)
print(type(myList))

cadena1 = "".join(myList)
print(cadena1)
print(type(cadena1))

cadena2 = "*".join(myList)
print(cadena2)
print(type(cadena2))

"""
Basic List Operations
You can perform all the standard sequence operations on lists, 
such as indexing, slicing, concatenating, and multiplying. 
But the interesting thing about lists is that they can be modified.
In this section, you'll see some of the ways you can change a list: 
item assignments, item deletion, slice assignments, and list methods. 
(Note that not all list methods actually change their list.)
"""
#Changing Lists: Item Assignments
x = [1, 1, 1]
print(x)
x[1] = 2
print(x)

#Deleting Elements
del(x[1])
print(x)

#Assigning to Slices
name = list('Perl')
listName = list(name)
print(listName)

listName[2:3] = list("Saludos")
print(listName)

listName[1:6:2] = [1,2,3]
print(listName)

#append
listName.append("hola")
print(listName)

#clear  ->listName.clear() -ERROR en 2.7
listName[:] = []
print(listName)

#copy
a = [1, 2, 3]
b = a
b[1] = 4
print(a)
print(b) # a y b apuntan al mismo objeto en memoria

a = [1, 2, 3]
# b = a.copy() --> Error
b = a + [] # a y b apuntan a objetos diferentes
print(b)
b[1] = 4
print(a)
print(b) # a y b apuntan al mismo objeto en memoria

listaNombres = ["Marta", "Sonia", "Marta"]
print(listaNombres.count("Marta"))



