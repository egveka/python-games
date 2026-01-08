import pgzrun

WIDTH = 600
HEIGHT = 500
time = int(input("Enter the number of seconds\n"))
time_left = 0

cps = 0
button = Actor("orange")
button.x = WIDTH // 2
button.y = HEIGHT // 2

def timer():
    global time_left
    time_left = time
    if time_left > 0:
        time_left -= 1
    else:
        ranking_system()

def ranking_system():
    if time_left == 0:
        print(cps/time)

clock.schedule_interval(timer, 1)

def draw():
    screen.clear()
    button.draw()

def on_mouse_down(pos):
    global cps
    if button.collidepoint(pos):
        cps += 1
    else:
        pass

pgzrun.go()