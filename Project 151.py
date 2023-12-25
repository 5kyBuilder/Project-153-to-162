from tkinter import *

root = Tk()
root.title("Half Yearly Profit Calculation")
root.geometry("700x700")
root.config(bg="snow")

months = ("January", "February", "March", "April", "May", "June")
profits = (2000, 32103, 490243, 329209, 1230914, 3000404)

maximum_profit = max(profits)
minimum_profit = min(profits)

maximum_profit_index = profits.index(maximum_profit)
minimum_profit_index = profits.index(minimum_profit)

maximum_profit_month = months[maximum_profit_index]
minimum_profit_month = months[minimum_profit_index]

title = Label(root, text="Half yearly Calculation", font=('Helvetica bold',40))

months_label = Label(root, text=months)
profits_label = Label(root, text=profits)

minimum_label = Label(root)
maximum_label = Label(root)

def display_min():
    minimum_label["text"] = "Minimum profit of $" + str(minimum_profit) + " was earned in the month of " + minimum_profit_month

def display_max():
    maximum_label["text"] = "Maximum profit of $" + str(maximum_profit) + " was earned in the month of " + maximum_profit_month
    
button_min = Button(root, command=display_min, text="Show Minimum profitable month", bg="red")    
button_max = Button(root, command=display_max, text="Show Maximum profitable month", bg="green")    

title.place(relx=0.5, rely=0.1, anchor=CENTER)
months_label.place(relx=0.5, rely=0.2, anchor=CENTER)
profits_label.place(relx=0.5, rely=0.3, anchor=CENTER)
button_min.place(relx=0.5, rely=0.4, anchor=CENTER)
minimum_label.place(relx=0.5, rely=0.5, anchor=CENTER)
button_max.place(relx=0.5, rely=0.6, anchor=CENTER)
maximum_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()