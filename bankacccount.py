class BankAccount:
    # now here its like we are setting a fixed variable 
    interest_rate = 0.05

    def __init__(self, account_holder):
        self.account_holder = account_holder  # here what we are trying to say is that self.account _holder = the real holder that i will name
        self.balance = 0  # this is the state of our balance
    def deposit(self, amount):
        """Adds the amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:-
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts the amount from the balance if sufficient funds exist."""
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def apply_interest(self):
        """Adds interest to the current balance based on the interest rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")

    def display_account_info(self):
        """Displays the account holder's name and the current balance."""
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

# Creating two instances of BankAccount
account1 = BankAccount("robert")
account2 = BankAccount("")

# Performing deposits and withdrawals
account1.deposit(100)
account1.withdraw(30)
account2.deposit(200)
account2.withdraw(100)

# Applying interest
account1.apply_interest()
account2.apply_interest()

# Displaying account information
account1.display_account_info()
account2.display_account_info()
