a=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
plst=[]
nlst=[]
for i in range(0,len(a)):
    if(a[i]<0):
        nlst.append(a[i])
    else:
        plst.append(a[i])
print("POSITIVE INTEGER LIST : ",plst)
print("NEGATIVE INTEGER LIST : ",nlst)