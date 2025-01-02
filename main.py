import pgzrun, random

TITLE="Water Gun"
WIDTH=680
HEIGHT=460

speed=5

bullets=[]
enemies=[]

score=0

enemy=Actor("bubbles.png")
bullet=Actor("water.png")
defender=Actor("watergun.png")

enemies.append(enemy)

def draw():
    screen.clear()
    screen.fill(skyblue)
    defender.draw()
    for i in enemies():
        i.draw()
    screen.draw.text(str(score), (50,50), color="navy") 


def update():
    global score
    if keyboard.left:
        defender.y+=speed
    elif keyboard.right:
        defender.y-=speed

