from functions import *
from tkinter import *
from tkinter import ttk

def GetNames():
    a = text1.get()
    b = text2.get()
    flames_outcome(a, b)

def flames_outcome(a, b):
    msgbox = Tk()
    msgbox.title("FLAMES_OUTCOME")
    msgbox.geometry("300x100")
    name1 = Label(msgbox, text="Name1: " + a)
    name2 = Label(msgbox, text="Name2: " + b)
    name1.pack()
    L3.pack()
    name2.pack()

    ct = count(a, b)
    r = flames_calc(ct)
    res = result(r)

    outcome = Label(msgbox, text=res)
    outcome.pack()
    

frame1 = Tk()
frame1.title("Flames")
frame1.geometry("300x150")

L1 = Label(frame1, text="Enter first name below")
L2 = Label(frame1, text="Enter second name below")
L3 = Label(frame1, text="")

text1 = Entry(frame1)
text2 = Entry(frame1)

button = Button(frame1, text="Check", command=GetNames)

L1.pack()
text1.pack()
L2.pack()
text2.pack()
L3.pack()
button.pack()

frame1.mainloop()
