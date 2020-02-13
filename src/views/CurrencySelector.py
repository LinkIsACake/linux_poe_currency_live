import logging
from tkinter import *
from tkinter.ttk import Notebook
from tkinter.ttk import Frame
from tkinter.ttk import Checkbutton

from .Categorie import Categorie


class CurrencySelector(Notebook):
    logger = logging.getLogger(__name__)
    categories: {}
    itembuttons: []

    def __init__(self, context, categoeries):

        self.logger.info("Create currency Selector")
        super().__init__(context)

        self.categories = {}
        itembuttons = []

        for categorie in categoeries:
            self.categories[categorie] = Categorie(self, categorie)
            self.add(self.categories[categorie], text=categorie)

        self.grid(row=0, column=len(self.categories) - 1, sticky="n")

    def add_item(self, name, categories, id):
        contexts = []

        for categorie in categories:
            contexts.append(self.categories.get(categorie, None))
        for context in contexts:
            if context:
                context.add_item(context, name, id)
