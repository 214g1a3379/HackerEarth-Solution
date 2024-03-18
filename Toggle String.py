name=input()
str1=""
for i in name:
    if i.isupper():
        str1+=i.lower()
    if i.islower():
        str1+=i.upper()

print(str1)
