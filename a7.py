a=input("ENTER YOUR STRING : ")
c=input("ENTER CHARACTER SYMBOL TO BE REPLACED : ")
n=input("ENTER NEW CHARACTER SYMBOL : ")
str2=" "
for i in range(len(a)):
    if(c==a[i]):
        str2+=n
    else:
        str2+=a[i]
print(str2)