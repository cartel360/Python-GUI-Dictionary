import json
from difflib import get_close_matches as g

data = json.load(open("data.json"))
keys = data.keys()


def meaning():
    w = e1_value.get()

    if w in data:
        for i, j in enumerate(data[w]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.upper() in data: #in case user enters words like USA or NATO
        for i, j in enumerate(data[w.upper()]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        for i, j in enumerate(data[w.title()]):
            t1.insert(END,str(i)+' '+j+'\n')
    else:
        list=g(w,keys,n=1,cutoff=0.8)
        if len(list) == 0:
            t1.insert(END, "The word doesn't exist. Please double check it.")
        else:
            real=list[0]
            answer=tkinter.messagebox.askquestion("Word Suggestion", "Is Your Word "+real+"?")

            if answer == "yes":
                for i, j in enumerate(data[real]):
                    t1.insert(END,str(i)+' '+j+'\n')
            else:
                t1.insert(END,"Apologies, No Word Found, Please Recheck Your Input Word.")


def meaning2():
    t1.delete(1.0,END)
    e1.delete(0,END)

    meaning


from tkinter import *
import tkinter.messagebox



gui= Tk()
gui.wm_title("Simple Dictionary")



l1=Label(gui,text="Enter Your Word")
l1.grid(row=0,column=0)


e1_value=StringVar()
e1=Entry(gui,textvariable=e1_value)
e1.grid(row=0,column=1,ipadx=100,pady=10)

b1=Button(gui,text="Find Meaning!",command=meaning,bg="light green",fg="red")
b1.grid(row=1,column=0,columnspan=8,ipadx=10,pady=10)

t1=Text(gui,height=10,width=70)
t1.grid(row=2,column=0,columnspan=8)

l2=Label(gui,text="Hit the Button Below to Search Another Word")
l2.grid(row=3,column=0,columnspan=8)

b2=Button(gui,text="Another Word!",command=meaning2,bg="light green",fg="red")
b2.grid(row=4,column=0,columnspan=8,ipadx=10,pady=5)

gui.mainloop()
