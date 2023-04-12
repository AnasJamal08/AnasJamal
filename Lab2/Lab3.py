# Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included)

# n=[]
# for i in range(1495,2705):
#     if (i%5)==0 and (i%7)==0:
#         n.append(str(i))
# print(','.join(n))

# Write a Python program to guess a number between 1 to 9.

n=int(input("Enter a guess : "))
for i in range(1,):
    if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
        print("Well Guessed.")
    else:
        print("Wrong Guess.Enter Again.")
        n=int(input("Enter a guess : "))

