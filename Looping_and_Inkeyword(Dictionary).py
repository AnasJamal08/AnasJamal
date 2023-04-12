user_info=dict(
    name="Anas",
    age=21,
    fav_movies=['KGF','300']
)
# check if key exist in Dictionary
if 'name' in user_info:
    print('present')
else:
    print("Not present")


# For values

if 'Anas' in user_info.values():
    print('present')
else:
    print("Not present")


# Loops
for i in user_info.values():
    print(i)


for i in user_info:
    print(i)    

# --------------------------------------------------------------------------
# values method
# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# ---------------------------------------------------------------------------
# keys method 

# user_info_keys=user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))


# ----------------------------------------------------------------------

# items method(Imp)
# user_items=user_info.items()
# print(user_items)  #dict_items([('name', 'Anas'), ('age', 21), ('fav_movies', ['KGF', '300'])])
# print(type(user_items))


for key,value in user_info.items():
    print(f"key is {key} and value is {value}")