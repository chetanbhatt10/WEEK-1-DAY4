def avg(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum/len(a)
a=[]
num=int(input("TOTAL ELEMENTS OF LIST : "))
for i in range(0,num):
    value=int(input("INPUT IS : "))
    a.append(value)
for i in range(0,len(a)):
    if(a[i]>avg(a)):
        print("ELEMENT ABOVE THEN AVERAGE ARE:",a[i])
