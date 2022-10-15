"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter
if __name__ == '__main__':

    root = Tk()

    canvas = Canvas(root, width=200, height=200, bg="#FF00FF");
    canvas.grid()

    '''
    Text Rendering Example:
                        x    y                                                       
    canvas.create_text(100, 50, text="text goes here", font=("Arial", 16))
    '''
    # Put your code below
    text = 'banana'
    for i in range(4):
        canvas.create_text(100, 100 - (25 * i), text=text, font=('Arial', 16))
        if i == 0:
            text = 'ice cream'
        i = i + 1

    root.mainloop()
