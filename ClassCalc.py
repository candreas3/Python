import tkinter
from tkinter import *

from tkinter import messagebox

class DrawCalc:

    window = Tk()
    display = Text(window, height=1, width=20)
    value = ""

    def __init__(self):
        DrawCalc.window.geometry("200x400")

    def value1(self, val):
        DrawCalc.value = DrawCalc.value + val
        DrawCalc.display.index(index)
        DrawCalc.display.insert(INSERT, DrawCalc.value)


    def stop(self):
        exit()

    def hello(self):
        messagebox.showinfo("Say Hello", "Hello World")

    def draw(self):
        B1 = Button(DrawCalc.window, text="Say Hello", command=self.hello)
        B2 = Button(DrawCalc.window, text="Cancel", command=self.stop)
        B9 = Button(DrawCalc.window, text="9", command=lambda x="9": self.value1(x))

        B2.place(x=120, y=350)
        B1.place(x=35, y=350)
        B9.place(x=120, y=100)

        DrawCalc.display.place(x=35, y=50)

        DrawCalc.window.mainloop()


calc = DrawCalc()
calc.draw()
