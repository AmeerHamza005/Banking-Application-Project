class InsufficientFundsError(Exception):
    """Custom exception to indicate insufficient funds."""
    pass

class UserAlreadyExistsError(Exception):
    """Custom exception to indicate that a user already exists."""
    pass

class UserNotFoundError(Exception):
    """Custom exception to indicate that a user was not found."""
    pass

class BankAccount:
    accounts: dict[str, 'BankAccount'] = {}  # Dictionary to store user accounts with type annotation

    def __init__(self, username: str, password: str, balance: float = 0):
        self.username = username
        self.password = password
        self.balance = balance

    @classmethod
    def signup(cls, username: str, password: str) -> 'BankAccount':
        if username in cls.accounts:
            raise UserAlreadyExistsError("Username already exists.")
        account = BankAccount(username, password)
        cls.accounts[username] = account
        return account

    @classmethod
    def login(cls, username: str, password: str) -> 'BankAccount':
        if username not in cls.accounts or cls.accounts[username].password != password:
            raise UserNotFoundError("Incorrect username or password.")
        return cls.accounts[username]

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        return self.balance

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        self.balance += amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance
