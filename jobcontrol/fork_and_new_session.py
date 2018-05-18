import sys
import os
import time

pid = os.fork()
# for father_process
if pid > 0:
    while True:
        print("parent process write into stdout!")
    sys.exit(0)

# for sub_process
os.chdir("/")
## start new session group
os.setsid()
os.umask(0)

while True:
    print("subprocess write into stdout!")
    #for line in sys.stdin:
    #    print(line + "got!")
    time.sleep(1)
