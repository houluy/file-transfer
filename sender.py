import client
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("houlu.me", 8674)
filename = "test.txt"

client.send(s, server_addr, filename)
