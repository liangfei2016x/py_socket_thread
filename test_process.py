#test_process.py
#跨平台的多进程
#Process：进程对象
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))

if __name__ == '__main__':
    #父线程
    print('Parent process %s' % os.getpid())
    #子线程
    p=Process(target=run_proc,args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('Child process end')
