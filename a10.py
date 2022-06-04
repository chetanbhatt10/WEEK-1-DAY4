a=input("ENTER YOUR STRING : ")
b=input("ENTER CHARACTER YOU WANTS TO CHECK : ")
stq=" "
for i in range(len(a)):
    if(a[i]==b):
        stq+=a[0:i]+a[i+1:len(a)]
        break
print(stq)
