a, b, c = map(int,input().split())
a1, b1, c1 = map(int,input().split())
t1 = []
t2 = []
t1.append(a)
t1.append(b)
t1.append(c)
t2.append(a1)
t2.append(b1)
t2.append(c1)
ans = a + b + c + a1 + b1 + c1 - max(t1) - max(t2) + abs(max(t1) - max(t2))
print(ans)
