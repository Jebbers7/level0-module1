"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if they would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    sum = 0
    diff = 0
    product = 0
    quotient = 0


    r = simpledialog.askinteger('Number', 'Please enter a number')
    r2 = simpledialog.askinteger('Number 2', 'Please enter a second number')

    o = simpledialog.askstring('Operation', 'Would you like to add, subtract, multiply, or divide these numbers?')

    if o == 'add':
        sum = r + r2
        messagebox.showinfo('Sum', 'The sum of the numbers is ' + str(sum))
    elif o == 'subtract':
        diff = r - r2
        messagebox.showinfo('Difference', 'The difference of the numbers is ' + str(diff))
    elif o == 'multiply':
        product = r * r2
        messagebox.showinfo('Product', 'The product of the numbers is ' + str(product))
    elif o == 'divide':
        quotient = r / r2
        messagebox.showinfo('Quotient', 'The quotient of the numbers is ' + str(quotient))
