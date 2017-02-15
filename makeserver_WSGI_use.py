from wsgiref.simple_server import make_server
def application(env,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>hello,%s!</h1>'%(env['COMSPEC'])
	return [body.encode('utf-8')]
sim_http=make_server('',8670,application)
## 创建一个服务器，IP地址为空，端口是8000，处理函数是application
print('ready')
sim_http.serve_forever()
