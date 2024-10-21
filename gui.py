import tkinter as tk
from tkinter import messagebox
from banking import BankAccount, InsufficientFundsError

# Create a new instance of a bank account
account = BankAccount(500)  # Initial balance of 500

# Function to handle withdrawals
def handle_withdraw():
    try:
        amount = float(entry_amount.get())
        account.withdraw(amount)
        lbl_balance.config(text=f"Balance: {account.get_balance()}")
        messagebox.showinfo("Success", f"Withdrew {amount} successfully!")
    except InsufficientFundsError as e:
        messagebox.showerror("Error", str(e))
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered")

# Function to handle deposits
def handle_deposit():
    try:
        amount = float(entry_amount.get())
        account.deposit(amount)
        lbl_balance.config(text=f"Balance: {account.get_balance()}")
        messagebox.showinfo("Success", f"Deposited {amount} successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered")

# Function to display current balance
def check_balance():
    lbl_balance.config(text=f"Balance: {account.get_balance()}")

# Ensure to set up the GUI and the buttons
root = tk.Tk()
root.title("Banking Application")

# UI elements (Assuming this is defined)
lbl_title = tk.Label(root, text="Welcome to Your Bank Account", font=("Arial", 16))
lbl_title.pack(pady=10)

lbl_amount = tk.Label(root, text="Enter Amount:")
lbl_amount.pack(pady=5)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

btn_withdraw = tk.Button(root, text="Withdraw", command=handle_withdraw)
btn_withdraw.pack(pady=5)

btn_deposit = tk.Button(root, text="Deposit", command=handle_deposit)
btn_deposit.pack(pady=5)

btn_check_balance = tk.Button(root, text="Check Balance", command=check_balance)
btn_check_balance.pack(pady=5)

lbl_balance = tk.Label(root, text=f"Balance: {account.get_balance()}", font=("Arial", 14))
lbl_balance.pack(pady=20)

# Start the GUI loop
root.mainloop()