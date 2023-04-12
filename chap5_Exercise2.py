
# import numbers


# def reverse_list(l):
#     l.reverse()
#     return l
# numbers=[1,2,3,4]
# print(reverse_list(numbers))



# ------------------------------>
# def reverse_list(l):
#     return l[::-1]
    

# numbers=[1,2,3,4]
# print(reverse_list(numbers))


# ------------------------------------->
# by pop amnd append method
def reverse_list(l):
    r_list=[]
    for i in range(len(l)):
        popped_item=l.pop()
        r_list.append(popped_item)
    return r_list



numbers=[1,2,3,4]
print(reverse_list(numbers))
