# -*- coding: utf-8 -*-

"""
Membership 
To check whether a value can be found in a sequence, you use the in operator
It checks whether something is true and returns a value 
accordingly: True for true and False for false
"""
permissions = 'rw'
print('w' in permissions) #True
print('x' in permissions) #False
print('rw' in permissions) #True
print('wr' in permissions) #False

#List of lists
database = [
    ['albert',  '1234'],
    ['dilbert', '4242'],
    ['smith',   '7524'],
    ['jones',   '9843']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')
if [username, pin] in database:
    print('Access granted')
else:
    print('Access denied')
