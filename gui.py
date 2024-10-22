import tkinter as tk
from tkinter import messagebox
from banking import BankAccount, InsufficientFundsError, UserAlreadyExistsError, UserNotFoundError

current_user = None  # To store the logged-in user

# Function to handle login
def handle_login():
    global current_user
    username = entry_username.get()
    password = entry_password.get()

    try:
        current_user = BankAccount.login(username, password)
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        load_banking_interface()
    except UserNotFoundError as e:
        messagebox.showerror("Error", str(e))

# Function to handle signup
def handle_signup():
    global current_user
    username = entry_username.get()
    password = entry_password.get()
    phone = entry_phone.get()  # Get phone number from the input field 
    email = entry_email.get()  # Get email from the input field

    try:
        current_user = BankAccount.signup(username, password, phone, email)  # Pass all required arguments
        messagebox.showinfo("Signup Success", f"Account created for {username}!")
        load_banking_interface()
    except UserAlreadyExistsError as e:
        messagebox.showerror("Error", str(e))

# Function to load the banking interface
def load_banking_interface():
    for widget in root.winfo_children():
        widget.destroy()

    lbl_balance = tk.Label(root, text=f"Balance: {current_user.get_balance()}", font=("Arial", 14))
    lbl_balance.pack(pady=20)

    lbl_amount = tk.Label(root, text="Enter Amount:")
    lbl_amount.pack(pady=5)

    entry_amount = tk.Entry(root)
    entry_amount.pack(pady=5)

    def handle_withdraw():
        try:
            amount = float(entry_amount.get())
            current_user.withdraw(amount)
            lbl_balance.config(text=f"Balance: {current_user.get_balance()}")
            messagebox.showinfo("Success", f"Withdrew {amount} successfully!")
        except InsufficientFundsError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered")

    def handle_deposit():
        try:
            amount = float(entry_amount.get())
            current_user.deposit(amount)
            lbl_balance.config(text=f"Balance: {current_user.get_balance()}")
            messagebox.showinfo("Success", f"Deposited {amount} successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered")

    btn_withdraw = tk.Button(root, text="Withdraw", command=handle_withdraw)
    btn_withdraw.pack(pady=5)

    btn_deposit = tk.Button(root, text="Deposit", command=handle_deposit)
    btn_deposit.pack(pady=5)

    btn_logout = tk.Button(root, text="Logout", command=load_login_signup_interface)
    btn_logout.pack(pady=5)

# Function to load login/signup interface
def load_login_signup_interface():
    for widget in root.winfo_children():
        widget.destroy()

    lbl_title = tk.Label(root, text="Banking App Signup", font=("Arial", 16))
    lbl_title.pack(pady=10)

    lbl_username = tk.Label(root, text="Username:")
    lbl_username.pack(pady=5)

    global entry_username
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    lbl_password = tk.Label(root, text="Password:")
    lbl_password.pack(pady=5)

    global entry_password
    entry_password = tk.Entry(root, show='*')
    entry_password.pack(pady=5)

    lbl_phone = tk.Label(root, text="Phone Number:")
    lbl_phone.pack(pady=5)

    global entry_phone
    entry_phone = tk.Entry(root)
    entry_phone.pack(pady=5)

    lbl_email = tk.Label(root, text="Email:")
    lbl_email.pack(pady=5)

    global entry_email
    entry_email = tk.Entry(root)
    entry_email.pack(pady=5)

    btn_signup = tk.Button(root, text="Signup", command=handle_signup)  # Call handle_signup when clicked
    btn_signup.pack(pady=5)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Banking Application")

# Load the login/signup interface at the start
load_login_signup_interface()

# Start the GUI loop
root.mainloop()
