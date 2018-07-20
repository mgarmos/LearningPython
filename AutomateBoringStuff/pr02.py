import pyperclip, re

mensaje = pyperclip.paste()
print (mensaje)

patron = re.compile(r'class=".*?"')
clases = patron.findall(mensaje)
clasesSinRepetir = list(set(clases))




print("Numero de clases: " + str(len(clases)))
print("Numero de clases sin repetri: " + str(len(clasesSinRepetir)))
# print(patron.findall(mensaje))