import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    r = simpledialog.askstring("Birthday", "When is your birthday? (mm/dd) format please")
    if r == "10/14":
        messagebox.showinfo("It's your birthday!", "Happy Birthday!")
    else:
        messagebox.showinfo("It's not your birthday, but", "Happy UNBirthday!")
