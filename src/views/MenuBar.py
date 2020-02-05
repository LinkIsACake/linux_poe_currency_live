from tkinter import Menu
from tkinter import Tk

from .MenuAction import MenuAction

class MenuBar(Menu):
    actions: [MenuAction]

    def __init__(self, context: Tk):
        super().__init__(context)
        self.actions = []

        menuaction = MenuAction(self,"Action")

        self.actions.append(menuaction)
        for action in self.actions:
            self.add_cascade(label=action.label,menu=action)

        menuaction.add_command(label="Enregistrer")

