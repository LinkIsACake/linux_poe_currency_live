from tkinter.ttk import Frame
from tkinter import Tk, Checkbutton
import logging

class Categorie(Frame):
    name: str
    items: []
    logger = logging.getLogger(__name__)
    collumns = 0
    row = 0
    def __init__(self, context: Tk, name: str):
        super().__init__(context)
        self.name = name
        self.items = []
        self.logger.info("Create %s categorie", name)

    def add_item(self, context, name, id):
        self.items.append(Checkbutton(context, text=name).grid(
            row=self.row,
            column=self.collumns)
        )
        if self.row == 20:
            self.collumns+=1
            self.row = 0
        else:
            self.row += 1