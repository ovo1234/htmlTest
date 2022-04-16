# # 3주차

# import turtle as t

# t.pensize(3)
# t.penup()
# t.goto(-200,-50)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.setheading(60) # 시작위치
# t.circle(30, steps=3) # 삼각형 그리기
# t.end_fill()

# t.pensize(3)
# t.penup()
# t.goto(-100,-50)
# t.pendown()
# t.color("blue")
# t.begin_fill()
# t.setheading(45)
# t.circle(30, steps=4) # 삼각형 그리기
# t.end_fill()

# t.pensize(3)
# t.penup()
# t.goto(0,-50)
# t.pendown()
# t.color("green")
# t.begin_fill()
# t.setheading(35) # 시작위치
# t.circle(30, steps=5) # 삼각형 그리기
# t.end_fill()

# t.pensize(3)
# t.penup()
# t.goto(100,-50)
# t.pendown()
# t.color("yellow")
# t.begin_fill()
# t.setheading(30) # 시작위치
# t.circle(30, steps=6) # 삼각형 그리기
# t.end_fill()

# t.pensize(3)
# t.penup()
# t.goto(200,-50)
# t.pendown()
# t.color("purple")
# t.begin_fill()
# t.circle(30) # 삼각형 그리기
# t.end_fill()

# t.penup()
# t.goto(-100,50)
# t.pendown()
# t.color("green")
# t.write("Colorful Shapes", font = ("times", 18, "bold"))


# t.done()

# a= max(2,3,4)
# min(2,3,4)
# round(3.51)
# round(3.4)
# abs(-1)
# pow(2,4)
# print(a)

# import math as m

# x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points "))

# a = m.sqrt((x2-x3) * (x2-x3) + (y2-y3) * (y2-y3))
# b = m.sqrt((x1-x3) * (x1-x3) +(y1-y3) * (y1-y3))
# c = m.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))

# A = m.degrees(m.acos((a*a - b*b - c*c) / (-2 * b * c)))
# B = m.degrees(m.acos((b*b - a*a - c*c) / (-2 * a * c)))
# C = m.degrees(m.acos((c*c - b*b - a*a) / (-2 * a * b)))

# print("The three angles are ", round(A*100) / 100.0, round(B*100) / 100.0 , round(C*100) / 100.0)

# # Receive the amount 
# amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# # Convert the amount to cents
# remainingAmount = int(amount * 100)

# # Find the number of one dollars
# numberOfOneDollars = int(remainingAmount / 100)
# remainingAmount = int(remainingAmount % 100)

# # Find the number of quarters in the remaining amount
# numberOfQuarters = int(remainingAmount / 25)
# remainingAmount = remainingAmount % 25

# # Find the number of dimes in the remaining amount
# numberOfDimes = int(remainingAmount / 10)
# remainingAmount = remainingAmount % 10

# # Find the number of nickels in the remaining amount
# numberOfNickels = int(remainingAmount / 5)
# remainingAmount = remainingAmount % 5

# # Find the number of pennies in the remaining amount
# numberOfPennies = remainingAmount

# # Display results
# print("Your amount", amount, "consists of\n", 
#     "\t", numberOfOneDollars, "dollars\n", 
#     "\t", numberOfQuarters, "quarters\n",
#     "\t", numberOfDimes,  "dimes\n",
#     "\t", numberOfNickels, "nickels\n",
#     "\t", numberOfPennies, "pennies")

# money = input("Enter money : ")

# remainAmount = int(money)

# numOfGr = int(remainAmount / 10000)
# remainAmount = int(remainAmount % 10000)

# numOfBl = int(remainAmount / 1000)
# remainAmount = int(remainAmount % 1000)

# numOfCoin = int(remainAmount / 100)
# remainAmount = int(remainAmount % 100)

# print("Money : ", numOfGr , "만원", numOfBl, "천원", numOfCoin, "백원")