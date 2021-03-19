a = int(input())
if (a%2==1):
    print('NO')
else:
    if (a // 5000 % 2 == 1):
        print("NO")
    elif (a % 5000 // 500 % 2 == 1):
        print("NO")
    elif(a % 5000 % 500 // 100 % 2 == 1):
        print("NO")
    elif(a % 5000 % 500 % 100 // 50 % 2 ==1 ):
        print("NO")
    elif (a % 5000 % 500 % 100 % 50 // 10 % 2 == 1):
        print("NO")
    elif(a % 5000 % 500 % 100 % 50 % 10 // 5 % 2 == 1):
        print("NO")
    elif (a % 5000 % 500 % 100 % 50 % 10 % 5 // 2 % 2 == 1):
        print("NO")
    else:
        print("YES")
