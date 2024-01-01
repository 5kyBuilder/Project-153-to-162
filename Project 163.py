from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Fever Report")

q1_radiobtn = StringVar(value="0")
q2_radiobtn = StringVar(value="0")
q3_radiobtn = StringVar(value="0")
q4_radiobtn = StringVar(value="0")
q5_radiobtn = StringVar(value="0")

q1_label = Label(root, text="Do you experience shortness of breath during routine activities?")
q1_r1 = Radiobutton(root, text="yes", value="yes", variable=q1_radiobtn)
q1_r2 = Radiobutton(root, text="no", value="no", variable=q1_radiobtn)

q2_label = Label(root, text="Do you have a swelling in the feet/ankles/legs(shows feel tighter) or abdomen?")
q2_r1 = Radiobutton(root, text="yes", value="yes", variable=q2_radiobtn)
q2_r2 = Radiobutton(root, text="no", value="no", variable=q2_radiobtn)

q3_label = Label(root, text="Do you feel any of these symptoms - Confusion, disorientation or loss of memory?")
q3_r1 = Radiobutton(root, text="yes", value="yes", variable=q3_radiobtn)
q3_r2 = Radiobutton(root, text="no", value="no", variable=q3_radiobtn)

q4_label = Label(root, text="Do you experience shortness of breath while sleeping/resting?")
q4_r1 = Radiobutton(root, text="yes", value="yes", variable=q4_radiobtn)
q4_r2 = Radiobutton(root, text="no", value="no", variable=q4_radiobtn)

q5_label = Label(root, text="Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus?")
q5_r1 = Radiobutton(root, text="yes", value="yes", variable=q5_radiobtn)
q5_r2 = Radiobutton(root, text="no", value="no", variable=q5_radiobtn)

def report():
    score = 0
    if q1_radiobtn.get() == "yes":
        score += 1
    if q2_radiobtn.get() == "yes":
        score += 1
    if q3_radiobtn.get() == "yes":
        score += 1
    if q4_radiobtn.get() == "yes":
        score += 1
    if q5_radiobtn.get() == "yes":
        score += 1
    
    if score == 5:
        messagebox.showinfo("Result", "You should visit the doctor immediately.")
    elif score >= 1 and score <= 4:
        messagebox.showinfo("Result", "You should, perhaps visit the doctor.")
    elif score < 1:
        messagebox.showinfo("Result", "You are fine.")

button_1 = Button(root, text="Show Result", command=report)

q1_label.pack()
q1_r1.pack()
q1_r2.pack()

q2_label.pack()
q2_r1.pack()
q2_r2.pack()

q3_label.pack()
q3_r1.pack()
q3_r2.pack()

q4_label.pack()
q4_r1.pack()
q4_r2.pack()

q5_label.pack()
q5_r1.pack()
q5_r2.pack()

button_1.pack()

root.mainloop()