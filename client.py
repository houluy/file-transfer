import socket

SYNC_MSG = "SEND"
RECV_MSG = "RECV"
BUFFER_SIZE = 1024
END_SIGN = "\u169D"

def recv(s, server_addr):
    s.sendto(RECV_MSG.encode(), server_addr)
    file_name, _ = s.recvfrom(BUFFER_SIZE)
    try:
        f = open(file_name.decode(), 'wb')
    except:
        pass
    else:
        while True:
            data, _ = s.recvfrom(BUFFER_SIZE)
            if data == END_SIGN.encode():
                break
            else:
                f.write(data)
                f.write(b'hello')
    finally:
        f.close()
    s.close()

def send(s, server_addr, filename):
    s.sendto(SYNC_MSG.encode(), server_addr)
    with open(filename, 'rb') as f:
        s.sendto(filename.encode(), server_addr)
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            s.sendto(data, server_addr)
        s.sendto(END_SIGN.encode(), server_addr)
        s.close()


