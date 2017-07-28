
import asyncio
import time

#回调函数
def callback(Future):
    print('callback:',Future.result())
	

async def hello_world(x):
    print('wait:',x)
    await asyncio.sleep(x)
    print("Hello World!{}".format(x))
    return 'done{}'.format(x)

#建立事件循环
loop = asyncio.get_event_loop()

#使用ensure_future是为了能够获得回调的结果，就是能够有task.result()方法
tasks = [
    asyncio.ensure_future(hello_world(3)),
    asyncio.ensure_future(hello_world(3)),
    asyncio.ensure_future(hello_world(3)),    
]
#tasks = [
#    hello_world(5),
#    hello_world(6),
#    hello_world(7),   
#]

#为每一个task绑定回调函数,回调函数会改变task.result的结果
for task in tasks:
    task.add_done_callback(callback)

print('==== start loop ====')
#asyncio.wait(tasks) 等待tasks全部完成 
#loop.run_until_complete loop等待asyncio.wait(tasks)执行完毕
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print('==== end loop ====')

for task in tasks:
    print('Task ret: ', task.result())
