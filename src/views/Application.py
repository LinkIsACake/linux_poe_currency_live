from tkinter import *
from tkinter import ttk

from .MenuBar import MenuBar
from .CurrencySelector import CurrencySelector


class Application(Tk):
    notebook: ttk.Notebook
    window_label: Label
    menubar: Menu
    menubar_entity: [Menu]
    currencySelector: CurrencySelector

    def __init__(self,controller):
        print("Create Application")
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.window_label = Label(self, text="Path of exil Currency live")

        self.menubar = MenuBar(self,controller)
        self.config(menu=self.menubar)

        self.currencySelector = CurrencySelector(self,controller.categories)

    def start(self):
        self.mainloop()

    def add_items(self,nom,categorie,id):
            self.currencySelector.add_item(nom,categorie,id)