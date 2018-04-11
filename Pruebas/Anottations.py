# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:47:11 2018

@author: miguel
"""

my_file = open('My Clippings.txt','r')
print(my_file.read(26))

#for line in my_file:
#    print line
print( 'El nombre es: ' + my_file.name)
my_file.close()
