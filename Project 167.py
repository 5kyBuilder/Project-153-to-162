from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Inserting Shapes in a Canvas")
root.minsize(800, 600)
root.maxsize(800, 600)

color_label = Label(root, text="Color: ")
color_label.place(relx=0.6, rely=0.9, anchor=CENTER)

startX_label = Label(root, text="Start X: ")
startX_label.place(relx=0.05, rely=0.8, anchor=CENTER)

starY_label = Label(root, text="Start Y: ")
starY_label.place(relx=0.3, rely=0.8, anchor=CENTER)

endX_label = Label(root, text="End X: ")
endX_label.place(relx=0.55, rely=0.8, anchor=CENTER)

endY_label = Label(root, text="End Y: ")
endY_label.place(relx=0.79, rely=0.8, anchor=CENTER)

startX_input = Entry(root)
startX_input.place(relx=0.17, rely=0.8, anchor=CENTER)

startY_input = Entry(root)
startY_input.place(relx=0.41, rely=0.8, anchor=CENTER)

endX_input = Entry(root)
endX_input.place(relx=0.66, rely=0.8, anchor=CENTER)

endY_input = Entry(root)
endY_input.place(relx=0.9, rely=0.8, anchor=CENTER)

color_input = Entry(root)
color_input.insert(0, "black")
color_input.place(relx=0.8, rely=0.9, anchor=CENTER)

go_Out_Input = Entry(root)
go_Out_Input.place(relx=0.1, rely=0.9, anchor=CENTER)

canvas = Canvas(root, width=790, height=450, background="grey40", highlightbackground="black")
canvas.pack()

def Circle(event):
    oldX, newX, oldY, newY = startX_input.get(), endX_input.get(), startY_input.get(), endY_input.get()
    draw("c", oldX, oldY, newX, newY)

def Rectangle(event):
    oldX, newX, oldY, newY = startX_input.get(), endX_input.get(), startY_input.get(), endY_input.get()
    draw("r", oldX, oldY, newX, newY)

def Line(event):
    oldX, newX, oldY, newY = startX_input.get(), endX_input.get(), startY_input.get(), endY_input.get()
    draw("l", oldX, oldY, newX, newY)

def draw(shape, oldX, oldY, newX, newY):
    colorInput = color_input.get()
    if(shape=="c"):
        canvas.create_oval(oldX, oldY, newX, newY, width=3, fill=colorInput)
    elif(shape=="r"):
        canvas.create_rectangle(oldX, oldY, newX, newY, width=3, fill=colorInput)
    elif(shape=="l"):
        canvas.create_line(oldX, oldY, newX, newY, width=5, fill=colorInput)
        
def clearEverything(event):
    canvas.delete('all')

root.bind("<c>", Circle)
root.bind("<r>", Rectangle)
root.bind("<l>", Line)

root.bind("<f>", clearEverything)

root.mainloop()