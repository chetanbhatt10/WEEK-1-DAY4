a=[]
b=[]
num=int(input("TOTAL ELEMENTS OF LIST : "))
for i in range(0,num):
    value=int(input("INPUT IS : "))
    a.append(value)
x=int(input("HOW MUCH ELEMENTS YOU WANT TO ROTATE LEFT : "))
print("BEFORE LEFT ROTATING : ",a)
print("AFTER LEFT ROTATING : ")
b=a[x:]+a[:x]
print(b)

