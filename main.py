import socket
import logging
import logging.config as lc
import config

logger = logging.getLogger("main")
lc.dictConfig(config.log_config)

SYNC_LEN = 4
SYNC_MSG = "SEND"
RECV_MSG = "RECV"
END_SIGN = "\n"
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("", 8674)
s.bind(addr)
num = 2

while True:
    sync_data0, addr0 = s.recvfrom(SYNC_LEN)
    logger.info(f"Get a connection with {addr0}")
    sync_data1, addr1 = s.recvfrom(SYNC_LEN)
    logger.info(f"Get a connection with {addr0}")
    # Start a new thread to handle
    if sync_data0.decode() == SYNC_MSG:
        src = addr0
        tgt = addr1
    else:
        src = addr1
        tgt = addr0
    # Source and target are determined
    while True:
        data, _ = s.recvfrom(BUFFER_SIZE)
        if not data:
            break
        s.sendto(data, tgt)

