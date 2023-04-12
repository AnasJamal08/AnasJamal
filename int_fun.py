num_1=input("Enter First Num ") #5
num_2=input("Enter Second Num ") #5
total=num_1+num_2
print("Total is " + total)
# "5" + "5" = 55   error So,



num_1=int(input("Enter First Num ")) #5     int Fun() converts string into int()
num_2=int(input("Enter Second Num ")) #5
total=num_1+num_2
print("Total is " + str(total))                    #We cannot concatenate string and Int So we have to use str()

#                   We can add int() and float() number but answer will be in float()