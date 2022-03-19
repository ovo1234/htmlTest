# 타입 설명 

# radius = 20

# area = radius * radius * 3.14159

# print("the area for the circle of radius", radius, "is", area)

# variable = input("Enter a string: ")


# turtle 공부

import turtle as tu

x1 , y1 = eval(input("x1 과 y1 포인트 : "))
x2 , y2 = eval(input("x2 과 y2 포인트 : "))

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

tu.penup()
tu.goto(x1, y1) #Move to (x1, y1)
tu.pendown()
tu.write("Point 1")

tu.goto(x2, y2)
tu.write("Point 2")

tu.penup()
tu.goto((x1 + x2 ) / 2 , (y1 + y2) / 2)
tu.write(distance)

tu.done()


# import turtle
# # Prompt the user for inputing two points
# x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
# x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
# # Compute the distance
# distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# # Display two points and the connecting line
# turtle.penup()
# turtle.goto(x1, y1) # Move to (x1, y1)
# turtle.pendown()
# turtle.write("Point 1") 
# turtle.goto(x2, y2) # draw a line to (x2, y2)
# turtle.write("Point 2")
# # Move to the center point of the line
# turtle.penup()
# turtle.goto((x1 + x2) / 2, (y1 + y2) / 2) 
# turtle.write(distance)
# turtle.done()