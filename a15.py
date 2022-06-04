a=input("ENTER YOUR STRING : ")
c=input("ENTER CHARACTER : ")
ind=0
occ=0
for i in a:
    ind+=1
    if(i==c):
        occ+=1
        print("FOUND AT ",ind)
print("TOTAL OCCURANCE : ",occ)