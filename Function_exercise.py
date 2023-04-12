# A function which takes two input and tells us that which number is greater.

def greater(num1,num2):
    if num1==num2:
        return "Both numbers are equal."
    elif num1>num2:
        return f"{num1} is Greater than {num2}"
    else:
        return f"{num2} is Greater than {num1}"

x=int(input("Enter first number :"))
y=int(input("Enter first number :"))
print(greater(x,y))