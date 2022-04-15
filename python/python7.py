# class Rectangle:
#     def __init__(self, width = 1, height =2):
#         self.width = width
#         self.height = height
    
#     def getArea(self):
#         return self.width * self.height
    
#     def getPerimeter(self):
#         return 2*(self.width + self.height)
    
# def main():
#     r1 = Rectangle(4,40)
#     print("width = ", r1.width)
#     print("height", r1.height)
#     print("Area = ", r1.getArea())
#     print("Perimeter = ", r1.getPerimeter())
# main()

# import math

# class QE:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def getA(self):
#         return self.a
#     def getB(self):
#         return self.b
#     def getC(self):
#         return self.c
#     def getDiscriminant(self):
#         return self.b * self.b - 4 * self.a * self.c
#     def getRoot1(self):
#         if self.getDiscriminant() < 0:
#             return 0
#         else :
#             return(-self.b+self.getDiscriminant()) / (2*self.a)
#     def getRoot2(self):
#         if self.getDiscriminant() < 0:
#             return 0
#         else :
#             return(-self.b-self.getDiscriminant()) / (2*self.a)

# def main():
#     a,b,c = eval(input("Enter a, b, c : "))
#     eq = QE(a,b,c)
#     disc = eq.getDiscriminant()

#     if disc < 0:
#         print("No roots")
#     elif disc == 0 :
#         print("Root = ", eq.getRoot1())
#     else :
#         print("Roots = ", eq.getRoot1(), "and", eq.getRoot2())

# main()

import time
import random

class StopWatch :
    def __init__(self) :
        self.startTime = time.time()
    def getStartTime(self) :
        return self.startTime
    def getEndTime(self) :
        return self.endTime
    def start(self):
        self.startTime = time.time()
    def stop(self) :
        self.endTime = time.time()
    def getElapsedTime(self):
        return int(1000 * (self.endTime - self.startTime))

def main():
    size = 1000000

    stopWatch = StopWatch()
    sum = 0
    for i in range(1, size+1):
        sum += i
    stopWatch.stop()

    print("The loop time : ", stopWatch.getElapsedTime(), "milliseconds")

main()