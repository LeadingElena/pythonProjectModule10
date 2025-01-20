import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        number_warriors = 100
        count_days = 0
        print(f'{self.name}, на нас напали!')
        while number_warriors:
            number_warriors -= self.power
            count_days += 1
            if number_warriors < 0:   #проверка количества воинов на отрицательный остаток
                number_warriors = 0
            print(f'{self.name} сражается {count_days}..., осталось {number_warriors} воинов.')
            time.sleep(1)
            if number_warriors <= 0:
                print(f'{self.name} одержал победу спустя {count_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')