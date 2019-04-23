import pgzrun
import pgzero.screen
from pgzero.builtins import *

global screen 
myscr = screen 

print (pgzrun.__package__)

WIDTH = 1024
HEIGHT = 768

def draw():
    myscr.clear()
    myscr.draw.circle ( (400, 300), 35, 'blue')

    print (type(screen))

#


pgzrun.go()