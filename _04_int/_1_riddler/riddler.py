"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    score = 0

    r1 = simpledialog.askstring('Riddle #1', 'What gets wet while it dries?')
    if r1 == 'towel':
        score = score + 1
    r2 = simpledialog.askstring('Riddle #2', 'What has a mouth but never talks, has a head but never weeps, and has a bed but never sleeps?')
    if r2 == 'river':
        score = score + 1
    r3 = simpledialog.askstring('Riddle #3', 'If the english alphabet goes from A to Z, what goes from Z to A?')
    if r3 == 'zebra':
        score = score + 1

    messagebox.showinfo('Score', 'You answered ' + str(score) + ' riddles correct!')
