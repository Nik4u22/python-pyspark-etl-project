import threading

import time
from threading import *
from time import sleep, perf_counter


def thread_function(name, delay):
    print(f"Thread '{name}' started...")
    time.sleep(delay)
    print(f"Thread '{name}' finished..")


thread1 = threading.Thread(target=thread_function, args=("Thread1", 2))

thread2 = threading.Thread(target=thread_function, args=("Thread2", 4))

thread1.start()
thread2.start()

print("This is also part of the main thread.")

thread1.join()
thread2.join()

print("All threads have finished execution.")
print("google")
print("nihilism")


# main thread will execute after the finishing of threads..... by using JOin()


def task():
    print('starting task......')
    sleep(1)
    print('done')


start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f"the process time {end_time - start_time: 0.2f} seconds()")

def task2(id):
    print(f'starting task {id}....')
    sleep(1)
    print(f'The task {id} completed..')

start_time = perf_counter()

threads = []

for n in range (1,11):
    t = Thread(target=task2, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()
print(f"the process time {end_time - start_time: 0.2f} seconds()")
