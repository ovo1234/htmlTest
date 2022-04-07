# money = True
# if money :
#     print("택시를 타고 가라")
# else :
#     print("걸어가라")

# x = 3
# y = 2
# x > y


# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket :
#     print("택시를 타고 가라")
# else :
#     print("걸어가라")

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." %treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# coffee = 10
# money = 300
# while money :
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0 : continue
#     print(a)

# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i, end=" ") # 출력할 때 엔터가 아니라 바로 옆에 출력됨.

# a = [(1,2),(3,4),(5,6)]
# for (first, last) in a :
#     print(first + last)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end=" ")
#     print(' ')


# 사칙 연산 계산기 코딩 작성
def add(num1, num2):
    return num1 + num2
def min(num1, num2) : 
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

## 나머지 값 출력
## 몫 만을 출력

def rest(num1, num2):
    return num1 % num2
def share(num1, num2):
    return num1 // num2

while True : 
    print("계산기를 종료하시면 숫자 0을 입력하세요.")
    num1 = int(input("첫번째를 입력하세요 : "))

    if(num1 == 0 ):
        print("계산기를 종료합니다.")
        break
    Cal = str(input("+ - * / % //고르시오."))
    num2 = int(input("두번째 숫자를 입력하세요 : "))

    if(Cal == '+'):
        result = add(num1,num2)
    elif(Cal == '-'):
        result = min(num1,num2)
    elif(Cal == '*'):
        result = mul(num1,num2)
    elif(Cal == '/'):
        result = div(num1,num2)
    elif(Cal == '/'):
        result = div(num1,num2)
    elif(Cal == '%'):
        result = rest(num1,num2)
    elif(Cal == '//'):
        result = share(num1,num2)
    else : 
        print("입력방식이 잘못되었습니다.")
        continue
    
    print("결과 : {} {} {} {}" .format(num1 , Cal, num2, result))

