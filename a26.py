a=[]
max=0
num=int(input("TOTAL NUMBER OF ELEMENTS ARE : "))
for i in range(0,num):
    value=int(input("TOTAL ELEMENT's ARE : "))
    a.append(value)
for i in range(0,len(a)):
    if(a[i]>max):
        max=a[i]
print("MAXIMUM ELEMENT IS : ",max)

