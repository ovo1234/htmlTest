# 3주차

import turtle as t

t.pensize(3)
t.penup()
t.goto(-200,-50)
t.pendown()
t.color("red")
t.begin_fill()
t.setheading(60) # 시작위치
t.circle(30, steps=3) # 삼각형 그리기
t.end_fill()

t.pensize(3)
t.penup()
t.goto(-100,-50)
t.pendown()
t.color("blue")
t.begin_fill()
t.setheading(45)
t.circle(30, steps=4) # 삼각형 그리기
t.end_fill()

t.pensize(3)
t.penup()
t.goto(0,-50)
t.pendown()
t.color("green")
t.begin_fill()
t.setheading(35) # 시작위치
t.circle(30, steps=5) # 삼각형 그리기
t.end_fill()

t.pensize(3)
t.penup()
t.goto(100,-50)
t.pendown()
t.color("yellow")
t.begin_fill()
t.setheading(30) # 시작위치
t.circle(30, steps=6) # 삼각형 그리기
t.end_fill()

t.pensize(3)
t.penup()
t.goto(200,-50)
t.pendown()
t.color("purple")
t.begin_fill()
t.circle(30) # 삼각형 그리기
t.end_fill()

t.penup()
t.goto(-100,50)
t.pendown()
t.color("green")
t.write("Colorful Shapes", font = ("times", 18, "bold"))


t.done()