number = eval(input('Enter the number of pyramid:'))

cnt = 1
for i in range(1,number+1):
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(1, number*2-i+1):
        print(j, end=" ")
        if j== number+1-i:
            for d in range(number-i,0,-1):
                print(d, end=" ")
            break;

    print()
