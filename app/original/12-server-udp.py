import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def echo_server(port):
    """A simple UDP echo server"""
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    
    while True:
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        if data:
            print("Data: %s" % data)
            sent = sock.sendto(data, address)
            print("Sent %s bytes back to %s" % (sent, address))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


# python 12-server-udp.py --port=9991