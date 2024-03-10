class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

# Combined function
def withdraw_and_handle(account, amount):
    try:
        if account.balance < amount:
            raise ValueError("Insufficient funds")
        account.balance -= amount
        print("Withdrawal successful.")
    except ValueError as e:
        print(f"Error: {e}")

# Create an Account object
account2 = Account(100)

# Test the function
withdraw_and_handle(account2, 50)
withdraw_and_handle(account2, 200)