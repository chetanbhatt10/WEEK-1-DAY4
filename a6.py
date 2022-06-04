a=input("ENTER YOUR STRING : ")
str1=" "
for i in range(len(a)):
    if(a[i]==" "):
        str1+="_"
    else:
        str1+=a[i]
print(str1)