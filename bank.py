# Определить класс 'Account', имитирующий банковский счет.
# Класс должен иметь атрибуты для хранения идентификатора владельца счета и баланса счета.
# Методы для депозита (пополнения) и снятия денежных средств, если на счету достаточно средств.

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")

    def withdraw(self, money=None):
        if money > self.balance:
            print(f"Недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли средства со счета. Остаток на счете - {self.balance}")

    def all_balance(self):
        print(f"Ваш баланс - {self.balance}")

man = Account(1221323213, 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(500)
man.all_balance()
