t=int(input())
for i in range(t):
    c,n=map(int,input().split())
    sum=(n*(n+1))//2
    if sum<=c:
        c=c-sum
        print(c%n)
    else:
        print(c)
