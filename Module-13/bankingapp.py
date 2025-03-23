class BankingApp:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount
        self.transaction_log(f"Deposit - ${amount}")

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_log(f"Withdrawal - ${amount}")
        else:
            print("Insufficient funds!")

    def transaction_log(self, transaction):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction} \t\t Balance - ${self.balance}\n")

    def print_balance(self):
        print(f"Your balance is ${self.balance}")


account = BankingApp()

while True:
    try:
        user = input("What would you like to do? (deposit / withdrawal / balance) ")
    except KeyboardInterrupt:
        print("\nExiting...\n")
        break

    if user == 'deposit':
        amount = float(input("How much would you like to deposit? $"))
        account.deposit(amount)
    elif user == 'withdrawal':
        amount = float(input("How much would you like to withdraw? $"))
        account.withdrawal(amount)
    elif user == 'balance':
        account.print_balance()
    else:
        print("Invaild action! Try again.")
