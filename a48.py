a=[]
num=int(input("TOTAL ELEMENTS OF LIST : "))
for i in range(0,num):
    value=int(input("INPUT IS : "))
    a.append(value)
a.sort()
print("SMALLEST ELEMENT I LIST IS : ",a[0])
