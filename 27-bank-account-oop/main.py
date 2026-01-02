"""
🏦 PROJECT: Bank Account System - OOP Basics
🎯 OBJECTIVE: Learn Object-Oriented Programming fundamentals through a banking system
📖 DIFFICULTY: Beginner
🔧 CONCEPTS: Classes, Objects, Methods, Attributes, Encapsulation, Magic Methods

This project introduces core OOP concepts by building a simple banking system
where you can create accounts, deposit, withdraw, and manage transactions.
"""

class BankAccount:
    """
    🏦 BankAccount Class
    
    Represents a bank account with basic operations.
    
    LEARNING: Classes and Objects
    - A class is a blueprint for creating objects
    - Objects are instances of a class with their own data
    """
    
    # Class variable (shared by all instances)
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, account_holder, account_number, initial_balance=0):
        """
        🔧 Constructor Method (__init__)
        
        Called automatically when creating a new object.
        Initializes the instance attributes.
        
        LEARNING: Instance Attributes
        - self.attribute_name creates attributes specific to each object
        - self refers to the current instance
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute (name mangling)
        self.transaction_history = []
        
        # Increment class variable
        BankAccount.total_accounts += 1
        
        # Record account creation
        self._add_transaction("Account Created", initial_balance)
    
    def deposit(self, amount):
        """
        💰 Deposit Method
        
        Adds money to the account.
        
        LEARNING: Instance Methods
        - Methods are functions defined inside a class
        - First parameter is always 'self'
        - Can access and modify instance attributes
        """
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self._add_transaction("Deposit", amount)
        print(f"✅ Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        💸 Withdraw Method
        
        Removes money from the account if sufficient balance exists.
        
        LEARNING: Encapsulation and Validation
        - Private attributes (__balance) can only be accessed within the class
        - Methods can validate data before modifying attributes
        """
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! Current balance: ${self.__balance:.2f}")
            return False
        
        self.__balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"✅ Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True
    
    def get_balance(self):
        """
        💵 Balance Getter
        
        Returns the current balance.
        
        LEARNING: Getters (Accessor Methods)
        - Used to access private attributes safely
        - Can add logic/validation before returning value
        """
        return self.__balance
    
    def transfer(self, recipient_account, amount):
        """
        🔄 Transfer Method
        
        Transfers money to another account.
        
        LEARNING: Object Interaction
        - Methods can interact with other objects of the same class
        - Demonstrates encapsulation: uses public methods of other objects
        """
        if amount <= 0:
            print("❌ Transfer amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds for transfer! Current balance: ${self.__balance:.2f}")
            return False
        
        # Withdraw from this account
        self.__balance -= amount
        self._add_transaction(f"Transfer to {recipient_account.account_number}", -amount)
        
        # Deposit to recipient account
        recipient_account.__balance += amount
        recipient_account._add_transaction(f"Transfer from {self.account_number}", amount)
        
        print(f"✅ Transferred ${amount:.2f} to {recipient_account.account_holder}")
        print(f"   Your new balance: ${self.__balance:.2f}")
        return True
    
    def _add_transaction(self, transaction_type, amount):
        """
        📝 Private Helper Method
        
        Adds transaction to history.
        
        LEARNING: Private Methods (Convention)
        - Methods starting with _ are "private" (convention, not enforced)
        - Used internally by the class, not meant for external use
        """
        from datetime import datetime
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'balance': self.__balance,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transaction_history.append(transaction)
    
    def show_transaction_history(self):
        """
        📊 Display Transaction History
        
        Prints all transactions for this account.
        """
        print(f"\n{'='*60}")
        print(f"📜 Transaction History - {self.account_holder}")
        print(f"Account: {self.account_number}")
        print(f"{'='*60}")
        
        if not self.transaction_history:
            print("No transactions yet.")
            return
        
        print(f"{'Date/Time':<20} {'Type':<25} {'Amount':>10} {'Balance':>10}")
        print("-" * 60)
        
        for trans in self.transaction_history:
            amount_str = f"${trans['amount']:+.2f}"
            balance_str = f"${trans['balance']:.2f}"
            print(f"{trans['timestamp']:<20} {trans['type']:<25} {amount_str:>10} {balance_str:>10}")
    
    def __str__(self):
        """
        🎨 String Representation (__str__)
        
        Called by print() and str()
        
        LEARNING: Magic Methods (Dunder Methods)
        - Special methods with double underscores
        - __str__ returns human-readable string representation
        """
        return f"Account({self.account_holder}, {self.account_number}, Balance: ${self.__balance:.2f})"
    
    def __repr__(self):
        """
        🔧 Developer Representation (__repr__)
        
        Called by repr() and in interactive console
        
        LEARNING: __repr__ vs __str__
        - __repr__ should be unambiguous, for developers
        - __str__ is for end users
        """
        return f"BankAccount('{self.account_holder}', '{self.account_number}', {self.__balance})"
    
    @classmethod
    def get_total_accounts(cls):
        """
        📊 Class Method
        
        Returns total number of accounts created.
        
        LEARNING: Class Methods
        - Decorated with @classmethod
        - First parameter is 'cls' (the class itself)
        - Can access class variables but not instance variables
        """
        return cls.total_accounts
    
    @staticmethod
    def is_valid_account_number(account_number):
        """
        ✅ Static Method
        
        Validates account number format.
        
        LEARNING: Static Methods
        - Decorated with @staticmethod
        - Doesn't receive self or cls
        - Like a regular function but belongs to the class namespace
        """
        return isinstance(account_number, str) and len(account_number) >= 5


def main():
    """Main function demonstrating OOP concepts"""
    
    print("=" * 60)
    print("🏦 BANK ACCOUNT SYSTEM - OOP BASICS")
    print("=" * 60)
    
    # Creating Objects (Instances)
    print("\n📝 Creating Bank Accounts...")
    account1 = BankAccount("Alice Johnson", "ACC001", 1000)
    account2 = BankAccount("Bob Smith", "ACC002", 500)
    account3 = BankAccount("Charlie Brown", "ACC003")
    
    print(f"\n✅ Created {BankAccount.get_total_accounts()} accounts")
    print(f"   Bank Name: {BankAccount.bank_name}")
    
    # Demonstrating __str__ method
    print(f"\n📋 Account Details:")
    print(f"   {account1}")
    print(f"   {account2}")
    print(f"   {account3}")
    
    # Deposit operations
    print(f"\n{'='*60}")
    print("💰 DEPOSIT OPERATIONS")
    print(f"{'='*60}")
    account1.deposit(500)
    account2.deposit(200)
    account3.deposit(1000)
    
    # Withdrawal operations
    print(f"\n{'='*60}")
    print("💸 WITHDRAWAL OPERATIONS")
    print(f"{'='*60}")
    account1.withdraw(300)
    account2.withdraw(1000)  # This should fail (insufficient funds)
    account3.withdraw(250)
    
    # Transfer operations
    print(f"\n{'='*60}")
    print("🔄 TRANSFER OPERATIONS")
    print(f"{'='*60}")
    account1.transfer(account2, 200)
    
    # Check balances
    print(f"\n{'='*60}")
    print("💵 CURRENT BALANCES")
    print(f"{'='*60}")
    print(f"   {account1.account_holder}: ${account1.get_balance():.2f}")
    print(f"   {account2.account_holder}: ${account2.get_balance():.2f}")
    print(f"   {account3.account_holder}: ${account3.get_balance():.2f}")
    
    # Show transaction history
    account1.show_transaction_history()
    
    # Interactive menu
    print(f"\n{'='*60}")
    print("🎮 INTERACTIVE MODE")
    print(f"{'='*60}")
    
    current_account = account1
    
    while True:
        print(f"\n--- Current Account: {current_account.account_holder} ---")
        print(f"Balance: ${current_account.get_balance():.2f}")
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. View Transaction History")
        print("5. Switch Account")
        print("6. Account Info")
        print("7. Exit")
        
        choice = input("\n👉 Enter your choice (1-7): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: $"))
                current_account.deposit(amount)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                current_account.withdraw(amount)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == '3':
            print("\nAvailable accounts for transfer:")
            accounts = [account1, account2, account3]
            for i, acc in enumerate(accounts, 1):
                if acc != current_account:
                    print(f"{i}. {acc.account_holder} ({acc.account_number})")
            
            try:
                choice_idx = int(input("Select recipient account: ")) - 1
                if 0 <= choice_idx < len(accounts) and accounts[choice_idx] != current_account:
                    amount = float(input("Enter transfer amount: $"))
                    current_account.transfer(accounts[choice_idx], amount)
                else:
                    print("❌ Invalid account selection!")
            except (ValueError, IndexError):
                print("❌ Invalid input!")
        
        elif choice == '4':
            current_account.show_transaction_history()
        
        elif choice == '5':
            print("\nSwitch to account:")
            print("1. Alice Johnson")
            print("2. Bob Smith")
            print("3. Charlie Brown")
            acc_choice = input("Select account (1-3): ").strip()
            if acc_choice == '1':
                current_account = account1
            elif acc_choice == '2':
                current_account = account2
            elif acc_choice == '3':
                current_account = account3
            else:
                print("❌ Invalid choice!")
        
        elif choice == '6':
            print(f"\n📋 Account Information:")
            print(f"   Account Holder: {current_account.account_holder}")
            print(f"   Account Number: {current_account.account_number}")
            print(f"   Current Balance: ${current_account.get_balance():.2f}")
            print(f"   Total Transactions: {len(current_account.transaction_history)}")
            print(f"   Bank: {BankAccount.bank_name}")
        
        elif choice == '7':
            print("\n👋 Thank you for using Python Bank!")
            print(f"📊 Total Accounts: {BankAccount.get_total_accounts()}")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\n⏸️  Press Enter to continue...")


if __name__ == "__main__":
    main()

