class Atm:
    # Constructor
    def __init__(self):   #magic method
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input("""
        What You want to do?
        1.Create Pin.
        2.Deposit money
        3.Withdraw money
        4.Check Balance
        5.Exit
        """)
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
            print("Good Bye.")
    def create_pin(self):
        self.pin=input("Enter Pin.")
        print("Pin Created Successfully.")
    def deposit(self):
        temp=input("Enter you pin.")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Amount Deposit Successfully.")
        else:
            print("Invalid Pin.")
    def withdraw(self):
        temp=input("Enter you pin.")
        if temp==self.pin:
            amount=int(input("Enter the amount."))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("Amount Withdrawn Successfully.")
            elif amount>self.balance:
                print("Insufficiet Amount.")
        else:
            print("Invalin Pin.")
    def check_balance(self):
        temp=input("Enter you pin.")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin.")
        



s=Atm()
s.create_pin()
s.deposit()
s.withdraw()
s.check_balance()
