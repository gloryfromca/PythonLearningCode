# import requests
# # from Pillow import Image

# r = requests.get('http://httpbin.org/get')
# if r.status_code == requests.codes.ok:
#     print(r.headers)
#     print(r.content)
#     print(r.encoding)
#     print(r)

import requests
import re

cs_url  = 'https://github.com/login'
cs_user = 'huizhang1995@gmail.com'
cs_psw  = '19940203zhhu'
my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

sss     = requests.Session()
r       = sss.get(cs_url, headers = my_headers)

reg     = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern = re.compile(reg)
# print(r.content)
result  = pattern.findall(r.content.decode('utf-8'))#二进制变为可处理的string
print(result)
token   = result[0]
my_data = {
    'commit' : 'Sign in',
    'utf8' : '%E2%9C%93',
    'authenticity_token' : token,
    'login' : cs_user,
    'password' : cs_psw
}
cs_url  = 'https://github.com/session'
r       = sss.post(cs_url, headers = my_headers, data = my_data)
print (r.url, r.status_code, r.history)#经由 302 跳转，打开了（200）GitHub 首页。
print(r.content)
#在 Tamper Chrome 中，我们发现：虽然登录页面是 https://github.com/login，
#但实际接收表单的是 https://github.com/session。
#若登录成功，则跳转到 https://github.com/ 首页，返回状态码 200。