a=[1,2,3,4,5,6,7,8,9,10]
elst=[]
olst=[]
for i in range(0,len(a)):
    if(a[i]%2==0):
        elst.append(a[i])
    else:
        olst.append(a[i])
print("EVEN INTEGER LIST : ",elst)
print("ODD INTEGER LISt : ",olst)