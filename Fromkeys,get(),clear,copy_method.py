# fromkeys method    (assigning same value by this method)

# d=dict.fromkeys(['name','age','height'],'unknown')
# d1=dict.fromkeys(('name','age','height'),'unknown')
# d2=dict.fromkeys("abc",'unknown')
# d3=dict.fromkeys(range(1,11),'unknown')
# d4=dict.fromkeys(['name','age'],['unknown','unknown']) 
# print(d)
# print(d1)
# print(d2)
# print(d3)
# print(d4)

# get method 

d={'name':'unknown','age':'unknown'}
# print(d['name'])
# print(d['names'])  There is a error(to handle this error we use get() method)
print(d.get('name'))  #if i write "names" instead of name then it returns "None" not a error
# if 'name' in d:
#     print('present')
# else:
#     print("not present")

#Shortcut method by get() metod
# if d.get('name'):
#     print("prsent")
# else:
#     print("not present") 


# clear() method

# d.clear()  
# print(d)  

d1=d.copy()
print(d1)

