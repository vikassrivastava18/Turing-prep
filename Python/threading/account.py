from concurrent.futures import ThreadPoolExecutor
import time

class Account:
    def __init__(self):
        self.balance = 100

    def update(self, transaction, amount):
        balance_copy = self.balance
        balance_copy += amount
        time.sleep(1)
        self.balance = balance_copy

if __name__ == '__main__':
    for _ in range(5):
        account = Account()
        with ThreadPoolExecutor(max_workers=2) as ex:
            for transaction, amount in [('deposit', 50), ('withdrawl', -150)]:
                ex.submit(account.update, transaction, amount)
        print(f'Final balance is: {account.balance}')

