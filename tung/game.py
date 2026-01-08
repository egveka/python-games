import inter

def adventure():
    if inter.bva.get() == False and inter.bvb.get() == True:
        inter.window.destroy()
    if inter.bva.get() == True and inter.bvb.get() == False:
        inter.bva.set(False)
        inter.bvb.set(False)
        inter.action.config(font=("Arial", 20), text="You were working in a high-tech techno lab, when you accidentaly opened a wrong door.\n You wanted to exit the room, but you realized that you are standing in front of a giant time machine.\n What will you do?")
        inter.a.config(text="Exit the room")
        inter.b.config(text="Explore the machine")
        inter.go.config(command=scenario1)
        return
    
def destruction():
    inter.window.destroy()
    
def scenario1():
    if inter.bva.get() == True and inter.bvb.get() == False:
        inter.action.config(text="You exit the room and move on with your work.\n But you are very curious of where could it take you, so you go to sleep with it.\n At morning, you don't remember anything.\n YOU SUCCESSFULLY BEAT THE GAME WITH A BORING LEVEL OF 10/10!\n YOU ARE BORING!")
        inter.b.config(text="")
        inter.a.config(text="")
        inter.go.config(text="The End")
        inter.bva.set(False)
        inter.bvb.set(False)
        inter.go.config(command=destruction)
    elif inter.bvb.get() == True and inter.bva.get() == False:
        inter.bva.set(False)
        inter.bvb.set(False)
        inter.action.config(text="You accidentaly press one of the buttons on the table, but you dont notice it and go in to inspect it.\n Suddenly you feel like your body is being twisted around and you find yourself on the ground.\n What will you do?")
        inter.a.config(text="Go out of the cabinet")
        inter.b.config(text="Drink the coke on the table.")
        inter.go.config(command=scenario2)
        return

def scenario2():
    if inter.bvb.get() == True and inter.bva.get() == False:
        inter.bva.set(False)
        inter.bvb.set(False)
        inter.action.config(text="It appears that the liquid on the table wasn't coke.\n It was machine oil. You spit out the oil.\n You notice a cat sleeping on a mat in the corner.\n What will you do?")
        inter.a.config(text="Pet the cat")
        inter.b.config(text="Go out of the room")
        inter.go.config(command=scenario3a)
    elif inter.bva.get() == True and inter.bvb.get() == False:
        inter.bva.set(False)
        inter.bvb.set(False)
        inter.action.config(text="You go out of the room and see everything shining with cleanness.\n You see robots flying all around you and you figure that you must be in the future.\n What will you do?")
        inter.a.config(text="Ask a robot about the year")
        inter.b.config(text="Try to go back into the room with a time machine")
        inter.go.config(command=scenario3b)

def scenario3a():
    if inter.bvb:
        pass