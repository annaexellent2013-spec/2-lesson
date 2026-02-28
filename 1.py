class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit (self, amount):
        self.balance += amount
        print(f"Рахунок попвнено на {amount}. Новий баланс рахунку: {self.balance}")

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount}. Залишилося: {self.balance}")
        else:
            print("Недостатньо коштів на рахунку.")


first_account = BankAccount("UA12345678", 1000)
first_account.deposit(500)
first_account.withdraw(300)
first_account.withdraw(2000)