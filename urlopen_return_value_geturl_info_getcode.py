from urllib.request import urlopen
html=urlopen('https://www.baidu.com')
print(html.geturl())
print('------------')
print(html.info())
print('------------')
print(html.getcode())
print('------------')
print(html.read().decode('UTF-8'))
