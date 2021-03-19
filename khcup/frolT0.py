itaration = 0
position = int(input())
while position != 0:
    print('shift_left ' * (position-1) + 'shift_right '*itaration)
    itaration = (itaration + 2) % 10
    position = int(input())
