#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.17", 4444))


'''
In 192.168.1.17 we listen for incoming connections using netcat
>nc -vv -l -p 4444
'''