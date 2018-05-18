import sys
import os
import time

pid = os.fork()
# for father_process
if pid > 0:
    print("parent process write into stdout!")
    sys.exit(0)

# for subp_rocess
os.chdir("/")
## start new session group
os.setsid()
os.umask(0)

sys.stdout.flush()
sys.stderr.flush()

# redirect stdin stdout stderr
with open('/dev/null') as read_null, open('/dev/null','w') as write_null:
    # method dup2() duplicates file descriptor
    # fd to fd2
    os.dup2(read_null.fileno(), sys.stdin.fileno())
    os.dup2(write_null.fileno(), sys.stdout.fileno())
    os.dup2(write_null.fileno(), sys.stderr.fileno())

while True:
    print("subprocess write into stdout!")
    time.sleep(1)
