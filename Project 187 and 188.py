from tkinter import *
from tkinter import messagebox, filedialog
import os

try:
    from firebase import firebase
    from simplecrypt import encrypt, decrypt
except ModuleNotFoundError:
    print("error")


firebase = firebase.FirebaseApplication("https://letschat-9b3f2-default-rtdb.firebaseio.com", None)

text, fileName = "", ""

login_window = Tk()
login_window.geometry("600x600")
login_window.config(bg='#AB92BF')

def Encrypt():
    ciphercode = encrypt("AIM", text.get("1.0", END))
    hex_string = ciphercode.hex()
    
    file = open(fileName.get()+".txt", "w")
    file.write(hex_string)
    
    fileName.delete(0, END)
    text.delete(1.0, END)
    
    messagebox.showinfo("SUCCESS", "File has been created!")
    
def enterRoom():   
    global text, fileName
    
    message_window = Tk()
    message_window.config(bg='#AFC1D6')
    message_window.geometry("600x500")
    
    text = Text(message_window, height=20, width=72)
    text.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    file_labl = Label(message_window, text="File Name: " , font = ('arial 13', 18), bg='#AFC1D6', fg="white")
    file_labl.place(relx=0.3,rely=0.8, anchor=CENTER)
    
    fileName = Entry(message_window, font = 'arial 15')
    fileName.place(relx=0.6,rely=0.8, anchor=CENTER)
    
    btn_send = Button(message_window, text="Create", font = 'arial 13', bg="#D6CA98", fg="black", padx=10, relief=FLAT, command=Encrypt)
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER)
    
    message_window.mainloop()
    

def chooseFile():
    message_window = Tk()
    message_window.config(bg='#AFC1D6')
    message_window.geometry("600x500")
    
    text = Text(message_window, height=20, width=72)
    text.place(relx=0.5,rely=0.35, anchor=CENTER)    
    
    text_File = filedialog.askopenfilename(title="Open Text File", filetypes=[("Text Files", "*.txt")])
    name = os.path.basename(text_File)
    
    file = open(name, "r")
    paragraph = file.read()

    byte_str = bytes.fromhex(paragraph)
    original = decrypt("AIM", byte_str)
    final_message = original.decode("utf-8")  
    
    text.insert(END, final_message)
    
    file.close()

eandd_label = Label(login_window, text="ENCRYPTION AND DECRYPTION : " , font = ('arial 13', 25), bg ='#AB92BF', fg="white")
eandd_label.place(relx=0.5,rely=0.3, anchor=CENTER)

btn_encrypt = Button(login_window, text="Encrypt" , font = ('arial 13', 20), bg="#CEF9F2", fg="black", command=enterRoom, relief=FLAT, padx=10)
btn_encrypt.place(relx=0.25,rely=0.5, anchor=CENTER)

btn_decrypt = Button(login_window, text="Decrypt" , font = ('arial 13', 20), bg="#CEF9F2", fg="black", command=chooseFile, relief=FLAT, padx=10)
btn_decrypt.place(relx=0.75,rely=0.5, anchor=CENTER)


login_window.mainloop()
