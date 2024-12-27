from tkinter import *
from PIL import ImageTk,Image

root = Tk()
def forward(image_num):
    global my_label
    global back_button
    global next_button
    
    my_label.grid_forget()
    my_label = Label(image=img_list[image_num-1])
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
    my_label = Label(image=img_list[image_num-1])
    back_button = Button(root,text="<<", command=lambda:back(image_num-1))
    next_button = Button(root, text=">>", command=lambda:forward(image_num+1))
    if image_num == 1:
        back_button = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

img1 = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/pasta.jpg"))
img2 = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/burger.png"))
img3 = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/ribs.jpg"))
img4 = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/dice.png"))

my_label = Label(image = img1)
my_label.grid(row=0,column=0,columnspan=3)

img_list = [img1, img2, img3, img4]

back_button = Button(root,text="<<", command=back, state=DISABLED)
next_button = Button(root, text=">>", command=lambda:forward(2))

back_button.grid(row=1,column=0)
next_button.grid(row=1,column=2)

root.mainloop()