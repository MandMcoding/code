from tkinter import *
from PIL import ImageTk,Image

root = Tk()
def forward(image_num):
    global my_label
    global back_button
    global next_button
    
    my_label.grid_forget()
    my_label = lab_list[image_num-1]
    back_button = Button(root,text="<<", command=lambda:back(image_num-1))
    next_button = Button(root, text=">>", command=lambda:forward(image_num+1))
    if image_num == 4:
        next_button = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)
    
def back(image_num):
    global my_label
    global back_button
    global next_button
    
    my_label.grid_forget()
    my_label = lab_list[image_num-1]
    back_button = Button(root,text="<<", command=lambda:back(image_num-1))
    next_button = Button(root, text=">>", command=lambda:forward(image_num+1))
    if image_num == 1:
        back_button = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

lab1 = Label(root,text="Hello")
lab2 = Label(root,text="my")
lab3 = Label(root,text="name is")
lab4 = Label(root,text="joe")

my_label = lab1
my_label.grid(row=0,column=0,columnspan=3)

lab_list = [lab1, lab2, lab3, lab4]

back_button = Button(root,text="<<", command=back, state=DISABLED)
next_button = Button(root, text=">>", command=lambda:forward(2))

back_button.grid(row=1,column=0)
next_button.grid(row=1,column=2)

root.mainloop()