from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("500x500")

guessing_entry = Entry(root)

guessing_label = Label(root)
label_todisplay = Label(root)

threed_array_of_passwords = [[['1', '2', '3', '4', '5', '6'], ["Queens", "Kings"], ["a", "b", "!", "d", "#", "f", "g", "%"]]]

def generate():
    guessing_label["text"] = "Guessed Password is " + guessing_entry.get()
    random_1 = random.randint(0, 5)
    random_2 = random.randint(0, 1)
    random_3 = random.randint(0, 7)
        
    textt = str(threed_array_of_passwords[0][0][random_1]) + "" + threed_array_of_passwords[0][1][random_2] + "" + threed_array_of_passwords[0][2][random_3]
    
    label_todisplay["text"] = "Generated Password is " + textt

button_1 = Button(root, command=generate, text="Generate new Password")
guessing_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
guessing_label.place(relx=0.5, rely=0.4, anchor=CENTER)
button_1.place(relx=0.5, rely=0.5, anchor=CENTER)
label_todisplay.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()