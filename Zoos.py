n=input()
l=[]
cz=0
co=0
for i in n:
    l.append(i)
for i in range(len(l)):
    if l[i]=='z':
        cz+=1
    elif l[i]=='o':
        co+=1
if 2*cz==co:
    print("Yes")
else:
    print("No")
