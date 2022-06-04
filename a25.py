a=[]
pnum=0
nnum=0
num=int(input("ENTER TOTAL NUMBER OF ELEMENTS : "))
for i in range(0,num):
    value=int(input("ELEMENT IS : "))
    a.append(value)
for i in range(0,num):
    if(a[i]>0):
        pnum+=1
    else:
        nnum+=1
print("POSITIVE NUMBERS ARE : ",pnum)
print("NEGATIVE NUMBERS ARE : ",nnum)