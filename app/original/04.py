import socket
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
        
    print("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_service_name()

# HTTP: Port 80 (web trafiği)
# HTTPS: Port 443 (güvenli web trafiği)
# FTP: Port 21 (dosya transferi)
# SMTP: Port 25 (e-posta gönderimi)
# POP3: Port 110 (e-posta alma)
# IMAP: Port 143 (e-posta alma)
# DNS: Port 53 (alan adı çözümlemesi)
# RDP: Port 3389 (uzak masaüstü)
