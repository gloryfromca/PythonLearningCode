import io 
import sys 
import urllib.request 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf8')
print(sys.stdin.encoding)
print(sys.stdout.encoding)
