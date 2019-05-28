from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import random
from random import randint
import numpy as np
import matplotlib
import webcolors
###

### functions

def chosen_listbox():
    choose_listbox_val=choose_listbox.get()
    if choose_listbox_val=='1':
        x=color_listbox1
    elif choose_listbox_val=='2':
        x=color_listbox2
    elif choose_listbox_val=='3':
        x=color_listbox3
    return x

def load_list():
    x=chosen_listbox()    
    filename = askopenfilename() 
    lines = [line.rstrip('\n') for line in open(filename)]
    length=len(lines)
    for i in range (0 ,length):
        x.insert(END,lines[i])
        x.itemconfigure(END, background=lines[i])


def save_list():  
    x=chosen_listbox()
    length=x.size()
    list_mat=['']*length
    for index in range (0 ,length):
        list_mat[index]=(x.get(index))

    filename = input('Enter a file name: ')
    filename= filename + '.txt'
    outF = open(filename, "w")
    for line in list_mat:
        outF.write(line)
        outF.write("\n")
    outF.close()


def add_to_list():
    global RGB
    x=chosen_listbox()
    x.insert(END, RGB)
    x.itemconfigure(END, background=RGB)


def create_color():
    global RGB
    R = int(entry_red.get())
    G = int(entry_green.get())
    B = int(entry_blue.get())
    if (R>255 or R<0) or (G>255 or G<0) or (B>255 or B<0): 
        messagebox.showinfo("Error", "RGB value range is 0-255")
    else:
        RGB=webcolors.rgb_to_hex((R, G, B))
        canvas.create_rectangle(0, 0, 50, 50 , fill=RGB)

def create_color_rnd():
    global RGB
    R=randint(0, 255) 
    G=randint(0, 255) 
    B=randint(0, 255) 
    entry_red.delete(0,END)
    entry_red.insert(0,str(R))
    entry_green.delete(0,END)
    entry_green.insert(0,str(G))
    entry_blue.delete(0,END)
    entry_blue.insert(0,str(B))
    RGB=webcolors.rgb_to_hex((R, G, B))
    canvas.create_rectangle(0, 0, 50, 50 , fill=RGB)
               

###
root = Tk()
root.title('Create Pallet')
root.geometry("800x500")

### frames
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack()
frame6 = Frame(root)
frame6.pack()

### frame1
red_label = Label(frame1, text="Red", fg="red")
red_label.pack( side = LEFT)

green_label = Label(frame1, text="Green", fg="green")
green_label.pack( side = LEFT )

blue_label = Label(frame1, text="Blue", fg="blue")
blue_label.pack( side = LEFT )

### frame2
entry_red = Entry(frame2, width =5 )
entry_red.insert(0, "0")
entry_red.pack(side = LEFT)

entry_green = Entry(frame2, width =5)
entry_green.insert(0, "0")
entry_green.pack(side = LEFT)

entry_blue = Entry(frame2, width =5)
entry_blue.insert(0, "0")
entry_blue.pack(side = LEFT)

### frame3
create_color_btn = Button(frame3, text="Create Color", fg="black",command=create_color)
create_color_btn.pack(side = LEFT)
create_color_rnd_btn = Button(frame3, text="Random Color", fg="black",command=create_color_rnd)
create_color_rnd_btn.pack(side = LEFT)


### frame4
list_label=Label(frame4, text='List Index:')
list_label.pack(side = LEFT)
choose_listbox = Spinbox(frame4, from_=1, to=3, width=3)
choose_listbox.pack(side = LEFT)
add_to_list_btn = Button(frame4, text="Add to List", fg="black",command=add_to_list)
add_to_list_btn.pack(side = LEFT)
save_list_btn = Button(frame4, text="Save List", fg="black",command=save_list)
save_list_btn.pack(side = LEFT)
load_list_btn = Button(frame4, text="Load List", fg="black",command=load_list)
load_list_btn.pack(side = LEFT)


### frame5
canvas=Canvas(frame5,width=50,height=50)
canvas.pack()


### frame6
color_listbox1 = Listbox(frame6,height='50')
color_listbox1.pack(side=LEFT)
color_listbox2 = Listbox(frame6,height='50')
color_listbox2.pack(side=LEFT)
color_listbox3 = Listbox(frame6,height='50')
color_listbox3.pack(side=LEFT)

###
root.mainloop()
