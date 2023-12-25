from tkinter import *
import random

root = Tk()
root.title("Random Countries and Capitals")
root.geometry("500x500")
 
countries = []
capitals = []
 
country_box = Entry(root)
country_box.place(relx=0.5, rely=0.1, anchor=CENTER)

capital_box = Entry(root)
capital_box.place(relx=0.5, rely=0.2, anchor=CENTER)

countries_label = Label(root)
capitals_label = Label(root)

random_counteries_label = Label(root)
random_capitals_label = Label(root)

countries_label.place(relx=0.5, rely=0.4, anchor=CENTER)
capitals_label.place(relx=0.5, rely=0.5, anchor=CENTER)

random_counteries_label.place(relx=0.5, rely=0.7, anchor=CENTER)
random_capitals_label.place(relx=0.5, rely=0.8, anchor=CENTER)

def list_display():
    value1 = country_box.get()
    value2 = capital_box.get()
    
    if value1 and value2:
        countries.append(value1)
        countries_label["text"] = "Countrys: " + str(countries)
        
        capitals.append(value2)
        capitals_label["text"] = "Capitals: " + str(capitals)
def random_pick():
    length_countries = len(countries)
    length_capitals = len(capitals)
    
    random_num_1 = random.randint(0, length_countries - 1)
    random_num_2 = random.randint(0, length_capitals - 1)
    
    random_integer_1 = countries[random_num_1]
    random_integer_2 = capitals[random_num_2]

    random_counteries_label["text"] = "Random Country: " + str(random_integer_1)
    random_capitals_label["text"] = "Random Capital: " + str(random_integer_2)

button_1 = Button(root, command=list_display, text="Display countries and capitals")    
button_2 = Button(root, command=random_pick, text="Display countries and capitals randomly")

button_1.place(relx=0.5, rely=0.3, anchor=CENTER)
button_2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()