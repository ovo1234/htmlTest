def Add(f,s):
    return f+s

def Sub(f,s):
    return f-s

def Div(f,s):
    if s==0:
        return "0으로 나누어 에러입니다."
    return f/s

def Mul(f,s):
    return f*s

def Sq(f,s):
    return f**s

def Classification(op, f,s):
    if'+'==op:
        print(Add(f,s))
    elif'-'==op:
        print(Sub(f,s))
    elif'/'==op:
        print(Div(f,s))
    elif'*'==op:
        print(Mul(f,s))
    elif'**'==op:
        print(Sq(f,s))

FirNum = eval(input('첫 번째 숫자:'))
Operator = input('연산자:')
SecNum = eval(input('두 번째 숫자:'))

Classification(Operator, FirNum, SecNum)
