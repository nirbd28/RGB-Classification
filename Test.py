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
global w1
global b1
global w2
global b2

### load parameters
path_name=sys.path[0]+'\Parameters'
w1 = np.loadtxt(path_name+'\\'+'w1'+'.txt', delimiter=',')
b1 = np.loadtxt(path_name+'\\'+'b1'+'.txt', delimiter=',')
w2 = np.loadtxt(path_name+'\\'+'w2'+'.txt', delimiter=',')
b2 = np.loadtxt(path_name+'\\'+'b2'+'.txt', delimiter=',')
b2=np.array([b2])

##### functions

def test_color():
    input=hex2rgb(RGB)
    input=Norm(input)
    output=Main_Func.Predict(input, w1, b1, w2, b2)
    entry_out.delete(0, 'end')
    if output==0:
        str='Dark'
        entry_out.configure({"background": "black"})
    else:
        str='Bright'
        entry_out.configure({"background": "white"})
    entry_out.insert(0, str)
    

def Norm(x):
    normalize=255
    x=x/normalize
    return x

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

    test_color_btn.config(state=ACTIVE)

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

    test_color_btn.config(state=ACTIVE)




##### gui
root = Tk()
root.title('Test')
root.geometry("300x200")

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
test_color_btn = Button(frame3, text="Test Color", fg="black",command=test_color)
test_color_btn.pack(side = LEFT)

### frame4
canvas=Canvas(frame4, width=50,height=50)
canvas.pack()

### frame6
entry_out = Entry(frame5, width =8, fg="red" )
entry_out.delete(0, 'end')
entry_out.pack(side = LEFT)


### program start
RGB=webcolors.rgb_to_hex((0, 0, 0))
canvas.create_rectangle(0, 0, 50, 50 , fill=RGB)
test_color_btn.config(state=DISABLED)

###
root.mainloop()