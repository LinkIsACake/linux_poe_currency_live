from tkinter import *
from tkinter import ttk

from .MenuBar import MenuBar

class Application(Tk):
    notebook : ttk.Notebook
    window_label: Label
    menubar: Menu
    menubar_entity: [Menu]
    def __init__(self):
        super().__init__()
        self.notebook = ttk.Notebook(self)
        self.window_label = Label(self, text="Path of exil Currency live")

        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)

    def start(self):
        self.mainloop()

