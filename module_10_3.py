import random, time, threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            n = random.randint(50, 100)
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            self.balance += n
            print(f'Пополнение: {n}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            n = random.randint(50, 100)
            print(f'Запрос на {n}')
            if n <= self.balance:
                self.balance -= n
                print(f'Снятие: {n}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
