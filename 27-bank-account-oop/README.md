# 🏦 Bank Account System - Complete OOP Guide

A comprehensive, hands-on introduction to Object-Oriented Programming through a practical banking system. Learn OOP concepts by building real-world functionality!

## 🎯 Project Overview

This project teaches Object-Oriented Programming (OOP) from the ground up by building a fully functional bank account system. You'll learn how to design classes, create objects, implement methods, and understand core OOP principles through practical application.

## 📚 Complete OOP Concepts Covered

### 1. 🏗️ Classes and Objects - The Foundation

**What is a Class?**
A class is a **blueprint** or **template** for creating objects. Think of it like a cookie cutter.

**What is an Object?**
An object is an **instance** of a class. Think of it like the actual cookie.

**Visual Representation**:
```
Class: BankAccount (Blueprint)
│
├─ Attributes: account_holder, account_number, balance
├─ Methods: deposit(), withdraw(), transfer()
│
└─ Objects (Instances):
    ├─ alice_account = BankAccount("Alice", "ACC001", 1000)
    ├─ bob_account = BankAccount("Bob", "ACC002", 500)
    └─ charlie_account = BankAccount("Charlie", "ACC003", 0)

Each object has its own data!
```

**Code Example**:
```python
# Define the Class (Blueprint)
class BankAccount:
    def __init__(self, holder, number, balance):
        self.account_holder = holder
        self.account_number = number
        self.balance = balance

# Create Objects (Instances)
alice = BankAccount("Alice", "ACC001", 1000)
bob = BankAccount("Bob", "ACC002", 500)

# Each object has its own data
print(alice.balance)  # 1000
print(bob.balance)    # 500

# Modifying one doesn't affect the other
alice.balance += 100
print(alice.balance)  # 1100
print(bob.balance)    # 500 (unchanged)
```

---

### 2. 🔧 Constructor (`__init__`) - Initializing Objects

**What is `__init__`?**
The constructor is a **special method** called automatically when creating an object.

**Visual Flow**:
```
1. alice = BankAccount("Alice", "ACC001", 1000)
           ↓
2. Python creates empty object
           ↓
3. __init__() is called automatically
           ↓
4. Attributes are set:
   alice.account_holder = "Alice"
   alice.account_number = "ACC001"
   alice.balance = 1000
           ↓
5. Object is ready to use!
```

**Understanding `self`**:
```python
class BankAccount:
    def __init__(self, holder, number, balance):
        # self = the current object being created
        self.account_holder = holder  # Store in THIS object
        self.account_number = number  # Store in THIS object
        self.balance = balance        # Store in THIS object

# When creating alice
alice = BankAccount("Alice", "ACC001", 1000)
# Python internally does: alice.__init__(alice, "Alice", "ACC001", 1000)
#                                        ↑
#                              self points to alice

# When creating bob
bob = BankAccount("Bob", "ACC002", 500)
# Python internally does: bob.__init__(bob, "Bob", "ACC002", 500)
#                                      ↑
#                            self points to bob
```

---

### 3. 🎯 Instance Attributes - Object-Specific Data

**What are Instance Attributes?**
Variables that belong to a specific object. Each object has its own copy.

**Visualization**:
```
┌─────────────────────────┐      ┌─────────────────────────┐
│   alice (Object 1)      │      │   bob (Object 2)        │
├─────────────────────────┤      ├─────────────────────────┤
│ account_holder: "Alice" │      │ account_holder: "Bob"   │
│ account_number: "ACC001"│      │ account_number: "ACC002"│
│ balance: 1000           │      │ balance: 500            │
└─────────────────────────┘      └─────────────────────────┘

Independent Data - Changes to alice don't affect bob!
```

**Code Example**:
```python
class BankAccount:
    def __init__(self, holder, balance):
        self.account_holder = holder  # Instance attribute
        self.balance = balance        # Instance attribute

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

# Each has their own data
print(alice.account_holder)  # "Alice"
print(bob.account_holder)    # "Bob"

# Modifying one doesn't affect the other
alice.balance = 2000
print(alice.balance)  # 2000
print(bob.balance)    # 500 (unchanged!)
```

---

### 4. 🔒 Encapsulation - Data Hiding and Protection

**What is Encapsulation?**
Hiding internal data and providing controlled access through methods.

**Why Encapsulation?**
- Prevents invalid data
- Controls how data is modified
- Hides implementation details

**Visual Comparison**:
```
❌ Without Encapsulation:
┌─────────────────────┐
│  BankAccount        │
│  ┌────────────────┐ │
│  │ balance = 1000 │ │  ← Anyone can access directly!
│  └────────────────┘ │
└─────────────────────┘

account.balance = -5000  # ❌ No validation!


✅ With Encapsulation:
┌─────────────────────┐
│  BankAccount        │
│  ┌────────────────┐ │
│  │ __balance      │ │  ← Private (hidden)
│  └────────────────┘ │
│         ↕             │
│  ┌────────────────┐ │
│  │ deposit()      │ │  ← Controlled access
│  │ withdraw()     │ │  ← With validation
│  │ get_balance()  │ │  ← Safe retrieval
│  └────────────────┘ │
└─────────────────────┘
```

**Implementation**:
```python
class BankAccount:
    def __init__(self, holder, balance):
        self.account_holder = holder
        self.__balance = balance  # Private (name mangling with __)
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive!")
            return False
        self.__balance += amount  # Controlled modification
        return True
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
            return False
        self.__balance -= amount  # Controlled modification
        return True
    
    def get_balance(self):
        return self.__balance  # Safe read-only access

# Usage
account = BankAccount("Alice", 1000)

# Can't access directly
# print(account.__balance)  # ❌ AttributeError!

# Must use methods
account.deposit(500)        # ✅ Validated!
account.withdraw(200)       # ✅ Validated!
print(account.get_balance())  # ✅ Safe access!
```

**Benefits**:
1. **Validation**: Can't deposit negative amounts
2. **Safety**: Can't withdraw more than balance
3. **Control**: Can add logging, security checks
4. **Flexibility**: Can change internal implementation

---

### 5. 📝 Instance Methods - Object Behavior

**What are Instance Methods?**
Functions that belong to a class and operate on object data.

**Method Structure**:
```python
class BankAccount:
    def method_name(self, parameter1, parameter2):
        # self = current object
        # Can access: self.attribute_name
        # Can call:   self.other_method()
        pass
```

**Visual Flow of Method Call**:
```
1. alice.deposit(500)
         ↓
2. Python finds deposit() method in BankAccount class
         ↓
3. Python calls: BankAccount.deposit(alice, 500)
                                      ↑     ↑
                                    self  amount
         ↓
4. Method executes:
   self.__balance += amount
   alice.__balance += 500
         ↓
5. Returns result
```

**Complete Example**:
```python
class BankAccount:
    def __init__(self, holder, balance):
        self.account_holder = holder
        self.__balance = balance
    
    def deposit(self, amount):
        """Instance method - operates on THIS object"""
        if amount <= 0:
            return False
        self.__balance += amount  # Modifies THIS object
        print(f"Deposited ${amount}. New balance: ${self.__balance}")
        return True
    
    def withdraw(self, amount):
        """Instance method - validates and modifies THIS object"""
        if amount > self.__balance:
            print(f"❌ Insufficient funds! Balance: ${self.__balance}")
            return False
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        return True
    
    def get_balance(self):
        """Instance method - returns data from THIS object"""
        return self.__balance

# Usage
alice = BankAccount("Alice", 1000)
alice.deposit(500)   # Works on alice's balance
alice.withdraw(200)  # Works on alice's balance

bob = BankAccount("Bob", 300)
bob.deposit(100)     # Works on bob's balance (independent!)
```

---

### 6. ✨ Magic Methods (Dunder Methods) - Special Behavior

**What are Magic Methods?**
Special methods with double underscores that give objects special behaviors.

**Common Magic Methods**:

#### `__str__()` - String Representation for Users
```python
class BankAccount:
    def __str__(self):
        return f"Account({self.account_holder}, ${self.balance})"

account = BankAccount("Alice", 1000)
print(account)  # Output: Account(Alice, $1000)
# Without __str__: <__main__.BankAccount object at 0x...>
```

#### `__repr__()` - Developer Representation
```python
class BankAccount:
    def __repr__(self):
        return f"BankAccount('{self.account_holder}', {self.balance})"

account = BankAccount("Alice", 1000)
repr(account)  # Output: BankAccount('Alice', 1000)
# Can copy-paste this to recreate object!
```

#### More Magic Methods
```python
class BankAccount:
    def __len__(self):
        """Length of transaction history"""
        return len(self.transaction_history)
    
    def __eq__(self, other):
        """Check if two accounts are equal"""
        return self.account_number == other.account_number
    
    def __lt__(self, other):
        """Compare by balance (for sorting)"""
        return self.balance < other.balance
    
    def __add__(self, other):
        """Combine two accounts"""
        total = self.balance + other.balance
        return BankAccount("Joint", "JOINT", total)

# Usage
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

len(account1)  # Calls __len__()
account1 == account2  # Calls __eq__()
account1 < account2   # Calls __lt__()
joint = account1 + account2  # Calls __add__()
```

---

### 7. 🌐 Class Variables & Methods - Shared Data

**Class Variables vs Instance Variables**:

```python
class BankAccount:
    # Class variable (shared by ALL instances)
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, holder, balance):
        # Instance variables (unique to each object)
        self.account_holder = holder
        self.balance = balance
        
        # Modify class variable
        BankAccount.total_accounts += 1

# All instances share class variables
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

print(alice.bank_name)   # "Python Bank"
print(bob.bank_name)     # "Python Bank" (same!)
print(BankAccount.total_accounts)  # 2

# Change class variable affects all
BankAccount.bank_name = "Global Bank"
print(alice.bank_name)   # "Global Bank"
print(bob.bank_name)     # "Global Bank"
```

**Visual Representation**:
```
┌─────────────────────────────────────┐
│     BankAccount (Class)             │
│  ┌────────────────────────────────┐ │
│  │ bank_name = "Python Bank"      │ │  ← Shared
│  │ total_accounts = 2             │ │  ← Shared
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘
         ↓                  ↓
    ┌─────────┐        ┌─────────┐
    │  alice  │        │   bob   │
    ├─────────┤        ├─────────┤
    │ holder  │        │ holder  │  ← Individual
    │ balance │        │ balance │  ← Individual
    └─────────┘        └─────────┘
```

**Class Methods**:
```python
class BankAccount:
    total_accounts = 0
    
    @classmethod
    def get_total_accounts(cls):
        """Can access class variables, not instance variables"""
        return cls.total_accounts
    
    @classmethod
    def from_dict(cls, data):
        """Alternative constructor"""
        return cls(data['holder'], data['balance'])

# Usage
print(BankAccount.get_total_accounts())  # Call on class

# Alternative constructor
data = {'holder': 'Alice', 'balance': 1000}
account = BankAccount.from_dict(data)
```

**Static Methods**:
```python
class BankAccount:
    @staticmethod
    def is_valid_account_number(number):
        """Utility function - doesn't need self or cls"""
        return isinstance(number, str) and len(number) >= 5

# Usage
if BankAccount.is_valid_account_number("ACC001"):
    print("Valid!")
```

---

### 8. 🔗 Object Interaction - Objects Working Together

**Visual Representation**:
```
Transfer: alice → bob  ($200)

Before:
┌─────────────┐          ┌─────────────┐
│   alice     │          │    bob      │
│ balance:    │          │ balance:    │
│   $1000     │          │   $500      │
└─────────────┘          └─────────────┘

Transfer Flow:
┌─────────────┐   $200   ┌─────────────┐
│   alice     │  -----→  │    bob      │
│ -$200       │          │ +$200       │
└─────────────┘          └─────────────┘

After:
┌─────────────┐          ┌─────────────┐
│   alice     │          │    bob      │
│ balance:    │          │ balance:    │
│   $800      │          │   $700      │
└─────────────┘          └─────────────┘
```

**Implementation**:
```python
class BankAccount:
    def transfer(self, recipient_account, amount):
        """Transfer money to another account object"""
        # Validate
        if amount > self.__balance:
            print("❌ Insufficient funds!")
            return False
        
        # Withdraw from this account
        self.__balance -= amount
        
        # Deposit to recipient account
        recipient_account.__balance += amount
        
        print(f"✅ Transferred ${amount} to {recipient_account.account_holder}")
        return True

# Usage - Objects interacting!
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

alice.transfer(bob, 200)  # Alice's method operates on Bob's object!
```

---

## 🎯 Complete Example with All Concepts

```python
class BankAccount:
    """Complete OOP example with all concepts"""
    
    # 1. Class Variables
    bank_name = "Python Bank"
    total_accounts = 0
    interest_rate = 0.02
    
    def __init__(self, holder, number, balance=0):
        """2. Constructor - Initialize object"""
        # 3. Instance Attributes
        self.account_holder = holder
        self.account_number = number
        self.__balance = balance  # 4. Encapsulation (private)
        self.transaction_history = []
        
        BankAccount.total_accounts += 1
        self._record_transaction("Account Created", balance)
    
    # 5. Instance Methods
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            return False
        self.__balance += amount
        self._record_transaction("Deposit", amount)
        return True
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > self.__balance:
            return False
        self.__balance -= amount
        self._record_transaction("Withdrawal", -amount)
        return True
    
    def get_balance(self):
        """Getter method for private balance"""
        return self.__balance
    
    # 8. Object Interaction
    def transfer(self, recipient, amount):
        """Transfer to another account object"""
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True
        return False
    
    # Private Helper Method
    def _record_transaction(self, type, amount):
        """Private method (convention: starts with _)"""
        self.transaction_history.append({
            'type': type,
            'amount': amount,
            'balance': self.__balance
        })
    
    # 6. Magic Methods
    def __str__(self):
        return f"Account({self.account_holder}, ${self.__balance})"
    
    def __repr__(self):
        return f"BankAccount('{self.account_holder}', '{self.account_number}', {self.__balance})"
    
    def __eq__(self, other):
        return self.account_number == other.account_number
    
    def __lt__(self, other):
        return self.__balance < other.__balance
    
    # 7. Class Methods
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @classmethod
    def create_savings_account(cls, holder, number):
        """Alternative constructor for savings accounts"""
        account = cls(holder, number, 1000)  # Minimum $1000
        return account
    
    # 7. Static Methods
    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

# Usage demonstrating all concepts
alice = BankAccount("Alice", "ACC001", 1000)
bob = BankAccount("Bob", "ACC002", 500)

# Instance methods
alice.deposit(500)
alice.withdraw(200)

# Object interaction
alice.transfer(bob, 100)

# Magic methods
print(alice)  # Uses __str__()
accounts = sorted([alice, bob])  # Uses __lt__()

# Class methods
print(f"Total accounts: {BankAccount.get_total_accounts()}")
savings = BankAccount.create_savings_account("Charlie", "ACC003")

# Static methods
if BankAccount.is_valid_amount(100):
    alice.deposit(100)
```

---

## 📊 OOP Principles Summary

### 1. **Encapsulation** 🔒
- Hide internal data
- Provide controlled access through methods
- Example: Private `__balance` with `deposit()` and `withdraw()` methods

### 2. **Abstraction** 🎭
- Hide complex implementation details
- Show only essential features
- Example: User calls `deposit()`, doesn't need to know internal validation

### 3. **Modularity** 🧩
- Code organized in self-contained units (classes)
- Easy to maintain and update
- Example: BankAccount class contains all account-related code

---

## 🚀 How to Run

```bash
cd 27-bank-account-oop
python main.py
```

## 💡 Key Features

### 1. **Complete Banking Operations**
- Deposits with validation
- Withdrawals with balance checking
- Inter-account transfers
- Transaction history

### 2. **Interactive Menu System**
- Switch between accounts
- Real-time balance updates
- User-friendly prompts

### 3. **Transaction Tracking**
- Every operation logged
- Timestamped records
- Balance history

---

## 🎓 Common Mistakes to Avoid

### 1. Forgetting `self`
```python
❌ Wrong:
def deposit(amount):
    balance += amount  # Which object's balance?

✅ Correct:
def deposit(self, amount):
    self.balance += amount  # This object's balance!
```

### 2. Accessing Private Attributes Directly
```python
❌ Wrong:
account.__balance = 5000  # Bypasses validation!

✅ Correct:
account.deposit(5000)  # Uses proper validation!
```

### 3. Confusing Class and Instance Variables
```python
❌ Wrong:
class BankAccount:
    balance = 0  # Class variable - shared by all!

alice = BankAccount()
bob = BankAccount()
alice.balance = 1000  # Actually creates instance variable
bob.balance = 500

✅ Correct:
class BankAccount:
    def __init__(self):
        self.balance = 0  # Instance variable - unique per object
```

---

## 📖 Further Learning

- [Python OOP Tutorial (Official)](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools - Python Classes](https://www.w3schools.com/python/python_classes.asp)
- [Corey Schafer - OOP Series](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

---

**Difficulty**: Beginner  
**Time**: 2-3 hours  
**Prerequisites**: Basic Python (variables, functions, data types)

Master OOP and unlock powerful programming patterns! 🚀
