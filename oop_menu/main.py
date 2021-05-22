# main class using tkinter
# import all lib
from tkinter import *
from tkinter.ttk import *
import calculator


# create TK() object
master = Tk()

# set main geometry of the main window
master.geometry("200x200")

label = Label(master, text="This is the main window")
label.pack(side=TOP, pady=10)

# button to open new window 
btn = Button(master, text="click me!")
btn.bind("<Button>", lambda e: calculator.Calculator(master))

btn.pack(pady=10)

# run main loop 
master.mainloop()