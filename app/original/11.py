import socket
import struct
import sys
import time
NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800
def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
        # 0x1b: (Single Byte)
        # LI (Leap Indicator): 2 bits, usually set to 0 indicating no warning.
        # VN (Version Number): 3 bits, here indicating NTP version 3.
        # Mode: 3 bits, with the value 3 representing a client mode.
        # SMTP Request is total 48-bytes
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        print('Response received from:', address)
    t = struct.unpack( '!12I', data )[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()
