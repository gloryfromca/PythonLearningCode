#-*- coding: UTF-8 -*-
import sys, getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
for op, value in opts:
    if op == "-h":
        print('h')
    if op == "-i":
        print(value)
    if op == "-o":
        print(value)
print(args)



