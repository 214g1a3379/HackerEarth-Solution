L=int(input())
n=int(input())
for i in range(n):
    w,h=map(int,input().split())
    if w<L or h<L:
        print("UPLOAD ANOTHER")
    else:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
