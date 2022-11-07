import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      #'001'
        num2 = str(num2).zfill(2)      # '01'
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

kim = Account("예금주", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)