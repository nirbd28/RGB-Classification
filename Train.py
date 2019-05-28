######################################## Impot from folder
folder_name='Functions_NN'
import sys
path_name=sys.path[0]
path_name_new=path_name+'\\'+folder_name
sys.path.append(path_name_new)
##### Import Files
import Main_Func,Dif
########################################

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import random
from random import randint
import numpy as np
import matplotlib
import webcolors

### globals
global features
global labels
global length
global i
i=0
###

##### functions

### init functions
def train_btn_enable(enable):
    if enable==0:
        dark_btn.config(state=DISABLED)
        bright_btn.config(state=DISABLED)
    elif enable==1:
        dark_btn.config(state=ACTIVE)
        bright_btn.config(state=ACTIVE)

def other_btn_enable(enable):
    if enable==0:
        create_color_btn.config(state=DISABLED)
        create_color_rnd_btn.config(state=DISABLED)
        add_to_list_btn.config(state=DISABLED)
        load_list_btn.config(state=DISABLED)
        train_btn.config(state=DISABLED)
    elif enable==1:
        create_color_btn.config(state=ACTIVE)
        create_color_rnd_btn.config(state=ACTIVE)
        add_to_list_btn.config(state=ACTIVE)
        load_list_btn.config(state=ACTIVE)
        train_btn.config(state=ACTIVE)

### train
def hex2rgb(hexcode):
    R=hexcode[1] + hexcode[2]
    R=int(R, 16)
    G=hexcode[3] + hexcode[4]
    G=int(G, 16)
    B=hexcode[5] + hexcode[6]
    B=int(B, 16)
    rgb_fun=np.zeros(3)
    rgb_fun[0]=R
    rgb_fun[1]=G
    rgb_fun[2]=B
    return rgb_fun

def train1():
    global i
    global features
    global labels
    global length
    other_btn_enable(0)
    train_btn_enable(1)
    value=listbox.get(i)
    canvas_train.create_rectangle(0, 0, 50, 50 , fill=value)
    length= listbox.size()
    features=np.zeros((length,3))
    labels=np.zeros(length)


def press_dark():
    color_class=0
    train(color_class)
    
def press_bright():
    color_class=1
    train(color_class)
         
def train(color_class):
    global i
    global features
    global labels
    global length

    if i<length:
        value=listbox.get(i)   
        value=hex2rgb(value)

        features[i]=value
        labels[i]=color_class
        i=i+1
        value=listbox.get(i) 
        canvas_train.create_rectangle(0, 0, 50, 50 , fill=value) 
    if i==length:
        messagebox.showinfo("Title", "a Tk MessageBox")

        train_btn_enable(0)
        other_btn_enable(1)
        i=0
        canvas_train.delete("all")
        class_train()

def Norm(x):
    normalize=255
    x=x/normalize
    return x

def class_train():

    x=features
    x=np.transpose(x)
    y=labels
    
    ### normalize
    x=Norm(x)
    
    ########## NN inputs
    itter_num=200
    learning_rate=2
    hidden_layer_n=6
    input_size=3
    output_size=1

    ##### init weights
    w1 = np.random.normal(0, 1, (hidden_layer_n,input_size))
    b1 = np.random.normal(0, 1, (hidden_layer_n,))
    w2 = np.random.normal(0, 1, (output_size,hidden_layer_n))
    b2 = np.random.normal(0, 1, (output_size,))
    ###
    cost,w1, b1, w2, b2=Main_Func.Parameters_OPT(x, y, w1, b1, w2, b2, learning_rate, itter_num)
    
    ### save txt files
    path_name=sys.path[0]+'\Parameters'
    np.savetxt(path_name+'\\'+'w1'+'.txt', w1,fmt='%0.5f', delimiter=',')
    np.savetxt(path_name+'\\'+'b1'+'.txt', b1,fmt='%0.5f', delimiter=',')
    np.savetxt(path_name+'\\'+'w2'+'.txt', w2,fmt='%0.5f', delimiter=',')
    np.savetxt(path_name+'\\'+'b2'+'.txt', b2,fmt='%0.5f', delimiter=',')

    ###
    Main_Func.Check_NN(x, y, w1, b1, w2, b2)

### other 
def load_list():  
    filename = askopenfilename() 
    lines = [line.rstrip('\n') for line in open(filename)]
    length=len(lines)
    for i in range (0 ,length):
        listbox.insert(END,lines[i])
        listbox.itemconfigure(END, background=lines[i])


def add_to_list():
    global RGB
    listbox.insert(END, RGB)
    listbox.itemconfigure(END, background=RGB)

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
               

##### gui
root = Tk()
root.title('Train')
root.geometry("800x600")

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
frame7 = Frame(root)
frame7.pack()
frame8 = Frame(root)
frame8.pack()

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
add_to_list_btn = Button(frame4, text="Add to List", fg="black",command=add_to_list)
add_to_list_btn.pack(side = LEFT)
load_list_btn = Button(frame4, text="Load List", fg="black",command=load_list)
load_list_btn.pack(side = LEFT)

### frame5
canvas=Canvas(frame5,width=50,height=50)
canvas.pack()

### frame6
listbox = Listbox(frame6,height='20')
listbox.pack(side=LEFT)

### frame7
train_btn = Button(frame7, text="Train", fg="black",command=train1)
train_btn.pack(side = LEFT)

### frame8
var = BooleanVar()

canvas_train=Canvas(frame8,width=50,height=50)
canvas_train.pack(side = LEFT)
dark_btn = Button(frame8, text="Dark", fg="red", bg="black",command=press_dark)
dark_btn.pack(side = LEFT)
bright_btn = Button(frame8, text="Bright", fg="red", bg="white",command=press_bright)
bright_btn.pack(side = LEFT)

### program start
train_btn_enable(0)

###
root.mainloop()
