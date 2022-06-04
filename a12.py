a=input("ENTER YOUR STRING : ")
b='''!_-.%()[]',<>}${/;:|'''
str1=" "
for i in a:
    if i not in b:
        str1+=i
print("STRING WITHOUT PUNCTUATION IS : ",str1)
