from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Country Flag")
root.geometry("700x700")

indian_flag = ImageTk.PhotoImage(Image.open("india.png"))
qatar_flag = ImageTk.PhotoImage(Image.open("qatar.png"))
pakistan_flag = ImageTk.PhotoImage(Image.open("pakistan.png"))
china_flag = ImageTk.PhotoImage(Image.open("china.png"))
russian_flag = ImageTk.PhotoImage(Image.open("russia.png"))

image_dictionary = {
    "India": indian_flag,
    "Qatar": qatar_flag,
    "Pakistan": pakistan_flag,
    "China": china_flag,
    "Russia": russian_flag
}

country_textbox = Entry(root)
country_textbox.pack()

Image = Label(root)

def getImageFromInput():
    country = country_textbox.get()
    
    try:
        country_flag = image_dictionary[country]
        Image.configure(image=country_flag)
        Image.image = country_flag
    except KeyError:
        messagebox.showinfo("Country Not Found", "The country you inputted is not found in our database")
    
button_1 = Button(root, text="Show Flag", command=getImageFromInput)

button_1.pack()
Image.pack()

root.mainloop()