import pgzrun
import random

WIDTH=600
HEIGHT=600
TITLE="connect the satelite"
list=[]
index=0
finished=False
lines=[]

for i in range(20):
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
    for i in lines:
        screen.draw.line(i[0],i[1],"white")


def on_mouse_down(pos):
    global index,lines
    if list[index].collidepoint(pos):
        if index>0:
            pos1=list[index-1].pos
            pos2=list[index].pos
            lines.append((pos1,pos2))
        index=index+1

def update():
    pass






pgzrun.go()