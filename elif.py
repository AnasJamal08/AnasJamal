# Ticketing Price

age=int(input("Enter your age :"))
if age ==0 or age < 0:
    print("You can't watch movie")
elif 1<age<=3:
    print("Ticket Price : Free")
elif 4<age<=10:
    print("Ticket Price : 150")
elif 11<age<=60:
    print("Ticket Price : 250")
elif age>60:
    print("Ticket Price : 200")
else:
    print("Ticket Price : 200")
