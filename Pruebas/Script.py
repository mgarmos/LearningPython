import subprocess

# Read in the file
with open(r'D:\LearningPython\Pruebas\file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('ram', 'abcd')

# Write the file out again
with open(r'D:\LearningPython\Pruebas\file.txt', 'w') as file:
  file.write(filedata)


print (subprocess.check_output(["mvn", "-n", "1", "8.8.8.8"]))

print (subprocess.check_output(["ping", "-n", "1", "8.8.8.8"]))


def modificarLinea(archivo,buscar,reemplazar):

	"""

	Esta simple función cambia una linea entera de un archivo

	Tiene que recibir el nombre del archivo, la cadena de la linea entera a

	buscar, y la cadena a reemplazar si la linea coincide con buscar

	"""

 

	with open(archivo, "r") as f:

		# obtenemos las lineas del archivo en una lista

		lines = (line.rstrip() for line in f)

 

		# busca en cada linea si existe la cadena a buscar, y si la encuentra

		# la reemplaza

		altered_lines = [reemplazar if line==buscar else line for line in lines]

 

	with open(archivo, "w") as f:

		# guarda nuevamente todas las lineas en el archivo

		f.write('\n'.join(altered_lines) + '\n')

 

modificarLinea("archivo.txt","casa","avion")
