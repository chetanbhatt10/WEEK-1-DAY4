a=input("ENTER YOUR STRING : ")
b=input("ENTER YOUR CHARACTER : ")
pos=0
temp=0
for i in a:
    pos+=1
    if(i==b):
        temp=pos
print(temp)
