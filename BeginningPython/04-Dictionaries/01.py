# -*- coding: utf-8 -*-

import random

phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook["Alice"]) # 

#The dict Function -> #crea diccionario a partir de una lista de items
items = [('name', 'Gumby'), ('age', 42)]
dictPerson = dict(items)
print(dictPerson)

print(dictPerson.items())

print(dictPerson.keys())



lista = ['perro', 'gato', 'pajaro']
print(random.choices(lista,k=2))


group_of_items = {1, 2, 3, 4}               # a sequence or set will work here.
num_to_select = 2                          # set the number to select here.
list_of_random_items = random.sample(group_of_items, num_to_select)
# first_random_item = list_of_random_items[0]
# second_random_item = list_of_random_items[1] 
print(list_of_random_items)

print('s' in 'HelloWords')

print(', #'.join(random.sample(lista,3)))

print('hello'.upper().center(50).replace(' ','-'))
