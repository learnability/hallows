from functions import *
from Tkinter import *
import MySQLdb as sql
import thread
import threading
import re
from mechanize import Browser


def GetNames():
    a = text1.get()
    b = text2.get()
    

    try:
        #thread.start_new_thread( access_db, (a, b))
        thread.start_new_thread( browser_ac, (a, b))
    except:
        print "Something went wrong :("
    flames_outcome(a, b)
    
    
def keyEnter(event):
	GetNames()

def keyEsc(event):
	frame1.destroy()

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

def access_db(a, b):
    try:
        db = sql.connect("xxxx", "xxxx", "xxxx", "xxxx")
        print "connected"
        cursor = db.cursor()
        cmd = """ INSERT INTO FLAMES_ENTRIES(name1, name2)
    		  VALUES ('%s', '%s')""" % (a, b)
  
        cursor.execute(cmd)
        db.commit()
    
        db.close()
    except:
        print "SOMETHING WENT WRONG \n"

def browser_ac(a, b):
    try:
        br = Browser()
        br.open("http://athena.nitc.ac.in/~shrishty_bcs11/test/index.html")
        br.select_form(nr=0)
        br["name1"] = a
        br["name2"] = b
        br.submit()
    except:
        print "OH NO!!"

        try:
            name1 = a
            name2 = b

            data = {
                    "name1": a,
                    "name2": b
                }
            encoded_data = urllib.urlencode(data)
            content = urllib2.urlopen("http://athena.nitc.ac.in/~shrishty_bcs11/test/index.html", encoded_data)
        except:
            print "oh NO here"

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
