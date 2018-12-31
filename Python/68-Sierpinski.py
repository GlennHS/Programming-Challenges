from graphics import *
from time import sleep

win = GraphWin("Sierpinski", 500, 500)
depth = 10 # Actually depth +1 but oh well, non-breaking and all that
height = 800 # Twice height actually
width = 460

def createTriangle(apexX, apexY, iteration):
        # Coords assigned clockwise from apex
        # eg. a
        #    / \
        #   /   \
        #  c-----b
        ax = apexX
        ay = apexY
        bx = apexX - (width / pow(2, iteration))
        by = apexY + (height / pow(2, iteration))
        cx = apexX + (width / pow(2, iteration))
        cy = apexY + (height / pow(2, iteration))
        T = Polygon(Point(ax, ay), Point(bx, by), Point(cx, cy))
        T.draw(win)
        if(not(iteration == depth)):
                iteration += 1
                createTriangle(ax, ay, iteration)
                createTriangle(bx + width / pow(2, iteration), by - height / pow(2, iteration), iteration)
                createTriangle(cx - width / pow(2, iteration), cy - height / pow(2, iteration), iteration)

createTriangle(width / 2, 0, 1)
sleep(5)