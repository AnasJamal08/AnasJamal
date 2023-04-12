def greatest(a,b,c):
    if a>b  and a>c:
        return f"{a} is the greatest number."
    elif b>a  and b>c:
        return f"{b} is the greatest number."
    elif c>a and c>b:
        return f"{c} is the greatest number."
    else:
        return "All numbers are equal."



num1=int(input("Enter a number :"))
num2=int(input("Enter a number :"))
num3=int(input("Enter a number :"))
print(greatest(num1,num2,num3))