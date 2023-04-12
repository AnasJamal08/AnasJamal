# function returning two values
def func(int1,int2):
    add=int1+int2
    multiply=int1*int2
    return add,multiply


# print(func(2,3))   #The output is always like tuple (5,6),Now we have to resolve this

add,multiply=func(2,3)
print(add)
print(multiply) 