name2="       Anas      "
name1="   An   as     "
dots=".........."
# lstrip method 
print(name2.lstrip()+dots)
print(name2.rstrip()+dots)   #lstrip and rstrip cannot remove spaces from the middle of any letter
                                #For this we have to use replace method
print(name2.strip()+dots)
print(name1.replace(" ","")+dots)



name,char=input("Enter your name and character which Uwant to count (comma separated) ").split(",")
# print ("Length of name is : ")
# print(len(name))
print (f"Length of name is : {len(name)}")
# print ("The number of letters is : ")
# print(name.count(char))
# print (f"The number of letters is : {name.count(char)}")
print (f"The number of letters is : {name.strip().lower().count(char.strip().lower())}")    #insqensitive case



