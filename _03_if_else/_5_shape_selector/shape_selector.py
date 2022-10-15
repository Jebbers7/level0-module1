import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    carlitos = turtle.Turtle()
    carlitos.speed = 100
    # Ask the user what shape they want to draw and store it in a variable
    r = simpledialog.askstring("Question", "What shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if r == "triangle":
        for i in range(3):
            carlitos.forward(100)
            carlitos.left(120)
            i = i + 1
    elif r == "square":
        for i in range(4):
            carlitos.forward(100)
            carlitos.left(90)
            i = i + 1
    elif r == "circle":
        for i in range(360):
            carlitos.forward(1)
            carlitos.left(1)
    # Call the turtle .done() method

