# 20220304 숙제

print(4 * (1- 1/3 +1/5 -1/7 +1/9 -1/11 +1/13 -1/15 +1/17 -1/19 +1/21 -1/23))

# 미국인구가 7초마다 1명씩 출산 13초씩 1명 사망 45초마다 새로운 이민지가 들어옴.
# 현재인구 : 3억 1천 2백만명

totalSecond = 365 * 24 * 60 * 60
print(312032486 + totalSecond//7 - totalSecond//13 +totalSecond//45)

# 별 그리기

import turtle 

turtle.penup()
turtle.goto(0,100)
turtle.down()

turtle.right(72)
turtle.forward(100)

turtle.right(144)
turtle.forward(100)

turtle.right(144)
turtle.forward(100)

turtle.right(144)
turtle.forward(100)

turtle.right(144)
turtle.forward(100)

turtle.done()