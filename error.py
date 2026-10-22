class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a transaction."""
    def __init__(self,balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: ${balance} available, ${amount} requested.")

def withdraw(balance, amount):
    """Withdraws the specified amount from the account balance."""
    if amount > balance:
        # Stop the transaction before it can create a negative balance.
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")