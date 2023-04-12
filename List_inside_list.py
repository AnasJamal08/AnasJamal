# list=[[1,2,3],[4,5,6],[7,8,9]]
# # print(list[2])
# for sublist in list:
#     for i in sublist:
#         print(i)


# # ---------------------------------------->    
# list=[[1,2,3],[4,5,6],[7,8,9]]   #2d list
# print(list[1][1])  #5
# print(list[1][2])  #6
# print(list[2][2])  #9
# print(type(list))

# ---------------------------------->
# numbers=list(range(1,11))   #creating list with range function
# # print(numbers)
# print(numbers.pop())  # ==10


# ------------------------------------------>
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(numbers.index(1,3))   #index(elementwhich you want to locate(position),search from where)


# ------------------------------------->
# pass list to a function
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative


print(negative_list(numbers))