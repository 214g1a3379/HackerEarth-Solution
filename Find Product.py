n = int(input())                # Reading input from STDIN
l=list(map(int,input().split()))
res=1
for i in range(n):
    res=(res*l[i])%(10**9+7)  
print(res)
