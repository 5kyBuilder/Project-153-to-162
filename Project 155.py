from tkinter import *
import random

root = Tk()
root.geometry("700x700")
root.title("Dictionaries")

dictionary = {
    'Colours': ("IndianRed3", "cyan", "green yellow", "dark orange", "gray50", "DarkOrchid2")
}

def change_bgcolour():
    random_numint = random.randint(0, len(dictionary['Colours']) - 1)
    colour = dictionary['Colours'][random_numint]
    
    root.configure(background=colour)

button_1 = Button(root, command=change_bgcolour, text="Click me")

button_1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()