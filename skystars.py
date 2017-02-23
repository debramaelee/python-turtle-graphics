from turtle import *
import math
import random

speed(0)
random_directions = []
random_distance = []
x = 5

def star():
    pencolor('yellow')
    bgcolor('black')
    fillcolor('yellow')
    for i in range(5):
        begin_fill()
        left(72)
        forward(x)
        right(144)
        forward(x)
    end_fill()
# inside pentagon fill
    fillcolor('yellow')
    begin_fill()
    for i in range(5):
        #forward(2 * math.sin(math.radians(18)) * x)
        forward(2 * sin(radians(18)) * x)
        right(72)
    end_fill()

#set number of stars and randomize star locations
for i in range(50):
    up()
    home()
    x_angle = random.randint(0, 360)
    x_distance = random.randint(0, 500)
    if not x_angle in random_directions\
     and not x_distance in random_distance:
        right(x_angle)
        forward(x_distance)
        random_directions.append(x_angle)
        random_distance.append(x_distance)
        down()
        star()

mainloop()
