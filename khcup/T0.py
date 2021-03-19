'''o = 1
sch = 1
o = int(input())
while(o != 0):
    m = (sch-1) % 5 * 2 + 1
    if o > m:
        i = 0
        for i in range(o - m):
            print("shift_left",end = " ")
    elif o < m:
        for i in range(m - o):
            print("shift_right",end = " ")
    else:
        print("shift_left shift_right", end = " ")
    sch+=1
    o = int(input())'''
o = 1
sch = 1
o = int(input())
while(o != 0):
    m = (sch-1) % 5 * 2 + 1
    if o > m:
        i = 0
        l = o - m - 1
        for i in range(l):
            print("shift_left",end = " ")
        print("shift_left")
    elif o < m:
        i = 0
        ll = m - o - 1
        for i in range(ll):
            print("shift_right",end = " ")
        print("shift_right")
    else:
        print()
    sch+=1
    o = int(input())
