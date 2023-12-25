from tkinter import *

root = Tk()
root.title("Class 147")

root.geometry("500x500")
root.configure(background="snow")

Text_box_1 = Entry(root)
Text_box_1.place(relx=.5, rely=.4, anchor=CENTER)

label_ascii = Label(root, text="ASCII Value: ", fg="red")
label_ascii.place(relx=.5, rely=.6, anchor=CENTER)

label_ascii_2 = Label(root, text="Encrypted Word: ", fg="green")
label_ascii_2.place(relx=.5, rely=.7, anchor=CENTER)

def ascii_Converter():
    input_words = Text_box_1.get()
    
    for letter in input_words:
        label_ascii["text"] += str(ord(letter)) + " "
        label_ascii_2["text"] += chr(ord(letter) - 1)
    
Ascii_btn = Button(root, text="Show ASCII Value", command=ascii_Converter, bg="blue", fg="white")
Ascii_btn.place(relx=.5, rely=.5, anchor=CENTER)

root.mainloop()