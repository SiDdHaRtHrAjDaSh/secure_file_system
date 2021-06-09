# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 01:27:31 2021

@author: Siddharth Raj dash
"""

# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('100x100')
 

    
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5',
                          command = add)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()