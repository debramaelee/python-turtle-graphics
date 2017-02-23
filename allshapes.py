from shapes import *

x = int(raw_input('What size? '))
y = raw_input('Do you want to fill the shape? (yes/no) ')
if y == "yes":
    y = True
    c = raw_input('What color? ')
if y == "no":
    y = False
    c = 'black'

speed(0)

triangle(y, c, x)
up()
home()
forward(100)
down()

square(x, c, y)
up()
home()
right(45)
forward(200)
down()

pentagon(x, c, y)
up()
home()
right(90)
forward(200)
down()

hexagon(x, c, y)
up()
home()
right(135)
forward(200)
down()

octagon(x, c, y)
up()
home()
right(200)
forward(200)
down()

star(x, c, y)
up()
home()
left(90)
forward(200)
down()


circle(c, y)

mainloop()
