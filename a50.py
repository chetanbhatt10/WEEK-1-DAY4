a=[]
sume=0
sumo=0
num=int(input("TOTAL ELEMENTS OF LIST : "))
for i in range(0,num):
    value=int(input("INPUT IS : "))
    a.append(value)
for i in range(0,len(a)):
    if(a[i]%2==0):
        sume+=a[i]
    else:
        sumo+=a[i]
print("SUM OF EVEN NUMBERS IS : ",sume)
print("SUM OF ODD NUMBERS IS : ",sumo)