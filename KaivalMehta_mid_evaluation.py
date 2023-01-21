from tkinter import *
from tkinter import filedialog
from tkinter import font

#DECLARING LIST OF FONTS AND SIZE
fontlist=[]
sizelist=[2,4,6,8,10,12,14,15,16,18,20,24,28,32,36,40,44,50]

#DECLARING DEFAULT FONT SIZE AND TYPE
size=20
fontname='Arial'

root=Tk()
root.title("Checkpoints")
root.geometry("1000x800")


global name 
name=False

#VARIABLES FOR STYLE MENU
bold=IntVar()
italic=IntVar()
underline=IntVar()

#FUNCTIONS USED IN SEVERAL COMMANDS

def newfile():             #CREATING A NEW FILE
    mytext.delete("1.0",END)
    global name
    name=False
    root.title('Untitled')
def openfile():            #OPEN AN EXISTING FILE
    mytext.delete("1.0",END)
    txtfile=filedialog.askopenfilename(initialdir="C:/Downloads/",title="Open File",filetypes=(("Text Files","*.txt"),("PDF","*.pdf")))
    root.title(txtfile)
    global name
    name=txtfile
    txtfile=open(txtfile,'r')
    data=txtfile.read()
    mytext.insert(END,data)
    txtfile.close()

def saveas():               #SAVING CHANGES AND CREATING A FILE
    txtfile=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/Downloads/",title="Save File",filetypes=(("Text Files","*.txt"),("PDF","*.pdf")))
    root.title(txtfile)
    txtfile=open(txtfile,'w')
    txtfile.write(mytext.get(1.0,END))
    txtfile.close()
def savefile():             # SAVING CHANGES IN AN EXISTING FILE OR SAVING AS NEW FILE IF FILE DOESNT EXIST
    global name
    if name :
        txtfile=open(name,'w')
        txtfile.write(mytext.get(1.0,END))
        txtfile.close
    else :
        saveas()
def changefont(fonttype):   # FOR CHANGING FONT TYPE OF THE TEXT
    global fontname
    fontname=fonttype
    mytext.config(font=(fonttype,size))

def changesize(sizeno):     # FOR CHANGING SIZE OF THE TEXT
    global fontname
    global size
    size=sizeno
    mytext.config(font=(fontname,size))

def style():                # FOR CHANGING STYLE OF THE TEXT
    global fontname
    global size
    mytext.tag_configure("bold", font=(fontname, size, "bold"))
    mytext.tag_configure("italic", font=(fontname, size, "italic"))
    mytext.tag_configure("underline", font=(fontname, size, "underline"))
    mytext.tag_configure("bolditalic", font=(fontname, size, "bold italic"))
    mytext.tag_configure("boldunderline", font=(fontname, size, "bold underline"))
    mytext.tag_configure("italicunderline", font=(fontname, size, "italic underline"))
    mytext.tag_configure("bolditalicunderline", font=(fontname,size, "bold italic underline"))
    mytext.tag_remove("bold", "1.0", "end")
    mytext.tag_remove("italic", "1.0", "end")
    mytext.tag_remove("underline", "1.0", "end")
    mytext.tag_remove("bolditalic", "1.0", "end")
    mytext.tag_remove("boldunderline", "1.0", "end")
    mytext.tag_remove("italicunderline", "1.0", "end")
    mytext.tag_remove("bolditalicunderline", "1.0", "end")
    if bold.get() == 1 and italic.get() == 1 and underline.get() == 1:
        mytext.tag_add("bolditalicunderline", "1.0", "end")
    elif bold.get() == 1 and italic.get() == 1:
        mytext.tag_add("bolditalic", "1.0", "end")
    elif bold.get() == 1 and underline.get() == 1:
        mytext.tag_add("boldunderline", "1.0", "end")
    elif italic.get() == 1 and underline.get() == 1:
        mytext.tag_add("italicunderline", "1.0", "end")
    elif bold.get() == 1:
        mytext.tag_add("bold", "1.0", "end")
    elif italic.get() == 1:
        mytext.tag_add("italic", "1.0", "end")
    elif underline.get() == 1:
        mytext.tag_add("underline", "1.0", "end")
    else:
        mytext.config(font=(fontname, size))


#CREATING FRAME
myframe=Frame(root)
myframe.pack(pady=5)
myframe.grid_propagate(False)

#CREATING TEXTBOX
mytext=Text(myframe,width=80,height=30,font=("Arial",size))
mytext.config(width=300,height=200)
mytext.pack()

#CREATING MAIN MENU
mymenu=Menu(root)
root.config(menu=mymenu)

#DECLARING SUBMENUS
filemenu=Menu(mymenu,tearoff=False)
fontmenu=Menu(mymenu,tearoff=False)
sizemenu=Menu(mymenu,tearoff=False)
stylemenu=Menu(mymenu,tearoff=False)

#DISPLAYING SUBMENUS
mymenu.add_cascade(label="File",menu=filemenu)
mymenu.add_cascade(label="Change Font",menu=fontmenu)
mymenu.add_cascade(label="Change Size",menu=sizemenu)
mymenu.add_cascade(label="Change Style",menu=stylemenu)

#ADDING FUNCTIONS TO THE FILE SUBMENU
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save As",command=saveas)
filemenu.add_command(label="Save",command=savefile)

#LIST OF ALL FONT TYPES
for i in font.families():
    fontlist.append(i)

default=StringVar()
default.set(fontlist[0])

#ADDING FONTS TO THE FONT SUBMENU
for fonttype in fontlist :
    fontmenu.add_radiobutton(label=fonttype,command=lambda  fonttype=fonttype: changefont(fonttype))

#ADDING SIZES TO THE SIZE SUBMENU
for sizeno in sizelist :
    sizemenu.add_radiobutton(label=sizeno,command=lambda sizeno=sizeno: changesize(sizeno))

#ADDING STYLES TO THE STYLE SUBMENU
stylemenu.add_checkbutton(label="Bold", variable=bold, command=lambda: style())
stylemenu.add_checkbutton(label="Italic", variable=italic, command=lambda: style())
stylemenu.add_checkbutton(label="Underline", variable=underline, command=lambda: style())

root.mainloop()