# strings are immutable

string="abcd"
print(string[1])

# string[1]='B'     ** once string is intialize then you cannot change it**

print(string.replace("b","B"))

string.replace("b","B")
print(string)        #replace menthod cannot change the original string but it created new string.
#  You can store it into new variable

new_string=string.replace("b","B")
print(new_string)