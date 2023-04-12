# user enter his/her name and program count the characters inname

name=input("Enter Your name :")
i=0
temp =""
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i=i+1
