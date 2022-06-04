a=[]
sum=0
num=int(input("TOTAL ELEMENTS OF LIST : "))
for i in range(0,num):
    value=int(input("INPUT IS : "))
    a.append(value)
for i in range(0,len(a)):
    sum+=a[i]
print(sum)