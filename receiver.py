import client
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("houlu.me", 8674)

client.recv(s, server_addr)
