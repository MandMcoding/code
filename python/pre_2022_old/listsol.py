# Flashcard Program
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Flash Cards")
        
# flips the cards to the front side
def flashcard_flip_to_front():
    flash_back.grid_forget()
    flash1_front.grid(row=0,column=0, columnspan=3)

# function that flips your card to the back
def flashcard_flip_to_back():
    # 1 deletes front
    flash1_front.grid_forget()
    global flash_back
    # 2 adds the back
    flash_back = Button(root, image=glue[flash1_front], command=flashcard_flip_to_front)
    flash_back.grid(row=0,column=0, columnspan=3)

# changes the cards
def forward(flashcard_number):
    global flash1_front
    global back_button
    global next_button
    
    # removes the front card
    flash1_front.grid_forget()
    # changes the front card to the next card
    flash1_front= flash_list[flashcard_number-1]
    # creates the next and back button and updates the flashcard number when clicked
    next_button = Button(root,text=">>", command=lambda: forward(flashcard_number+1))
    back_button = Button(root,text="<<",command=lambda: back(flashcard_number-1))
    
    # stops it from crashing because no value is for 3
    if flashcard_number == 3:
        next_button = Button(root, text=">>", state=DISABLED)
    
    flash1_front.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

# littrally exactly the same as the other function
def back(flashcard_number):
    global flash1_front
    global back_button
    global next_button
    
    flash1_front.grid_forget()
    flash1_front= flash_list[flashcard_number-1]
    next_button = Button(root,text=">>", command=lambda: forward(flashcard_number+1))
    back_button = Button(root,text="<<",command=lambda: back(flashcard_number-1))
    
    if flashcard_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)
        
    flash1_front.grid(row=0, column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

# 1 Creates the first flashcard, buttons which when clicked flip the card
# If you click then it triggers the flip_to_back function
flash1_front = Button(root, text="Pasta", padx=50,pady=50, command=flashcard_flip_to_back)
flash1_front.grid(row=0,column=0, columnspan=3)
flash1_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/pasta.jpg"))

# creates the other flashcards, but dosen't add them
flash2_front = Button(root, text="Burger", padx=50,pady=50, command=flashcard_flip_to_back)
flash2_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/burger.png"))

flash3_front = Button(root, text="Ribs", padx=50,pady=50, command=flashcard_flip_to_back)
flash3_back = ImageTk.PhotoImage(Image.open("/Users/marwan/Documents/Python/ribs.jpg"))

# the list of cards
flash_list = [flash1_front, flash2_front, flash3_front]

# gluing the front of the card to the back (used in flipping)
glue = {
  flash1_front: flash1_back,
  flash2_front: flash2_back,
  flash3_front: flash3_back
}

# 2 the buttons that change the flashcards
back_button = Button(root, text="<<",command=back)
exit_button = Button(root, text="Exit Program",command=root.quit)
next_button = Button(root, text=">>", command=lambda: forward(2))

back_button.grid(row=1,column=0)
#exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2)

root.mainloop()