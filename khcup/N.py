
n=int(input())
k1=int(input())
k2=int(input())
k3=int(input())
kol=0
q=(n//k1)
kol = ((n - k2) // (k2 - k3)) + 1
n = k3 + (n - k2) % (k2 - k3)
kol+=(n//k1)
print(max(kol,q))
