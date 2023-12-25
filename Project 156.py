from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.geometry("600x600")
root.title("Endless Pokemon Card Game")
root.configure(background="yellow3")

player_one_label = Label(root, text="Player 1:")
player_one_score = Label(root, text="0")

player_two_label = Label(root, text="Player 2:")
player_two_score = Label(root, text="0")

announcement_label = Label(root)

Scores = {
    'Player_1': 0,
    'Player_2': 0    
}

Image_Scores = {
    "1": 80,
    "2": 30,
    "3": 80,
    "4": 40,
    "5": 80,
    "6": 90,
    "7": 130,
    "8": 110,
    "9": 280,
    "10": 180
}

def change_image(image):
    announcement_label.configure(image=image)
    announcement_label.image = image

def getRandomNumForPlayerOne():
    random_int = random.randint(1, 10)
    Scores['Player_1'] += Image_Scores[str(random_int)]
    player_one_score["text"] = str(Scores['Player_1'])
    img = ImageTk.PhotoImage(Image.open("pokemon_card_"+ str(random_int) +".jpg"))
    change_image(img)
    
def getRandomNumForPlayerTwo():
    random_int = random.randint(1, 10)
    Scores['Player_2'] += Image_Scores[str(random_int)]
    player_two_score["text"] = str(Scores['Player_2'])
    img = ImageTk.PhotoImage(Image.open("pokemon_card_"+ str(random_int) +".jpg"))
    change_image(img)
    
button_1 = Button(root, command=getRandomNumForPlayerOne, text="Roll")
button_2 = Button(root, command=getRandomNumForPlayerTwo, text="Roll")

player_one_label.place(relx=0.05, rely=0.3, anchor=CENTER)
player_one_score.place(relx=0.05, rely=0.4, anchor=CENTER)

player_two_label.place(relx=0.95, rely=0.3, anchor=CENTER)
player_two_score.place(relx=0.95, rely=0.4, anchor=CENTER)

announcement_label.place(relx=0.5, rely=0.5, anchor=CENTER)

button_1.place(relx=0.05, rely=0.5, anchor=CENTER)
button_2.place(relx=0.95, rely=0.5, anchor=CENTER)

root.mainloop()