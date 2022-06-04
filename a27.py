a=[]
max=0

num=int(input("TOTAL NUMBER OF ELEMENT ARE : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    a.append(value)
min=a[0]
for i in range(0,len(a)):
    if(a[i]>max):
        max=a[i]
    if(a[i]<min):
        min=a[i]
print("LARGEST NUMBER IS : ",max)
print("MINIMUM NUMBER IS : ",min)

    
