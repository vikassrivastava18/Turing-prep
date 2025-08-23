from concurrent.futures import ThreadPoolExecutor
import time
import threading


class Account:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def update(self, trans, amount):
        print(f'Transaction {trans} thread is starting')
        with self.lock:
            if self.balance <= 0 and trans == 'withdrawl':
                return None
            local_copy = self.balance
            local_copy += amount
            time.sleep(1)
            self.balance = local_copy
        print(f'Transaction {trans} completed.')

if __name__ == '__main__':
    account = Account()
    with ThreadPoolExecutor(max_workers=2) as e:
        for trans, amount in [('submit', 50), ('withdrawl', -100)]:
            e.submit(account.update, trans, amount)

    print(f'Final amount: {account.balance}.')

