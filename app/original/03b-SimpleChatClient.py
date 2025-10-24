#!/usr/bin/env python3
import select
import socket
import sys
import signal
import pickle
import struct
import argparse
import threading

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

# Some utilities (assumed to be used by both server and client)
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size_data = channel.recv(struct.calcsize("L"))
    try:
        size = socket.ntohl(struct.unpack("L", size_data)[0])
    except struct.error as e:
        return ''
    buf = b""
    while len(buf) < size:
        buf += channel.recv(size - len(buf))
    return pickle.loads(buf)[0]

class ChatClient:
    """A command line chat client using a separate input thread."""
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        # Initial prompt
        self.prompt = '[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print("Now connected to chat server @ port {}".format(self.port))
            self.connected = True
            # Send my name...
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error as e:
            print("Failed to connect to chat server @ port {}".format(self.port))
            sys.exit(1)

    def run(self):
        """Chat client main loop using a separate input thread."""
        def input_thread():
            # This thread handles user input from the console.
            while self.connected:
                line = sys.stdin.readline().strip()
                if line:
                    send(self.sock, line)

        # Start the input thread
        t = threading.Thread(target=input_thread, daemon=True)
        t.start()

        try:
            # Main thread: receive messages from the server.
            while self.connected:
                data = receive(self.sock)
                if not data:
                    print("Client shutting down.")
                    self.connected = False
                    break
                else:
                    # Print received messages
                    print("\n" + data)
                    # Optionally, reprint the prompt:
                    sys.stdout.write(self.prompt)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            print("Client interrupted.")
        finally:
            self.sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example with Select')
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        # Assuming ChatServer is defined elsewhere in your code.
        # For example:
        # server = ChatServer(port)
        # server.run()
        pass
    else:
        client = ChatClient(name=name, port=port)
        client.run()


# python 03-SimpleChatClient.py --name=client1 --port=8800
# python 03-SimpleChatClient.py --name=client2 --port=8800