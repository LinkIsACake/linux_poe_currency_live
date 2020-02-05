from tkinter import Menu
from tkinter import Tk


class MenuAction(Menu):
    label: str

    def __init__(self, context: Menu,label: str):
        super().__init__(context,tearoff=0)
        self.label = label
