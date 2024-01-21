from tkinter import * 
import random

root = Tk()  
root.geometry("900x600") 
root.title("Classes")

int_Var = IntVar(root, value=0)

number = 1

class CreateElements:
    
    def __init__(self, Values): 
      global number
      newButton = Radiobutton(root, text="Value " + str(number), variable=int_Var, value=Values)
      newButton.pack()
      
      number+=1
      
def generate():
    randumNum = random.randint(1, 1000)
    obj_of_CreateElements = CreateElements(randumNum)
    
def valuePrint():
    messagebox.showinfo("Value", "the value is " + str(int_Var.get()))

btn = Button(root, text ="Create radio button", font=("Courier", 18), command=generate) 
btn.pack(padx=20, pady = 10) 

btn = Button(root, text ="Check value", font=("Courier", 18), command=valuePrint) 
btn.pack() 

root.mainloop()