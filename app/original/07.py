import socket
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 2048
def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

    # Get the size of the socket's send buffer
    sndbufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send Buffer size [Before]:%d" %sndbufsize)
    rcvbufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Receive Buffer size [Before]:%d" %rcvbufsize)

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    sndbufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send Buffer size [After]:%d" %sndbufsize)
    rcvbufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Receive Buffer size [After]:%d" %rcvbufsize)
    
if __name__ == '__main__':
    modify_buff_size()
