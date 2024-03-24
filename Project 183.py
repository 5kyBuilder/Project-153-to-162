import requests
import json
from tkinter import *

api_url = "https://restcountries.com/v2/capital/"

root = Tk()
root.overrideredirect(True)
root.geometry("500x500")

title = Label(root, font=("times", 40, "bold"), text="Capital City Name")
title.place(relx=0.5, rely=0.1, anchor=CENTER)

capital_entry = Entry(root)
capital_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

country_label = Label(root, text="Country: ")
country_label.place(relx=0.2, rely=0.5, anchor=CENTER)

region_label = Label(root, text="Region: ")
region_label.place(relx=0.2, rely=0.6, anchor=CENTER)

language_label = Label(root, text="Language: ")
language_label.place(relx=0.2, rely=0.7, anchor=CENTER)

population_label = Label(root, text="Population: ")
population_label.place(relx=0.2, rely=0.8, anchor=CENTER)

area_label = Label(root, text="Area: ")
area_label.place(relx=0.2, rely=0.9, anchor=CENTER)

def findDetails():
    response = requests.get(api_url + capital_entry.get())
    
    api_output = json.loads(response.content)[0]
        
    country_label["text"] = "Country: " + api_output["name"]
    region_label["text"] = "Region: " + api_output["region"]
    language_label["text"] = "Language: " + api_output["languages"][0]["name"]
    population_label["text"] = "Population: " + str(api_output["population"])
    area_label["text"] = "Area: " + str(api_output["area"])


findDetailsButton = Button(root, command=findDetails, text="Find City Details")
findDetailsButton.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()