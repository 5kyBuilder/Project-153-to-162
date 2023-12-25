from tkinter import *
import random

picnic_items = ["Bottle", "Soda", "Chips", "Chocolate", "Fruits", "Pie", "Pizza", "Burger"]

root = Tk()
root.title("Class 148")
root.geometry("500x500")

show_label = Label(root, text=picnic_items)
Item_picked = Label(root)

def randomNum():
    random_list = random.sample(range(0, len(picnic_items)), 1)
    Item_picked["text"] = "Item in " + str(random_list) + " is in the bag"
    
button_1 = Button(root, command=randomNum, text="Get Random Item")
button_1.place(relx=.5, rely=.5, anchor=CENTER)   

show_label.place(relx=.5, rely=.3, anchor=CENTER)    
Item_picked.place(relx=.5, rely=.6, anchor=CENTER)    

root.mainloop() 