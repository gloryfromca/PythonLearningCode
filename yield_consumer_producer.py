def consumer():
    r=''
    
    while True:
        n= yield r
        print(n)
        if not n:
          print('1')
          return 
        print('[consumer] consuming%s...'%n) 
        r='200 OK'
def producer(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[producer] producing%s...'%n)
        r=c.send(n)
        print('[producer] consumer return%s...'%r)
    c.close()
c=consumer()
producer(c)