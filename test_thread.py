#test_thread.py
import time,threading

import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

"""def loop():
    print('thread %s is running...(子)' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended...(子)' % threading.current_thread().name)

#任何进程会默认启动一个线程，这个线程叫主线程
print('thread %s is running...(主)' % threading.current_thread().name)
#子线程
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended...(主)' % threading.current_thread().name)

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n

def run_thread(n):
    for i in range(100000):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
"""
print('====================')
#ThreadLocal对象
local_school = threading.local()

def process_student():
    #获得当前线程相关的student
    std=local_school.student
    print('Hello ,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #把student绑定到ThreadLocal
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, name='Thread-A', args=('Alice',))
t2 = threading.Thread(target=process_thread, name='Thread-B', args=('Bob',))

t1.start()
t2.start()
t1.join()
t2.join()