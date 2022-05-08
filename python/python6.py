# def max(n1,n2):
#     if n1 > n2 :
#         result = n1
#     else : 
#         result = n2
#     return result

# max(10,30) # 그냥 값이 입력만 됨
# print(max(10,30)) # 값이 출력됨

# def gcd(n1, n2):
#     gcd = 1
#     k = 2

#     while k <= n1 and k <= n2:
#         if n1 % k ==0 and n2 % k == 0:
#             gcd = k
#         k += 1
    
#     return gcd

# def isPrime(num):
#     divisor = 2
#     while divisor <= num / 2:
#         if num % divisor == 0:
#             return False
#         divisor += 1
#     return True

# def printPrimeNumbers(numOfPrimes):
#     num_of_primes = 50
#     num_of_primes_per_line = 10
#     count = 0
#     num = 2

#     while count < numOfPrimes :
#         if isPrime(num):
#             count += 1

#             print(num, end=" ")
#             if count % num_of_primes_per_line == 0:
#                 print()

#         num += 1

# def main():
#     print("The first 50 prime num are")
#     printPrimeNumbers(50)
# main()

import turtle as t

def drawLine(x1, y1, x2, y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
def writeText(s,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(s)
def drawPoint(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
def drawCircle(x,y,r):
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.circle(r)
def drawRectangel(x,y,width,height):
    t.penup()
    t.goto(x+width/2 , y+height /2)
    t.pendown()
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

def main():
    drawLine(-50,-50,50,50)
    writeText("Testing useful Turtle functions",-50,-60)
    drawPoint(0,0)
    drawCircle(0,0,80)
    drawRectangel(0,0,60,40)
    t.hideturtle()
    t.done()
main()