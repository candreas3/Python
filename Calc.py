import tkinter
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x400")


def stop():
    exit()


def hello():
    messagebox.showinfo("Say Hello", "Hello World")


B1 = Button(top, text="Say Hello", command=hello)
B2 = Button(top, text="Cancel", command=stop)

B2.place(x=120, y=50)
B1.place(x=35, y=50)

top.mainloop()

