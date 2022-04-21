#미완성

import turtle
import random

x1, y1 = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))

ListXY = []

for _ in range(10):
    randX=random.randint(0,500)
    randY=random.randint(0,500)
    ListXY.append((randX,randY))

print(ListXY)

# Draw the circle
turtle.penup()         # Pull the pen up
turtle.goto(x1, y1)
turtle.pendown()       # Pull the pen down
turtle.circle(radius)



turtle.hideturtle()
turtle.done()
