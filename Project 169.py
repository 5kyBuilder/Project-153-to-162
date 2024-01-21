from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Classes")
root.geometry("700x700")

elementsList = ["Label", "Button", "Dropdown"]

string_var = StringVar(root, value="Label")
dropdown_One = ttk.Combobox(root, textvariable=string_var, values=elementsList)

text_textbox = Entry(root)
dropdownBox = Entry(root)

text_textbox.pack()
dropdownBox.pack()
dropdown_One.pack()

def generate():
    new_element = Elements(string_var.get(), text_textbox.get(), dropdownBox.get())

ButtonToGenerateElements = Button(root, command=generate, text="Click me to generate an element of your choosing!")
ButtonToGenerateElements.pack()

def MessageShow():
    messagebox.showinfo("Button clicked", "You have clicked a button!")

class Elements:
    def __init__(self, typeOfElement, Text, dropDownText):
        if typeOfElement == "Label":
            Label_One = Label(root, text=Text)
            Label_One.pack()
        elif typeOfElement == "Button":
            Button_One = Button(root, text=Text, command=MessageShow)
            Button_One.pack()
        elif typeOfElement == "Dropdown":
            list_of_stuff = dropDownText.split(",")
            examplevar = StringVar(root, value=list_of_stuff[0])
            dropdown_One = ttk.Combobox(root, textvariable=examplevar, values=list_of_stuff)
            dropdown_One.pack()

        
root.mainloop()