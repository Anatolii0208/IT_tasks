n=int(input())
m=int(input())
for i in range(min(n,m),(max(n,m)+1)):
    a=i//1000
    d=(i%10)
    c=(i//10)%10
    b=(i//100)%10
    if (a==b==c) or (a==b==d) or (b==c==d) or (a==c==d):
        print(i)
