from tkinter import *

root=Tk()
e=Entry(root,width=12,font='Arial  45')
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)

def add():
    global first
    global math 

    math='add'
    first=int(e.get())
    e.delete(0,END)
def add():
    global first
    global math 

    math='add'
    first=float(e.get())
    e.delete(0,END)
def sub():
    global first
    global math 

    math='sub'
    first=float(e.get())
    e.delete(0,END)
def mult():
    global first
    global math 

    math='mult'
    first=float(e.get())
    e.delete(0,END)
def div():
    global first
    global math 

    math='div'
    first=float(e.get())
    e.delete(0,END)

def equal():
    second=float(e.get())
    e.delete(0,END)
    if math=='add':
        e.insert(0,first+second)
    if math=='sub':
        e.insert(0,first-second)
    if math=='mult':
        e.insert(0,first*second)
    if math=='div':
        e.insert(0,first/second)
button1=Button(root,text='1',padx=40,pady=20,command=lambda : click(1),font='Georgia 20').grid(row=3,column=0)
button2=Button(root,text='2',padx=40,pady=20,command=lambda : click(2),font='Georgia 20').grid(row=3,column=1)
button3=Button(root,text='3',padx=40,pady=20,command=lambda : click(3),font='Georgia 20').grid(row=3,column=2)
button4=Button(root,text='4',padx=40,pady=20,command=lambda : click(4),font='Georgia 20').grid(row=2,column=0)
button5=Button(root,text='5',padx=40,pady=20,command=lambda : click(5),font='Georgia 20').grid(row=2,column=1)
button6=Button(root,text='6',padx=40,pady=20,command=lambda : click(6),font='Georgia 20').grid(row=2,column=2)
button7=Button(root,text='7',padx=40,pady=20,command=lambda : click(7),font='Georgia 20').grid(row=1,column=0)
button8=Button(root,text='8',padx=40,pady=20,command=lambda : click(8),font='Georgia 20').grid(row=1,column=1)
button9=Button(root,text='9',padx=40,pady=20,command=lambda : click(9),font='Georgia 20').grid(row=1,column=2)
button0=Button(root,text='0',padx=40,pady=20,command=lambda : click(0),font='Georgia 20').grid(row=4,column=1)
button_add=Button(root,text='+',padx=40,pady=20,command=add,font='Georgia 20').grid(row=1,column=3)
button0_sub=Button(root,text='-',padx=40,pady=20,command=sub,font='Georgia 20').grid(row=2,column=3)
button0_mult=Button(root,text='X',padx=40,pady=20,command=mult,font='Georgia 20').grid(row=3,column=3)
button0_div=Button(root,text='/',padx=40,pady=20,command=div,font='Georgia 20').grid(row=4,column=3)
button0_clr=Button(root,text='A/C',padx=40,pady=20,command=clear,font='Georgia 20').grid(row=4,column=0)
button0_eq=Button(root,text='=',padx=40,pady=20,command=equal,font='Georgia 20').grid(row=4,column=2)


root.mainloop()