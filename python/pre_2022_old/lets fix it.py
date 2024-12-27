from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Flash Cards")
global flash_location = 2
def flashcard_flip_to_front():
    flash_back.grid_forget()
    flash1_front.grid(row=0,column=0, columnspan=3)
    
def flashcard_flip_to_back():
    flash1_front.grid_forget()
    global flash_back
    flash_back = Button(root, image=glue[flash_list[flashcard_number]], command=flashcard_flip_to_front)
    flash_back.grid(row=0,column=0, columnspan=3)

def forward(flashcard_number):
    global flash1_front
    global back_button
    global next_button
    
    global flash_location
    
    flash1_front.grid_forget()
    flash1_front= flash_list[flashcard_number-1]
    next_button = Button(root,text=">>", command=lambda: forward(flashcard_number+1))
    back_button = Button(root,text="<<",command=lambda: back(flashcard_number-1))
    
    if flashcard_number == 3:
        next_button = Button(root, text=">>", state=DISABLED)
        
    flash1_front.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)
    
    flash_location = flash_location + flashcard_number

def back(flashcard_number):
    global flash1_front
    global back_button
    global next_button
    
    global flash_location
    
    flash1_front.grid_forget()
    flash1_front= flash_list[flashcard_number-1]
    next_button = Button(root,text=">>", command=lambda: forward(flashcard_number+1))
    back_button = Button(root,text="<<",command=lambda: back(flashcard_number-1))
    
    if flashcard_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)
        
    flash1_front.grid(row=0, column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)
    
    flash_location = flashcard_number
    
flash1_front = Button(root, text="Pasta", padx=50,pady=50, command=flashcard_flip_to_back)
flash1_front.grid(row=0,column=0, columnspan=3)
flash1_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/pasta.jpg"))


flash2_front = Button(root, text="Burger", padx=50,pady=50, command=flashcard_flip_to_back)
flash2_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/burger.png"))

flash3_front = Button(root, text="Ribs", padx=50,pady=50, command=flashcard_flip_to_back)
flash3_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/ribs.jpg"))

flash_list = [flash1_front, flash2_front, flash3_front]
glue = {
  flash1_front: flash1_back,
  flash2_front: flash2_back,
  flash3_front: flash3_back
}

back_button = Button(root, text="<<",command=back)
exit_button = Button(root, text="Exit Program",command=root.quit)
next_button = Button(root, text=">>", command=lambda: forward(2))

back_button.grid(row=1,column=0)
#exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2)

root.mainloop()