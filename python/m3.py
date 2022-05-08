import random
List = []
for _ in range(0, 5):
    List.append(random.randint(0,51))

for i in List:
    print("card", i, end=" ")
    res = divmod(i,13)
    if(res[0] == 0):
        print("♠", end=" ")
        if(res[1] == 0):
            print("A", end=" ")
        elif(res[1] == 11):
            print("J", end=" ")
        elif(res[1] == 12):
            print("Q", end=" ")
        elif(res[1] == 13):
            print("K", end=" ")
        else:
            print(res[1], end=" ")
        
    elif(res[0] == 1):
        print("♥", end=" ")
        if(res[1] == 0):
            print("A", end=" ")
        elif(res[1] == 11):
            print("J", end=" ")
        elif(res[1] == 12):
            print("Q", end=" ")
        elif(res[1] == 13):
            print("K", end=" ")
        else:
            print(res[1], end=" ")

    elif(res[0] == 2):
        print("◆", end=" ")
        if(res[1] == 0):
            print("A", end=" ")
        elif(res[1] == 11):
            print("J", end=" ")
        elif(res[1] == 12):
            print("Q", end=" ")
        elif(res[1] == 13):
            print("K", end=" ")
        else:
            print(res[1], end=" ")

    elif(res[0] == 3):
        print("♣", end=" ")
        if(res[1] == 0):
            print("A", end=" ")
        elif(res[1] == 11):
            print("J", end=" ")
        elif(res[1] == 12):
            print("Q", end=" ")
        elif(res[1] == 13):
            print("K", end=" ")
        else:
            print(res[1], end=" ")

    print()

