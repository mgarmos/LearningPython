
name = input('Please, insert your name: ')
age = int(input('Please, insert your age: '))

from datetime import datetime
actualYear = datetime.now().year

anio100 = actualYear + 100 - age

print(actualYear)
print(name)
print(anio100);
