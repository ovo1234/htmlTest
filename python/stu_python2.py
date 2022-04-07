# 함수 만들기
def Add(a,b) :
    return a + b

def Sub(a,b) :
    return a - b

def Mul(a,b) :
    return a * b

def Div(a,b):
    return a / b

def Sha(a,b):
    return a % b

def Rest(a,b):
    return a // b

# class 로 만들어서 하는 방법은 다음에
class bb:

    while True: # 잘못입력하면 반복해주는 코드
        num1 = int(input("정수를 입력하세요 "))
        Cal = str(input("기호(+,-,*,/,%,//)를 입력하세요 / end를 입력하면 계산기를 끝냅니다."))
        if(Cal == "end"):
            print("계산기를 끝내겠습니다.")
            break
        num2 = int(input("정수를 입력하세요 "))
        result = 0

        if(Cal == "+"):
            result = Add(num1,num2)
        elif(Cal == "-"):
            result = Sub(num1,num2)
        elif(Cal == "*"):
            result = Mul(num1,num2)
        elif(Cal == "/"):
            result = Div(num1,num2)
        elif(Cal == "%"):
            result = Sha(num1,num2)
        elif(Cal == "//"):
            result = Rest(num1,num2)
        else : 
            print("잘못입력하였습니다.")
            continue

        # print(num1 , Cal, num2, " = ", result)

        # format 을 f로 바꾸어도 된다.
        print("{} {} {} = {}" .format(num1, Cal, num2, result))
        # print(f"{num1} {Cal} {num2} = {result}")




