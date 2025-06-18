class CurrentAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.overdraft_limit = -100000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₦{amount:.2f}. New Balance: ₦{self.balance:.2f}"
        return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than 0."
        if self.balance - amount < self.overdraft_limit:
            return f"Insufficient funds. Overdraft limit of ₦{abs(self.overdraft_limit):.2f} exceeded."
        self.balance -= amount
        return f"Withdrew ₦{amount:.2f}. New Balance: ₦{self.balance:.2f}"
