import time
import threading
from datetime import datetime as dt, timedelta

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for number_of_word in range(1, word_count+1):
            file.write(f'Какое-то слово № {number_of_word}\n')
            time.sleep(0.1)
    print (f'Завершилась запись в файл {file_name}')

time_start = time.time()
result_func = []
for word_count, file_name in [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]:
    write_words(word_count, file_name)

time_end = time.time()
time_result = time_end - time_start
time_delta =  timedelta(seconds=time_result)
print(str(time_delta))

threads = []
time_start = time.time()
for count, name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=[count, name])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
time_end = time.time()
time_result = time_end - time_start
time_delta =  timedelta(seconds=time_result)
print(str(time_delta))

