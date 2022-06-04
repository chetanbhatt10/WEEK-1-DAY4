l=[1,2,3,4]
m=[9,8,7,6]
x=[]
y=[]
z=[]
w=[]
for i in range(0,4):
    x.append(l[i]+m[i])
    y.append(l[i]-m[i])
    z.append(l[i]*m[i])
    w.append(m[i]/l[i])
print("ADDITION OPERATION : ",x)
print("SUBTRACTION OPERATION : ",y)
print("MULTIPLICATION OPERATION : ",z)
print("DIVISION OPERATION : ",w)
