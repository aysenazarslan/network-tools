import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def echo_client(port):
    """A simple UDP echo client"""
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
    message = "Test message. This will be echoed"
    
    try:
        print("Sending: %s" % message)
        # Send the message to the server
        sent = sock.sendto(message.encode('utf-8'), server_address)
        
        # Receive the echoed message
        data, server = sock.recvfrom(data_payload)
        print("Received: %s" % data.decode('utf-8'))
        
    except socket.error as e:
        print("Socket error: %s" % e)
    finally:
        print("Closing the connection")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)

# python 12-client-udp.py --port=9991