from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("600x700")
root.title("Image Editor")

root.configure(bg="grey70")

Image_Label = Label(root, image="")

file1 = ""

def openFile():
    global file1
    file1 = filedialog.askopenfilename(title="Open Text File", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    print(file1)
    Image_Imported = ImageTk.PhotoImage(Image.open(file1))
    Image_Label.configure(image=Image_Imported)
    Image_Label.image = Image_Imported
    
def rotateImage():
    ImageFound = Image.open(file1)
    rotatedImage = ImageFound.rotate(180)
    Image_Imported = ImageTk.PhotoImage(rotatedImage)
    
    Image_Label.configure(image=Image_Imported)
    Image_Label.image = Image_Imported
    
Open_Button = Button(root, command=openFile, text="Open Image")
Rotate_Button = Button(root, command=rotateImage, text="Rotate Image")

Open_Button.pack()
Image_Label.pack()
Rotate_Button.pack()

root.mainloop()