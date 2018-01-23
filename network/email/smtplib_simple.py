import smtplib

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate

def format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

msg=MIMEText('hello,send','plain','utf-8')
print(msg)
addr='1281269628@qq.com'
password='cxrviggngepjbaee'
to=['1281269628@qq.com','zhhuwudi@163.com']
# msg['From']=format_addr('你大哥我<%s>'%addr)
# msg['To']=format_addr('hhh<%s>'%to)
# msg['Subject']=Header('我是主题','utf-8').encode()
# print(type(msg))
# print(msg.as_string())


smtp_server="smtp.qq.com"
server=smtplib.SMTP_SSL(smtp_server,465)
# server.set_debuglevel(1)
server.login(addr,password)
server.sendmail(addr,to,msg.as_string())
server.quit()