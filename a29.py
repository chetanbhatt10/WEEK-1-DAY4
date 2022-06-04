a=[]
b=[]
c=[]
num=int(input("ENTER TOTAL ELEMENTS : "))
print("ENTER ELEMENT OF LIST A  : ")
for i in range(0,num):
    value=int(input("ELMENTS IS : "))
    a.append(value)
print("ENTER ELEMENT OF LIST B : ")
for i in range(0,num):
    value=int(input("ELEMENTS IS : "))
    b.append(value)
for i in range(0,num):
    c.append(a[i]-b[i])
print(c)
    

