a=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
print("POSITIVE NUMBERS ARE : ")
for i in range(0,len(a)):
    if(a[i]<0):
        continue
    else:
        print(a[i])