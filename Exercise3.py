name,char=input("Enter your name and character which Uwant to count (comma separated) ").split(",")
# print ("Length of name is : ")
# print(len(name))
print (f"Length of name is : {len(name)}")
# print ("The number of letters is : ")
# print(name.count(char))
# print (f"The number of letters is : {name.count(char)}")
print (f"The number of letters is : {name.lower().count(char.lower())}")    #insqensitive case
