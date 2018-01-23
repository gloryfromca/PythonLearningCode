import base64
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

def format_addr(s):
	name,addr=parseaddr(s)
	print(formataddr((Header(name,'utf-8').encode(),addr)))
	print(Header(name,'utf-8').encode())
	print(name.encode('utf-8'))
	print(base64.b64encode(name.encode('utf-8')))#base64编码出来的和传送的相同
	return formataddr((Header(name,'utf-8').encode(),addr))

msg=MIMEText('hello,send','plain','utf-8')
addr='1281269628@qq.com'
password='cxrviggngepjbaee'
to=['1281269628@qq.com','zhhuwudi@163.com']
msg['From']=format_addr('你大哥我<%s>'%addr)
msg['To']=format_addr('hhh<%s>'%to)#出来的header结果好像没有写明具体的to地址
msg['Subject']=Header('我是主题','utf-8').encode()
print(type(msg))
print(msg.as_string())
smtp_server="smtp.qq.com"
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(addr,password)
server.sendmail(addr,to,msg.as_string())
server.quit()