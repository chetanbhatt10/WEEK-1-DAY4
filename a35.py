a=[1,2,3,4,5,6,7,8,9,10]
print("element at odd index : ")
for i in range(0,len(a)):
    if(i%2==0):
        continue
    else:
        print(a[i])