from tkinter import *
from tkinter.ttk import *

from time import strftime

R = Tk()
R.title ("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text = string)
    label.after (1000,time)

label = Label(R,font = ("Arial", 100), background = "black", foreground = "yellow")
label.pack (anchor = "center")

time()
mainloop()
