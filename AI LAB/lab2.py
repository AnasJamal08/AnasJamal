# # print("Hello world")
# # var=input("Enter any number: ")
# # print(var)

# # for i in range(5):
# #     j=0;
# #     while j<=i:
# #         print("*",end="")
# #         j+=1
# #     print("\n")


# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#   print(type(kid))

# my_function(fname = "Tobias", lname = "Refsnes")




# fun=lambda : print("chal oy")
# fun()

# fun1=lambda a: a + 2

# fun1(1)


# for i in range(6,0,-1):
#     j=0
#     while j<i:
#         print("*",end="")
#         j+=1
#     print("\n")

# for i in range(0,6):
#     for j in range(6,0,-1):
#         if j<=i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n")



# for i in range(5):
#     j=0;
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print("\n")


# temp=0
# for i in range(0,11):
#     temp+=i
#     if i==0:
#         print(f"Current number: {i}    Previous number: {i}    sum:{temp}")
#     else:
#         print(f"Current number: {i}    Previous number: {i-1}    sum:{temp}")
# print(f"total Sum is {temp}")




# class new:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def f1(self):
#         print(f"Hello!!!!\nMy name is {self.name}\nMy age is {self.age}")

# p1=new("ghani",23)
# p1.f1()


st=input("Enter any string_: ")
sub=input("Enter sub string to find_: ")

print(st.count(sub))