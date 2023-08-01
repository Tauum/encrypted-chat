import socket


def get():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    port = 9999
    return hostname, IPAddr, port
