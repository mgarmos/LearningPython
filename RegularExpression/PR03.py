
import re
CR = '\r\n'

anot = ("﻿Controle su destino (Anthony Robbins)" + CR +
	"- La subrayado en la página 17 | posición 253-255 | Añadido el jueves, 30 de noviembre de 2017 7:51:21" + CR +
	" " + CR +
	"Una de mis convicciones más profundas es la de que si establece un criterio más elevado, y logra creer en él, no cabe la menor duda de que conseguirá imaginar también las estrategias más adecuadas para alcanzarlo. Sencillamente, encontrará un camino.")

# Para evitar errores de encoding
anot = anot.replace(u'\ufeff', u'')
anot = anot.replace(u'\u2666',u'')
anot = anot.replace(u'\u2015',u'')		

print(anot)
print("-------------------")


# Elimina las lineas en blanco. 
lines = [x for x in anot.split(u'\r\n') if x] 	#x es True si tiene contenido

print("Título ", lines[0])

for line in lines:
	print(line)
	