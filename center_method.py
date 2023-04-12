# center method
name="Anas"
# **Anas**  ,8
print(name.center(8,"*"))
# *Anas*  ,6
print(name.center(6,"*"))
# **Anas*  , 7
print(name.center(7,"*"))


name1=input("Enter your name  : ")
print(name1.center(len(name1)+8,"*"))