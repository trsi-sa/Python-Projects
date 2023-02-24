from tkinter import *
from tkinter.ttk import *
from time import strftime

wn = Tk()
wn.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(wn, font=("Ds-Digital", 80), background="black", foreground="blue")
label.pack(anchor="center")
time()

mainloop()