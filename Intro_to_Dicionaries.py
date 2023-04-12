# What are Dictionaries
# unordered collection of data in key : value pair.
# 1st method
# user={'name':'Anas','age':24}
# print(user)
# print(type(user))
# 2nd method 
user1=dict(name='Anas',age=24)
print(user1)
# how to access data from dictionary
# There are no indexes in Dictionaries Because of unordered collection of data
# How to access data from Dictionary
print(user1['name'])
print(user1['age'])
# Which type of data can be stored in Dictionary?
# anything
# numbers,strings,list,dictionary
user_info=dict(
    name="Anas",
    age=21,
    fav_movies=['KGF','300'],
    user2=dict(
        name='Anas',
        age=21
    )
)
print(user_info['fav_movies'])
print(user_info['user2'])


# How to add data in empty Dictionary
user_info2=dict()
user_info2['name']='Anas'
user_info2['age']=21
print(user_info2)