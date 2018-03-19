from greenlet import getcurrent as get_ident
import asyncio

async def fake_IO():
    await asyncio.sleep(1)
async def A():
    await fake_IO()
    s = get_ident()
    print(s)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([A(), A()]))
print(get_ident())

print("=========================================")
import threading

def run_thread(s):
    print(s, get_ident())

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(get_ident())

print("=========================================")

import gevent
def fake_IO():
    gevent.sleep(1)
def A():
    fake_IO()
    print(get_ident())

gevent.joinall([gevent.spawn(A), gevent.spawn(A)])






