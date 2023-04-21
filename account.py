class Account:
    def init(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.__name