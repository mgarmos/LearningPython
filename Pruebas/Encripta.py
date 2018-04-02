"""
Use a list comprehension to create a list, cubes_by_four.

The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.

Finally, print that list to the console.

Note that in this case, the cubed number should be evenly divisible by 4, not the original number.

"""




def encripta(mensaje):
    temp = ""
    for c in mensaje:
        temp += chr(ord(c)+1)
    return temp
    
mensaje = "Hola Adrian y Victor. Este es el siguiente mensaje en clave que os envio"
print encripta(mensaje)