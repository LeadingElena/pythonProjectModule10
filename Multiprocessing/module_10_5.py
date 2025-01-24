import multiprocessing
import time
from datetime import timedelta


def read_info(name):
    all_data = []

    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
time_start = time.time()
for name in filenames:
    read_info(name)
time_end = time.time()
res_time = time_end - time_start
print(timedelta(seconds=res_time))

# Многопроцессный
"""if __name__ == '__main__':
    time_start = time.time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    time_end = time.time()
    res_time = time_end - time_start
    time_delta = timedelta(seconds=res_time)
    print(time_delta)"""

"""
Вывод на консоль, 2 запуска (результаты могут отличаться):
0:00:03.046163 (линейный)
0:00:01.092300 (многопроцессный)
"""
