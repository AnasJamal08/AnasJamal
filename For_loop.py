# # # # # for loop with range function
# # # # for i in range(10):  # 0 to 9
# # # #         print(f"Hello world : {i}")

# # # --------------------------------------------------------------------

# # # # for loop with range function
# # # for i in range(1, 11):  # 1 to 10
# # #         print(f"Hello world : {i}")

# # # ---------------------------------------

# # # # Example 1
# # # total=0
# # # for i in range(1,11):
# # #     total+=i
# # # print(total)

# # # --------------------------------------------------------------------

# # n=int(input("Enter a Number : "))
# # total=0
# # for i in range(1,n+1):
# #     total+=i
# # print(total)

# # # ---------------------------------------------------------------------


# # Example 2

# # ask user a number lik this 1234
# # calculate sum of digits ---------->1+2+3+4

# total=0
# num=input("Enter a number : ")
# for i in range(0,len(num)):
#     total+=int(num[i])
# print(total)


# # --------------------------------------------------------------------------

# # Example 3

# user enter his/her name and program count the characters in name

name=input("Enter Your name :")
temp =""
for i in range(0,len(name)):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    
