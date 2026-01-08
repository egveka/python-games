from tkinter import *

window = Tk()
window.geometry("890x700")
window.title("Choose your own adventure")
window.resizable(False, False)

interface = LabelFrame(text="Game")

go = Button(interface, text="I Chose", width=15, height=2, relief=RIDGE)
action = Label(interface, font=("Arial", 24), text="Welcome to Choose Your Own Adventure!\n This game is about choices and decisions.\n You will get a situation and you need to choose your action.\n And every decision you make, could be crucial.\n Do you want to play my game?")

bva = BooleanVar()
bvb = BooleanVar()

a = Checkbutton(interface, font=("Arial", 20), text="Of course!", variable=bva, onvalue=True, offvalue=False)
b = Checkbutton(interface, font=("Arial", 20), text="Nah, maybe another time", variable=bvb, onvalue=True, offvalue=False)

interface.pack()
action.pack(anchor=CENTER, pady=10)
a.pack(pady=5)
b.pack(pady=5)
go.pack(anchor=CENTER)