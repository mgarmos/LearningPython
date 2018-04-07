# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:52:07 2018

@author: miguel
"""

from Tkinter import *
from PIL import ImageTk, Image
#import os

root = Toplevel()
img = ImageTk.PhotoImage(Image.open("01.JPG"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")
root.mainloop()