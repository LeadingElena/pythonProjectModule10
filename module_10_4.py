from queue import Queue
import threading
import time
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

            time.sleep(1)  # Добавляем задержку, чтобы не загружать процессор

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

"""Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):

Maria сел(-а) за стол номер 1
Oleg сел(-а) за стол номер 2
Vakhtang сел(-а) за стол номер 3
Sergey сел(-а) за стол номер 4
Darya сел(-а) за стол номер 5
Arman в очереди
Vitoria в очереди
Nikita в очереди
Galina в очереди
Pavel в очереди
Ilya в очереди
Alexandra в очереди
Oleg покушал(-а) и ушёл(ушла)
Стол номер 2 свободен
Arman вышел(-ла) из очереди и сел(-а) за стол номер 2"""