# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:11:57 2018

@author: miguel
"""

import Tkinter as tk
from PIL import Image, ImageTk
from itertools import cycle

class App(tk.Tk):

    def __init__(self, image_files, x, y, delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x,y))
        self.delay = delay
        #self.pictures = cycle((ImageTk.PhotoImage(file=image), image) for image in image_files)
        self.pictures = cycle(image for image in image_files)        
        self.pictures = self.pictures
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
        self.images = [] # to keep references to images.

    def show_slides(self):        
        img_name = next(self.pictures)
        #image_pil = Image.open(img_name).resize((300, 300)) #<-- resize images here
        image_pil = Image.open(img_name).resize((400, 300))
        
        self.images.append(ImageTk.PhotoImage(image_pil))      

        self.picture_display.config(image=self.images[-1])
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()

delay = 3500
image_files = ['01.JPG','02.JPG','03.JPG','04.JPG']

x = 400
y = 300
app = App(image_files,x,y,delay)
app.show_slides()
app.run()