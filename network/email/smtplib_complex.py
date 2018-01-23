
import smtplib

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate

def format_addr(s):
    name,addr=parseaddr(s)
    # print(formataddr((Header(name,'utf-8').encode(),addr)))
    print('11111111111111')
    print(Header(name,'utf-8'))#神奇的打印结果
    print('11111111111111')
    print(type(Header(name,'utf-8')))
    print(Header(name,'utf-8').encode())#str

    return formataddr((Header(name,'utf-8').encode(),addr))

addr='1281269628@qq.com'
password='cxrviggngepjbaee'
to=['1281269628@qq.com',]
smtp_server="smtp.qq.com"

text = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '<p> <img src="cid:0"> </p>'+
    '<p> 我发的测试用 </p>'+
    '</body></html>', 'html', 'utf-8')


msg=MIMEMultipart('alternative')
# msg=MIMEMultipart()
msg.attach(MIMEText('hello', 'plain', 'utf-8'))

msg['From']=format_addr('你大哥我<%s>'%addr)
msg['To']=format_addr('hhh我<%s>'%to)
msg['Subject']=Header('元旦快乐，张波','utf-8').encode()#这里也要编码,这里的encode应该是重新改过的，用的是base64编码
# msg['Subject']=Header('元旦快乐，张波').encode()#没有'utf-8'也可以
print(Header('元旦快乐，张波').encode())#'utf-8'就是个参数，否则就用默认的参数，然后再编码为base64
print(type(Header('元旦快乐，张波').encode()))#str
print(type(Header('元旦快乐，张波')))#str
print('aaaaaaaa')
with open('\\Users\\Administrator\\Desktop\\120.jpg','rb')as f:
    mime=MIMEBase('image','jpeg',filename='120.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')#这个才是邮件中附件显示的名字
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    print(type(f.read()))
    encoders.encode_base64(mime)#编码成base64格式
    msg.attach(mime)

msg.attach(text)
print(type(msg))
print('*&&&&&&&&&&&&&&&&&&&&&&&')
print(type(msg.as_string(unixfrom=True)))
print(msg)

print('*&&&&&&&&&&&&&&&&&&&&&&&')
print(type(msg.as_string()))
print(msg)

# server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(addr, password)
# server.sendmail(addr, to, msg.as_string())#最后变为字符串
# server.quit()