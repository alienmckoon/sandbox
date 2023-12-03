class BankAccount:
    """
    A class representing a simple bank account.

    Attributes:
    - holder (str): The account holder's name.
    - balance (float): The current account balance.

    Methods:
    - deposit(amount: float): Deposits the specified amount into the account.
    - withdraw(amount: float): Withdraws the specified amount from the account.
    - get_balance(): Returns the current account balance.
    """

    def __init__(self, holder, balance=0.0):
        """
        Initializes a new bank account.

        Args:
        - holder (str): The account holder's name.
        - balance (float, optional): The initial account balance. Defaults to 0.0.
        """
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
        - amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.

        Args:
        - amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
        - float: The current account balance.
        """
        return self.balance


# Example usage of the BankAccount class
# Creating a new account for John with an initial balance of $1000
john_account = BankAccount("John", 1000.0)

# Depositing $500 into John's account
john_account.deposit(500.0)

# Withdrawing $200 from John's account
john_account.withdraw(200.0)

# Getting John's current account balance
john_balance = john_account.get_balance()
print(f"{john_account.holder}'s current balance: ${john_balance}")
