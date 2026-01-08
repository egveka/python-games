import pgzrun
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Nice shot!")
        place_apple()
    else:
        print("You missed")

place_apple()

pgzrun.go()