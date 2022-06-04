a=[]
mul=1
num=int(input("ENTER TOTAL NUMBER OF ELEMENTS : "))
for i in range(0,num):
    value=int(input("ENTER ELEMENTS : "))
    a.append(value)
for i in range(0,len(a)):
    mul*=a[i]
print("MULTIPLICATION OF LIST ELEMNTS ARE : ",mul)
