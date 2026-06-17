import random
random.seed(7)
class Bank:
    def __init__(self,name,balance):
        self.name = name
        # Protected
        self._account_number = random.randint(10000000000,99999999999)
        self.__balance = balance # Private 
    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self.__balance}")
    # Setter Methods
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    # Getter Method
    def bank_balance(self):
        return self.__balance

pranavi = Bank("Pranavi",10000)
pranavi.get_details()
print(pranavi._account_number)
# print(pranavi.__balance)
print(pranavi.bank_balance())
pranavi.deposit(100000)
print(pranavi.bank_balance())
pranavi.withdraw(10000)
print(pranavi.bank_balance())