import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop1):
    addr=8003
    app = web.Application(loop=loop1)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', addr)
    print('Server started at http://127.0.0.1:%d...'%addr)
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
#放在loop中完成初始化，创建一个Server。
#然后Sever负责处理请求。
#请求来的时候调用相应函数在loop中执行。