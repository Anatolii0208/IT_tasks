import math
k = int(input())
p = int(input())
print((round((-1*(2*k - p) + math.sqrt((2*k-p)**2- 4*k)) // 2) +1)*20)
print((round((-1*(2*k - p) - math.sqrt((2*k-p)**2- 4*k)) // 2) +1)*20)
