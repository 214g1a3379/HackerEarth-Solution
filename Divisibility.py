N = int(input())
data = [int(x) for x in input().split()]
li=data[-1]
if li%10==0:
    print("Yes")
else:
    print("No")
