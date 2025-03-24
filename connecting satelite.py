import pgzrun
import random

WIDTH=600
HEIGHT=600
TITLE="connect the satelite"

s=Actor("stli")
s.x=300
s.y=300

def draw():
    screen.blit("spb",(0,0))
    s.draw()
def update():
    pass






pgzrun.go()