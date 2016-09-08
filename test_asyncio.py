#test_asyncio.py

import asyncio

#把生成器标记为协程
@asyncio.coroutine
def hello():
    print('hello world');
    r=yield from asyncio.sleep(1)
    print('Hello again')
#获取EventLoop()
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.close()