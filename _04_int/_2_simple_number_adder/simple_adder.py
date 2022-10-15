"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    r = simpledialog.askinteger("Number", "Please enter a number")
    r2 = simpledialog.askinteger('Number', 'Please enter a second number')

    sum = r + r2
    messagebox.showinfo('Sum', sum)
