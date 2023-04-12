#                                     # looping in tuple
# ---------------------------------->
# mixed=(1,2,3,4,0)  #tuple
# for i in mixed:
#     print(i)
# We can also use while loop
# --------------------------------------------->

                                       # tuple with one element 
# num=(1)   its wrong

# num=(1,)
# words=('Anas',)
# print(type(num))
# print(type(words))

                                        # tuple without parenthesis

# name_of_bikes='Honda','Metro','Yamaha','Road Prince'
# print(type(name_of_bikes))    #It is a tuple

                                        #  tuple unpacking

# name_of_bikes=('Honda','Metro','Yamaha','Road Prince')
# name1,name2,name3,name4=(name_of_bikes)
# print(name1)
# print(name4)

                                       #list inside tuple

# name_of_bikes=('Honda','Metro',['Yamaha','Road Prince'])
# name_of_bikes[2].pop()
# name_of_bikes[2].append('125')
# print(name_of_bikes)

#   min(),max(),sum(),len() Functions can be used with tuples
#   Tuples are immutable
# But inside tuple if there is a list,then that list is muttable


# -------------------------------------->

# something more about tuples

# nums=tuple(range(1,11))   #creating tuple  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(nums)

nums=str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
nums1=list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(type(nums))       #but output like tuple
print(type(nums1))    #but output like tuple