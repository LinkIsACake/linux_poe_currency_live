from tkinter import Menu
from tkinter import Tk

from .MenuAction import MenuAction
import sys
sys.path.append('..')

from controllers import Controller

class MenuBar(Menu):
    actions: [MenuAction]
    controller: Controller

    def __init__(self, context: Tk,controller):
        super().__init__(context)
        self.actions = []
        self.controller = controller

        menuaction = MenuAction(self,"Action")

        self.actions.append(menuaction)
        for action in self.actions:
            self.add_cascade(label=action.label, menu=action)

        menuaction.add_command(label="Save",command=controller.save)
        menuaction.add_command(label="Quit",command=controller.quit)

