import hashlib
def calc_md5(password):
	a=hashlib.md5()
	a.update(password,encode('utf-8'))
	return a.hexdigest()
db={}
def register(username,password):
	a=hashlib.md5()
	a.update((password+username+'the Salt').encode('utf-8'))
	db[username]=a.hexdigest()

def log(username,password):
	a=hashlib.md5()
	a.update((password+username+'the Salt').encode('utf-8'))
	if db[username]==a.hexdigest():
		print('log in success!')
	else:
		print('please check your username or password!')
register('zhanghui','1994zhhu')
log('zhanghui','1994zhhu')
log('zhanghui','11994zhhu')