# calculator class using tkinter
# import lib
from tkinter import *
from tkinter.ttk import * 

class Calculator:
    def __init__(self, master=None):
        self.master = master
        label = Label(self, text="This is a new window")
        label.pack()

    '''
    def __init__(self, master = None):
        self.master = master

    def newWindow(self):
        new_window = Toplevel(self.master)

        new_window.title("New Window")

        new_window.geometry("200x200")

        Label(new_window, text="This is a new window").pack()
        return None
    '''
