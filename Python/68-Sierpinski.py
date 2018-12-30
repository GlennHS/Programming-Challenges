from graphics import *

win = GraphWin("Sierpinski", 500, 500)
depth = 4
height = 800
width = 460

def createTriangle(apexX, apexY, iteration):
    ax = apexX
    ay = apexY
    bx = apexX - (width / pow(2, iteration))
    by = apexY + (height / pow(2, iteration))
    cx = apexX + (width / pow(2, iteration))
    cy = apexY + (height / pow(2, iteration))
    T = Polygon(Point(ax, ay), Point(bx, by), Point(cx, cy))
    T.draw(win)
    if(not(iteration == depth)):
        createTriangle(ax, ay, iteration + 1)
        createTriangle(bx + width / pow(2, iteration + 1), by - height / pow(2, iteration + 1), iteration + 1)
        createTriangle(cx - width / pow(2, iteration + 1), cy - height / pow(2, iteration + 1), iteration + 1)

createTriangle(width / 2, 0, 1)