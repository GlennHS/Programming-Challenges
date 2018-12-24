from graphics import *
import time
import math
from random import *

win = GraphWin("Scorched Earth", 1000, 800)
floor = [Point(0, 800)]
background = Rectangle(Point(0, 0), Point(1000, 800))
background.setFill('black')
background.draw(win)

def generateLandscape():
    x = 0
    while(x < 1000):
        x += random() * 500
        y = 800 - random() * 300
        if(x > 1000):
            x = 1000
        floor.append(Point(x, y))
    # for i in range(len(floor) - 1):
    #     l = Line(Point(floor[i][0], floor[i][1]), Point(floor[i + 1][0], floor[i + 1][1]))
    #     l.draw(win)
    floor.append(Point(1000, 0))
    floor.append(Point(1000, 800))
    poly = Polygon(floor)
    poly.setFill('white')
    poly.draw(win)
    
generateLandscape()