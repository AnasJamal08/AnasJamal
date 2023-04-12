# # data structure
# # ordered collection of items
# # how to add data in list
# fruits=['apple','grapes']
# fruits.append("mango")     #append method add word at the last of string
# fruits[1]="Banana"     #Now grapes are replace with Banana
# print(fruits)

# ------------------------------------------->
# More methods to add data in list
# fruits1=['apple','grapes']
# fruits1.insert(1,"orange")   #insert method
# print(fruits1)

# -------------------------------------------->
# fruits2=['apple','grapes']
# fruits3=["mango","orange"]     
# fruit=fruits2+fruits3
# print(fruit)

# ------------------------------------------------->
# fruits2=['apple','grapes']
# fruits3=["mango","orange"]
# fruits2.extend(fruits3)
# print(fruits2)


# ------------------------------------->

# Deletion of data from list
# fruits=["orange","apple","orange","pear","banana",'kiwi']
# pop method(mostly used method)
# fruits.pop()    #it will delete last element from list(by default)
# fruits.pop(0)
# print(fruits)

# del method
# del fruits[1]
# print(fruits)

# remove
# fruits.remove("orange")  #it will remove first orange from list
# print(fruits)


# -------------------------->
# to add data in list 
# append,extend,insert 

# To delete data from list
# pop,remove,del

# ------------------------------------------------->
# # In keyword
# fruits=["orange","apple","orange","pear","banana",'kiwi']
# if 'apple' in fruits:
#     print("apple is present")
# else:
#     print("apple is not present")

# # ------------------------------------------------->
# fruits=["orange","apple","orange","pear","banana",'kiwi']
# # print(fruits.count("orange"))  
# # To sort words alphabetically
# fruits.sort()
# print(fruits)

# --------------------------------------------------->
# numbers=[3,5,1,2,7,8,4]
# numbers.sort()    #sort method sort the original list
# print(numbers)


# -------------------------------->
# # sorted Function
# numbers=[3,5,1,2,7,8,4]
# print(sorted(numbers))    #sorted function does not change orginal string but it creates new list and sort it
# print(numbers)

# ----------------------------------->
# clear method\
numbers=[3,5,1,2,7,8,4]
# numbers.clear()
num_copy=numbers.copy()
print(num_copy)