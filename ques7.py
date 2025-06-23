class BankAccount:
    # Constructor to initialize account number and balance
    def __init__(self,accountno, balance):
        self.accountno = accountno
        self.balance = balance
        
    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
        
    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
    
    # Method to show the current balance
    def show_balance(self):
        return f"Your current balance is {self.balance}"
        
import csv

# List to store all BankAccount objects
accounts =[]

# Read account data from CSV file and create BankAccount objects
with open("accounts.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # Each row contains account number and balance
        accounts.append(BankAccount(int(row[0]), float(row[1])))

# Function to update the CSV file with current account balances
def update_balance(accounts, filename= "accounts.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for acc in accounts:
            writer.writerow([acc.accountno, acc.balance])

# Ask user for their account number
search_acc = int(input("Enter Your account number:"))
current_user = None

# Find the account matching the entered account number
for acc in accounts:
    if acc.accountno == search_acc:
        current_user = acc
        break

if current_user:
    print("\nAccount Found!")

    # Main loop for user actions
    while True:
        print("\nWhat would you like to do with your account")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice  = input("Enter your choice (1-4): ")

        if choice == "1":
            # Show current balance
            print(current_user.show_balance())
        elif choice == "2":
            # Deposit money and update CSV
            amt = float(input("Enter the amount you want to deposit: "))
            print(current_user.deposit(amt))
            update_balance(accounts)
        elif choice == "3":
            # Withdraw money and update CSV
            amt = float(input("Enter the amount you want to withdraw: "))
            print(current_user.withdraw(amt))
            update_balance(accounts)
        elif choice == "4":
            # Exit the loop
            print("Thank you! Exiting.")
            break
        else:
            print("Invalid choice! Try Again")

else:
    # If account not found, show message
    print("Account Not Found")