a = int(input())
n = 1
while (a != 0):
    if (n > 9):
        n = 1
    if (a - n >= 0):
        if (a - n != 0):
            for i in range(a - n - 1):
                print('shift_left',end = ' ')
            print('shift_left')
    else:
        for i in range(abs(a - n) - 1):
            print('shift_right',end = ' ')
        print('shift_right')
    n += 2
    a = int(input())
