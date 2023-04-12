

winning_num=43
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
            guess+=1
            guessed_num=int(input("Guess Again"))
        else:
            print("too High")
            guess+=1
            guessed_num=int(input("Guess Again"))


# import random
# winning_num=random.randint(1,100)





# # Number guessing Game 

# winning_number=55
# guessed_number=int(input("Enter Guessed Number b/w 1 and 100:"))
# if winning_number==guessed_number:
#     print("YOU WIN !!!")
# elif guessed_number<winning_number:
#     print("too low")
# else:
#     print("too high")