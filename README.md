# Insufficient Funds Example

This project demonstrates how to define and handle a custom Python exception
when a withdrawal request is larger than the available account balance.

## How the code works

The example is in [`error.py`](./error.py).

1. `InsufficientFundsError` subclasses Python's built-in `Exception` class.
2. Its constructor stores the available `balance` and requested `amount`.
3. The constructor builds a useful error message, such as:
   `Insufficient funds: $100 available, $150 requested.`
4. `withdraw(balance, amount)` compares the requested amount with the balance.
5. If the request is too large, the function raises `InsufficientFundsError`
   before changing the balance.
6. Otherwise, it returns the remaining balance.
7. The `try`/`except` block catches the expected exception and prints a
   user-friendly failure message.

## Run the example

From the project directory, run:

```powershell
python error.py
```

Expected output:

```text
Transaction failed: Insufficient funds: $100 available, $150 requested.
```

## Successful withdrawal

The function returns the new balance when enough funds are available:

```python
from error import withdraw

new_balance = withdraw(100, 40)
print(new_balance)  # 60
```

## Failed withdrawal

An unsuccessful withdrawal raises the custom exception, which can be handled
explicitly:

```python
from error import InsufficientFundsError, withdraw

try:
    withdraw(100, 150)
except InsufficientFundsError as error:
    print(error)
```
