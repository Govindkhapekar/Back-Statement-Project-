class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


print("Welcome to National Bank Of India")
name = input("Enter your name: ")
account = BankAccount(name)

while True:
    print("\nSelect an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.display_balance()

    elif choice == '4':
        print("Thank you for using National Bank Of India!")
        break

    else:
        print("Invalid choice. Please try again.")
