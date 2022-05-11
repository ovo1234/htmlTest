# isCovered = 99 * [False]
# endOfInput = False
# while not endOfInput:
#     s = input("Enter a line of numbers separated by spaces : " )
#     items = s.split()
#     lst = [eval(x) for x in items]

#     for number in lst:
#         if number == 0 :
#             endOfInput = True
#         else : 
#             isCovered[number - 1] = True

# allCovered = True
# for i in range(99) :
#     if not isCovered[i]:
#         allCovered = False
#         break

# if allCovered :
#     print("The tickets cover all numbers")
# else :
#     print("The tickets don't cover all numbers")

# deck = [x for x in range(0,52)]
# suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
# ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# import random
# random.shuffle(deck)

# for i in range(4):
#     suit = suits[deck[i] // 13]
#     rank = ranks[deck[i] % 13]
#     print("Card number", deck[i], "is", rank, "of", suit)

# def main():
#     x = 1
#     y = [1,2,3]
#     m(x,y)
#     print("x is ", x)
#     print("y[0] is ", y[0])
    
# def m(num, nums):
#     num = 1001
#     nums[0] = 5555
# main()

# def add(x, lst=[]):
#     if not(x in lst):
#         lst.append(x)
#     return lst

# list1 = add(1)
# print(list1)
# list2 = add(2)
# print(list2)
# list3 = add(3,[11,12,13,14])
# print(list3)
# list4 = add(4)
# print(list4)

# def main() :
#     lst = [1,2,3,4,5]
#     reverse(lst)

#     for value in lst:
#         print(value,end=' ')

# def reverse(lst):
#     newLst = len(lst) * [0]

#     for i in range(len(lst)):
#         newLst[i] = lst[len(lst) - 1 - i]

#     lst = newLst
#     for value in lst:
#         print(value, end=' ')
# main()

def main():
    list1 = m(1)
    print(list1)
    list2 = m(1)
    print(list2)

def m(x, lst = [1,1,2,3]):
    if x in lst:
        lst.remove(x)
    return lst
main()