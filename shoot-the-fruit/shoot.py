import pgzrun
from random import randint

apple = Actor("apple")
score = 0

def draw():
    screen.clear()
    apple.draw()

def reset_timer():
    print("Time's up!")
    quit()

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 600)

clock.schedule_unique(reset_timer, 5)

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Nice shot!")
        score += 1
        place_apple()
        clock.schedule_unique(reset_timer, 5)
    else:
        print("You missed!")
        print("Your Score: ", score)
        clock.unschedule(reset_timer)
        quit()

place_apple()

pgzrun.go()