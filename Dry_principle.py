# Dry Principle
# it tells us that don't use repetition of code
import random
winning_num=random.randint(1,100)
guess=1
guessed_num=int(input("Enter a number b/w 1 and 100 :"))
game_over =False
while not game_over:
    if guessed_num==winning_num:
        print(f"You WIN!! and you guessed this number in {guess} times.")
        game_over=True
    else:
        if guessed_num<winning_num:
            print("too low")
        else:
            print("too High")

        guess+=1                             # here is the dry Principle
        guessed_num=int(input("Guess Again :"))





# winning_num=43
# guess=1
# guessed_num=int(input("Enter a number b/w 1 and 100 :"))
# while True:
#     if guessed_num==winning_num:
#         print(f"You WIN!! and you guessed this number in {guess} times.")
#         break
#     else:
#         if guessed_num<winning_num:
#             print("too low")
#         else:
#             print("too High")

#         guess+=1                             # here is the dry Principle
#         guessed_num=int(input("Guess Again :"))        