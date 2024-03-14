n=input()
num=[]
ascii=[48,49,50,51,52,53,54,55,56,57]
vowel=["A","E","I","O","U","Y"]
s=list(n)
for i in range(len(s)):
    if ord(s[i]) in ascii:
        num.append(int(s[i]))
if n[2] not in vowel:
    if (num[0]+num[1])%2==0 and (num[2]+num[3])%2==0 and (num[3]+num[4])%2==0 and (num[-1]+num[-2])%2==0 :
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")
