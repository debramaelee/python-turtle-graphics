from turtle import *
import math

def triangle(y, c, x):
    if y == True:
        pencolor(c)
        fillcolor(c)
        begin_fill()
        setheading(-60)
        forward(x)
        setheading(-180)
        forward(x)
        setheading(60)
        forward(x)
        end_fill()
    if y == False:
        setheading(-60)
        forward(x)
        setheading(-180)
        forward(x)
        setheading(60)
        forward(x)

def square(x, c, y):
    if y == True:
        fillcolor(c)
        begin_fill()
        for i in range(4):
            forward(x)
            right(90)
        end_fill()
    if y == False:
        for i in range(4):
            forward(x)
            right(90)

def pentagon(x, c, y):
    if y == True:
        fillcolor(c)
        begin_fill()
        right(36)
        forward(x)
        for i in range(4):
            right(72)
            forward(x)
        end_fill()
    if y == False:
            right(36)
            forward(x)
            for i in range(4):
                right(72)
                forward(x)

def hexagon(x, c, y):
    if y == True:
        fillcolor(c)
        begin_fill()
        for i in range(6):
            right(60)
            forward(x)
        end_fill()
    if y == False:
        for i in range(6):
            right(60)
            forward(x)

def octagon(x, c, y):
    if y == True:
        fillcolor(c)
        begin_fill()
        for i in range(8):
            right(45)
            forward(x)
        end_fill()
    if y == False:
        for i in range(8):
            right(45)
            forward(x)

def star(x, c, y):
    if y == True:
        fillcolor(c)
        for i in range(5):
            begin_fill()
            left(72)
            forward(x)
            right(144)
            forward(x)
        end_fill()
    # inside pentagon fill
        fillcolor(c)
        begin_fill()
        for i in range(5):
            forward(2 * math.sin(math.radians(18)) * x)
            right(72)
        end_fill()
    if y == False:
        for i in range(5):
            left(72)
            forward(x)
            right(144)
            forward(x)

def circle(c, y):
    if y == True:
        fillcolor(c)
        begin_fill()
        for i in range(360):
            forward(1)
            right(1)
        end_fill()
    if y == False:
        for i in range(360):
            forward(1)
            right(1)
