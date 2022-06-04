a=input("ENTER YOUR STRING:")
temp=0
for i in range(len(a)):
    if(a[i]!=a[len(a)-i-1]):
        temp=1
        break
if(temp==0):
    print("PALINDROM")
else:
    print("NOT A PALINDROM")

    