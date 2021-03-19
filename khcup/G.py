
l = int(input())
r = int(input())
t = int(input())
l = l + t - 1
l = l - (l % t)
r = r - (r % t)
print(((r - l) // t) + 1)
