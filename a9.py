a=input("ENTER Yout string : ")
str1=" "
def chkIND(N):
    if(N%2==0):
        return 0
    else:
        return 1
for i in range(len(a)):        
    if(chkIND(i)==1):
        continue
    else:
        str1+=a[i]
print(str1)