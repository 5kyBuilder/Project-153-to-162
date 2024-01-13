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

canvas = Canvas(root, width=790, height=450, background="grey40", highlightbackground="black")
canvas.pack()

direction = ""
startX, startY, endX, endY = 0, 0, 0, 0

def draw(direction, oldX, oldY, newX, newY):
    colorInput = color_input.get()

# root.bind("<UP>", up_dir)
# root.bind("<DOWN>", down_dir)
# root.bind("<LEFT>", left_dir)
# root.bind("<RIGHT>", right_dir)

root.mainloop()