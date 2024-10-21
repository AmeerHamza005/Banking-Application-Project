class InsufficientFundsError(Exception):
    """Custom exception to indicate insufficient funds."""
    pass
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        self.balance += amount
        return self.balance
    def get_balance(self):
        return self.balance
