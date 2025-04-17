from threading import *
from time import sleep, perf_counter

def mythread1():
    print("i am thread1", "current thread execution is::", current_thread().getName())


def mythread2():
    print("i am thread2", "current thread execution is :::", current_thread().getName())


t1 = Thread(target=mythread1(), args=[])
t2 = Thread(target=mythread2(), args=[])

t1.start()
t2.start()

#You can create the threads individually, as we saw above.
# But there is an easier and more efficient way of doing that. We do this by using the ThreadPoolExecutor in Python

#using the ThreadPoolExecutor

def task():
    print('starting a task...')
    sleep(1)
    print('done')

start_time = perf_counter()

task()
task()


end_time = perf_counter()
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
