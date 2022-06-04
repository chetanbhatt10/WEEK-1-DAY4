a=[]
edgt=0
odgt=0
rng=int(input("TOTAL NUMBER OF ELEMENT IN LIST ARE : "))
for i in range(0,rng):
    val=int(input("ELEMENT IS : "))
    a.append(val)
for i in range(len(a)):
    if(a[i]%2==0):
        edgt+=1
    else:
        odgt+=1
print("NUMBER OF EVEN DIGITS ARE : ",edgt)
print("NUMBER OF ODD DIGIT ARE : ",odgt)





