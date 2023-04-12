# while loop
# sum using while loop
# sum=0
# i=1
# while i<=10:
#     sum=sum+i
#     i=i+1

# print(f"The sum of first 10 numbers is : {sum}")

# Single statement while block
# count=0
# while (count == 0): print("Hello Geek")\

#For loop with range function 
# total=0
# current=0
# previous=0
# for current in range(1,11):
#     previous+=current-1
#     total=previous+current
#     print(f"{previous}+{current}= {total}")
# print(total)

# Iterating by index
# colors=['Red','Green','Yellow']
# for index in range(len(colors)):
#     print(index)

# for letter in "AnasJamal":
#     if letter=='a' or letter=='s':
#         continue
#     print(f"Current Letter is :{letter}")

# Functions
# def greatest(n1,n2):
#     if n1==n2:
#         return f"Both numbers are equal."
#     elif n1>n2:
#         return f"{n1} is greater than {n2}."
#     else:
#         return f"{n2} is grater than {n1}."


# x=int(input("Enter First number :"))
# y=int(input("Enter Second number :"))

# print(greatest(x,y))


# def myfun(x):
#     return 2*x

# a=int(input("Enter a Number :"))
# print(myfun(a))

# Classes
# class Myclass:
#     x=5

# p1=Myclass
# print(p1.x)

str_x="My name is Anas Jamal.My father name is Jamal Din."
cnt=str_x.count("name")
print(f"{cnt}")