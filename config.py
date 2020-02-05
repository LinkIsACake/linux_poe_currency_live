# coding: utf-8
import json
from tkinter import *
from tkinter import ttk

import requests
import os
import sys

url = "https://api.poe.watch/get?category=currency&league=Metamorph"
path = "/tmp/poe_currency_live"
max_row = 30

grid_columns = {
    'Orb': [],
    'Shard': [],
    'Oil': [],
    'Essence': [],
    'Fossil': [],
    'Resonator': [],
    'Incubator': [],
    'Catalyst': [],
}

Checkbuttons = []


def request_all_currrency():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error request", response.status_code)

def valider():
    global Checkbuttons
    choices = []
    f = open(path+"/choice.json","w")

    for checkbox in Checkbuttons:
        if checkbox[1].get() == 1:
            choices.append(checkbox[0])

    f.write(json.dumps(choices))

    sys.exit(1)

def configure_grid_list_data(options):
    for option in options:
        for categorie, items in grid_columns.items():
            if option[0].find(categorie) != -1:
                grid_columns[categorie].append(option)

def configure_grid_list(n):


    y = 0
    overload_y=0
    for categories,items in grid_columns.items():
        i = 3
        onglet = ttk.Frame(n)
        n.add(onglet, text=categories)
        n.grid(row=0, column=y+overload_y, sticky="nw")
        #Label(fenetre,text=categories).grid(row=2, column=y+overload_y, sticky=W)
        for item in items:
            var = IntVar()
            Checkbuttons.append([item[1], var])
            Checkbutton(onglet, text=item[0], variable=var).grid(row=i, column=y+overload_y, sticky=W)
            i += 1
            if i == max_row:
                i=3
                overload_y += 1
        y += 1

def load_options():
    options = None
    if not os.path.isdir(path):
        print(path," don't existe, create")
        os.mkdir(path)

    if os.path.isfile(path+"/options.json"):
        print("options.json exist, load")
        f = open(path+"/options.json", "r")
        data = f.read()
        options = json.loads(data)
    else:
        print("options.json not exist, downloads")
        list_currency = request_all_currrency()
        options = [[currency["name"], currency["id"]] for currency in list_currency]
        f = open(path+"/options.json", 'w')
        f.write(json.dumps(options))

    return options

def resize(event):
    global max_row
    if event.height > 400:
        max_row = 40
        configure_grid_list()
    elif event.height < 300:
        max_row = 30
    elif event.height < 200:
        max_row = 20


if __name__ == '__main__':

    options = load_options()

    if options is not None:
        fenetre = Tk()
        #fenetre.bind('<Configure>', resize)
        n = ttk.Notebook(fenetre)
        label = Label(fenetre, text="Currency sellector")
        configure_grid_list_data(options)
        configure_grid_list(n)

        menubar = Menu(fenetre)
        fenetre.config(menu=menubar)
        menuvalider = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Action", menu=menuvalider)
        menuvalider.add_command(label="Enregistrer" ,command=valider)
        fenetre.mainloop()
    else:
        print("Error load options !")
