# count = 1

# for i in range(100,201):
#     if not(i%5 == 0 and i%6 == 0) and (i%5==0 or i%6 ==0):
#         if count%10 != 0:
#             print(i,end=" ")
#         else : 
#             print(i)
#         count += 1

# for i in range(1, 6+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# for i in range(1, 6+1):
#     for j in range(1, 7-i+1):
#         print(j, end=" ")
#     print()

# for i in range(1, 6+1):
#     for j in range(6-i, 0 , -1):
#         print(" ", end=" ")
    
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

pi = 1
sign = 1

for i in range(2, 10000000+1):
    sign = -sign
    pi += sign / (2*i - 1)

    if i % 100000 == 0:
        print("i = ", i ,"Pi is ", 4*pi)