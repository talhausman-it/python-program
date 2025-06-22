class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance              # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance is ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance is ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Create an object of BankAccount
account = BankAccount("John Doe", 10000)

# Access public attribute
print("Account Holder:", account.account_holder)

# Access private attribute (should use method)
print("Initial Balance:", account.get_balance())

# Deposit and withdraw using methods
account.deposit(2000)
account.withdraw(5000)

# Trying to access private variable directly (will fail)
# print(account.__balance)  # ❌ This will raise an AttributeError

#thunder method exapmle
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

# Creating book objects
book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 300)

# Using dunder methods
print(book1)            # Calls __str__: "Book: Python Basics"
print(len(book1))       # Calls __len__: 300
print(book1 == book2)   # Calls __eq__: True

#abstruction method
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

    def stop_engine(self):
        print("Bike engine stopped.")

# main code
car = Car()
car.start_engine()
car.stop_engine()

bike = Bike()
bike.start_engine()
bike.stop_engine()

# vehicle = Vehicle()  # ❌ Error: Can't instantiate abstract class
#@decorater method
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
