import threading, time


class Knight(threading.Thread):
    _enemy_count = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')

        _enemies = self._enemy_count
        days = 0
        while _enemies > 0:
            _enemies -= self.power
            time.sleep(1)
            days += 1
            print(f'{self.name} сражается {days}..., осталось {_enemies} воинов.')

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')

