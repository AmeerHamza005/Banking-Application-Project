import random
import smtplib  # For sending email (optional)
from typing import Optional


class InsufficientFundsError(Exception):
    """Custom exception to indicate insufficient funds."""
    pass


class UserAlreadyExistsError(Exception):
    """Custom exception to indicate that a user already exists."""
    pass


class UserNotFoundError(Exception):
    """Custom exception to indicate that a user was not found."""
    pass


class InvalidOTPError(Exception):
    """Custom exception to indicate invalid OTP."""
    pass


class BankAccount:
    accounts: dict[str, 'BankAccount'] = {}  # Dictionary to store user accounts

    def __init__(self, username: str, password: str, phone: str, email: str, balance: float = 0):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.balance = balance
        self.otp: Optional[str] = None  # Store OTP here

    @classmethod
    def signup(cls, username: str, password: str, phone: str, email: str) -> 'BankAccount':
        if username in cls.accounts:
            raise UserAlreadyExistsError("Username already exists.")
        account = BankAccount(username, password, phone, email)
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

    def send_otp(self):
        """Generate and send OTP to user's phone or email."""
        self.otp = str(random.randint(100000, 999999))
        # For testing purposes, we'll print the OTP (normally, you'd send it)
        print(f"OTP sent to {self.phone} or {self.email}: {self.otp}")

    def verify_otp(self, entered_otp: str):
        """Verify the entered OTP."""
        if self.otp == entered_otp:
            print("OTP verified successfully.")
            self.otp = None  # Clear OTP after successful verification
        else:
            raise InvalidOTPError("Invalid OTP entered.")
