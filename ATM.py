class ATM:
    def __init__(self, starting_balance=100, pin=6969):
        self.balance = starting_balance
        self.pin = pin

    def login(self):
        entered_pin = int(input("Enter your ATM PIN: "))
        if entered_pin == self.pin:
            print("Login successful!\n")
            return True
        else:
            print("Incorrect PIN. Try again!")
            return False

    def menu(self):
        while True:
            print("     ATM MENU ")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            option = input("Select an option (1-5): ")
            if option == "1":
                self.check_balance()
            elif option == "2":
                self.deposit_money()
            elif option == "3":
                self.withdraw_money()
            elif option == "4":
                self.update_pin()
            elif option == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please select from 1-5.")

    def check_balance(self):
        print(f"Your current balance is: Rs.{self.balance}")

    def deposit_money(self):
        deposit = float(input("Enter amount to deposit: "))
        if deposit > 0:
            self.balance += deposit
            print(f"Rs.{deposit} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw_money(self):
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= 0:
            print("Enter a valid withdrawal amount.")
        elif withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Rs.{withdraw} withdrawn successfully.")
        else:
            print("Insufficient balance. Try smaller amount.")

    def update_pin(self):
        new_pin = int(input("Enter new 4-digit PIN: "))
        self.pin = new_pin
        print("PIN updated successfully.")

atm = ATM() 
if atm.login():
    atm.menu() 
