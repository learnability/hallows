from functions import *
from Tkinter import *
import MySQLdb as sql



def GetNames():
    a = text1.get()
    b = text2.get()
    
    db = sql.connect("192.168.62.223", "shrish", "shrishty", "FLAMES")
    cursor = db.cursor()
    
    cmd = """ INSERT INTO entries(name1, name2)
    		  VALUES ('%s', '%s')""" % (a, b)
  
    cursor.execute(cmd)
    db.commit()
    
    db.close()
    
    flames_outcome(a, b)
    
def keyEnter(event):
	GetNames()

def keyEsc(event):
	frame1.destroy()

def flames_outcome(a, b):
    msgbox = Tk()
    msgbox.title("FLAMES_OUTCOM`E")
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
frame1.bind("<Return>", keyEnter)
frame1.bind("<Escape>", keyEsc)

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
