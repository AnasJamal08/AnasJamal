# task 1
# ls=[]
# for i in range(1500,2701):
#     if (i%7==0) & (i%5==0):
#         ls.append(i)
# print(ls)

# task 2

# tem=float(input("Enter the value_: "))
# chk=input("Enter the unit of temprature(C/F)_: ")
# if chk=='c' or chk=='C':
#     print(f"temprature in farenhite is {(tem*9)/5+32}")
# elif chk=='f' or chk=='F':
#     print(f"temprature in celcius is {((tem-32)*5)/9}")
# else:
#     print("invalid input")


# task 3

# import random


# num=int(input("Enter the number between 1 and 9_: "))
# win=random.randint(1,11)
# while (True):
#     if num==win:
#         print("Well Guessed")
#         break
#     else:
#         num=int(input("Wrong guess!! \nEnter again_: "))

# task 4


# for i in range(0,6):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")    
# for k in range(6,0,-1):
#     for j in range(0,k):
#         print("*", end=" ")
#     print("\n")


# task 5

# str=input("Enter the string_: ")
# print(str[::-1])

# task 6

# num=(1,2,3,4,5,6,7,8,9)
# even=0
# odd=0
# for i in num:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"Even numbers are_: {even} \nOdd numbers are_: {odd}")


# task 7

# data_list=[1425,11.23,1+2j, True, 'w3resourse',(0,-1),[5,12],{"class":'V',"section":'A'}]

# for i in data_list:
#     print(i,type(i))

# task 8

# for i in range(0,7):
#     if i%3==0:
#         continue
#     else:
#         print(i)


# task 9

# fib=[]
# def fib_fun(num):
#     a, b=0, 1
#     fib.append(a)
#     fib.append(b)
#     for i in range(num-2):
#         c=a+b
#         a=b
#         b=c
#         fib.append(c)

# fib_fun(50)
# print(fib)


# task 10

# for i in range(0,51):
#     if i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")

# task 11

# row=int(input("Enter the rows _: "))
# col=int(input("Enter the cols _: "))
# ls=[[i*j for i in range(col)] for j in range(0,row) ]
# print(ls)

# task 12

# ls=input("Enter the values_: ").split(",")

# # def bin_dec(num):
# #     pow=3
# #     sum=0
# #     for i in range(0,4):
# #         sum=sum + ((int(num[i]))* (2**pow))
# #         pow-=1
# #     return (sum)

# l5=[]
# # for i in ls:
# #     if bin_dec(i)%5==0:
# #         l5.append(i)
# ## alternate method

# for i in ls:
#     if int(i,2)%5:
#         l5.append(i)
# print(l5)


# task 13

# s_num=0
# s_dig=0
# str=input("Enter the string_: ")
# for i in range(len(str)):
#     if type(str[i])== type("string"):
#         s_num+=1
#     elif type(str[i])==int:
#         s_dig+=1
# print(f"letters {s_num} digit {s_dig}")

