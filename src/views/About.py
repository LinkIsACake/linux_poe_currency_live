from tkinter import *
from tkinter import ttk
from tkinter import Text

class About(Tk):

    def __init__(self,controller):
        print("Create About")
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.window_label = Label(self, text="Path of exil Currency live")

        text = Text(self, height=20, width=35)
        text.pack()
        text.insert(END, "About this application : \nVersion : 0.0.1\nCreated by : Léo Sudreau")
    def start(self):
        self.mainloop()
