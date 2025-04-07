import pgzrun
import random

WIDTH=600
HEIGHT=600
TITLE="connect the satelite"
list=[]

for i in range(8):
    s=Actor("stli")
    s.x=random.randint(0,600)
    s.y=random.randint(0,600)
    list.append(s)

def draw():
    screen.blit("spb",(0,0))
    number=1
    for s in list:
        s.draw()
        screen.draw.text(str(number),(s.x,s.y+30),color="red")
        number=number+1
def update():
    pass






pgzrun.go()