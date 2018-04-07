# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:19:55 2018

@author: miguel
"""

#from Tkinter import *
#top = Tk()
#top.mainloop()

from PIL import Image
im = Image.open("01.JPG")
im.rotate(45).show()