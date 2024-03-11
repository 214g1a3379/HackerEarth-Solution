n=int(input())
for i in range(n):
    r,c=list(map(int,input().split()))
    matrix = []
    for _ in range(r):
        row = list(input().strip())  # Assuming input is a string of characters
        matrix.append(row)
    
    m=[]
    for i in range(r):
        count=0
        for j in range(c):
            if matrix[i][j]=='#':
                count+=1
        m.append(count)
    print(max(m))
