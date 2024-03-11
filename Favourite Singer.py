n= int(input())                # Reading input from STDIN
l=list(map(int,input().split()))
fr={}
for i in l:
    if i in fr:
        fr[i]+=1
    else:
        fr[i]=1

l1=list(fr.values())
m=max(l1)
c=0
for i in range(len(fr)):
    if m==l1[i]:
        c+=1
print(c)
