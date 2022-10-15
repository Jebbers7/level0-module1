from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name1 = 'jimmy'
    name2 = 'fred'
    name3 = 'alan'

    r = simpledialog.askstring("Name", "What is your name?")

    if r == name1:
        messagebox.showinfo("Dogs", "You have 20 dogs!")
    elif r == name2:
        messagebox.showinfo("Whales", "You are really interested in whale behavior!")
    elif r == name3:
        messagebox.showinfo("Sports", "You love sports!")

