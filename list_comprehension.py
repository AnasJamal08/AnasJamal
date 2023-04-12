# We can create list in one line 
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)


# Now in one line
square2=[i**2 for i in range(1,11)]   #list comprehension
print(square2)

neagative=[-i for i in range(1,11)]
print(neagative)


new_list=[]
lists=['Anas','Jamal','Din']
# new_list-['A','J','D']
for name in lists:
    new_list.append(name[0])
print(new_list)



# Now by list comprehension
new_list1=[name[0] for name in lists]
print(new_list1)




