# Prints a sentence in a centered "box" of correct width
"""
+-----------------------------+
|                             |
|  He's a very  naughty boy!  |
|                             |
+-----------------------------+
"""
# TODO Validar tamanio de entrada y errores
ANCHURA = 0

def lineaVacia(esCabecera, anchuraMensaje):
    if esCabecera:
        cadena = "+" + "-" * (anchuraMensaje +4) + "+"
    else:
        cadena = "|" + " " * (anchuraMensaje +4) + "|"
    return cadena

def ventana(mensaje, anchura):
    anchuraMensaje = len(mensaje)
    margen = " " *((anchura - anchuraMensaje + 6) / 2)
    
    print margen    
    resultado = ""
    resultado += margen + lineaVacia(True,anchuraMensaje) + "\n"
    resultado += margen + lineaVacia(False,anchuraMensaje)  + "\n"
    resultado += margen + "|  " + mensaje + "  |"  + "\n"
    resultado += margen + lineaVacia(False,anchuraMensaje)  + "\n"
    resultado += margen + lineaVacia(True,anchuraMensaje)  + "\n"
    return resultado

# TODO eliminar espacios
mensaje = raw_input("Introduce el mensaje: ")

print(ventana(mensaje, ANCHURA))

