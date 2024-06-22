from tkinter import *

try:
    from firebase import firebase
    from simplecrypt import encrypt, decrypt
except ModuleNotFoundError:
    print("error")


firebase = firebase.FirebaseApplication("https://letschat-9b3f2-default-rtdb.firebaseio.com", None)

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

name, text, entry = "", "", ""
last_value = ""

def getData():
    global text, last_value, ycode, fcode
    getDataOfMessages = firebase.get("/", ycode)
    byte_str = bytes.fromhex(getDataOfMessages)
    original = decrypt("AIM", byte_str)
    final_message = original.decode("utf-8")
    text.insert(END, final_message+"\n")

    last_value = final_message

    get_friendData = firebase.get("/", fcode)
    if(get_friendData != None):
        byte_str = bytes.fromhex(getDataOfMessages)
        original = decrypt("AIM", byte_str)
        final_message = original.decode("utf-8")
        if (final_message not in last_value):
            text.insert(END, final_message+"\n")
            last_value = final_message

def sendData():
    global name, entry
    
    message = entry.get()
    ciphercode = encrypt("AIM", message)
    hex_string = ciphercode.hex()
    
    put_data = firebase.put("/", name.get(), hex_string)
    print(put_data)
    
username_label = Label(login_window, text="Username: " , font = 'arial 13', bg ='#AB92BF', fg="white")
username_label.place(relx=0.3,rely=0.3, anchor=CENTER)

name = Entry(login_window)
name.place(relx=0.6,rely=0.3, anchor=CENTER)

password_label = Label(login_window, text="Password:  " , font = 'arial 13', bg ='#AB92BF', fg="white")
password_label.place(relx=0.3,rely=0.4, anchor=CENTER)

entry = Entry(login_window)
entry.place(relx=0.6,rely=0.4, anchor=CENTER)

btn_start = Button(login_window, text="Start" , font = 'arial 13' , bg="#CEF9F2", fg="black", command=sendData, relief=FLAT, padx=10)
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

login_window.mainloop()
