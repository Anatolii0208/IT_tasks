import math
n1 = int(input())
n2 = int(input())
if n1*50 < (n2-1)*70+1 or (n1-1)*50+1 > n2*70:
    print(-1)
else:
    d = []
    d.append(math.ceil(n1*50 / 60))
    d.append(math.ceil(((n1-1)*50+1) / 60))
    d.append(math.ceil(n2*70 / 60))
    d.append(math.ceil(((n2-1)*70+1) / 60))
    if (max(d[3],d[1]) == (min(d[0],d[2]))):
        print((min(d[0],d[2])))
    else:
        print((max(d[3],d[1])),(min(d[0],d[2])))
