from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Credit Card Authenticator")
root.geometry("700x700")

img = ImageTk.PhotoImage(Image.open("credit_card.png"))

Card_Entry = Entry(root)
Card_Entry.place(relx=0.5, rely=0.3, anchor=CENTER)

Credit_Card_Image = Label(image=img)
Credit_Card_Image.place(relx=0.5, rely=0.6, anchor=CENTER)

def check_card():
    pin = Card_Entry.get()
    try:
        pin = int(pin)
        messagebox.showinfo("Successful Transaction", "Your pincode is verified!")
    except(ValueError):
        messagebox.showinfo("Error", "Invalid Pin Code. It contains no numbers")
    
button_1 = Button(root, command=check_card, text="Check Pin Code")
button_1.place(relx=0.5, rely=0.35, anchor=CENTER)

root.mainloop()