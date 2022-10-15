# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
from tkinter import messagebox, simpledialog, Tk
import math
#Area = πr^2
#Circumference = 2πr

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    r = simpledialog.askinteger('Radius', 'Enter a radius')
    q = simpledialog.askstring('Calculation', 'Would you like to calculate the area or circumference of a circle?')
    a = 0
    c = 0

    if q == 'area':
        a = math.pi * (r**2)
        messagebox.showinfo('Area', a)
    elif q == 'circumference':
        c = 2 * r * math.pi
        messagebox.showinfo('Circumference', c)
