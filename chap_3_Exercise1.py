# Number guessing Game 

winning_number=55
guessed_number=int(input("Enter Guessed Number b/w 1 and 100:"))
if winning_number==guessed_number:
    print("YOU WIN !!!")
elif guessed_number<winning_number:
    print("too low")
else:
    print("too high")