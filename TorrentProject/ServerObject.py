import socket


class Node:
    """
    A server as represented by the client
    """
    connectionSpeed = 0
    ipAddress = ''
    server = socket.socket()

    def __init__(self, ip):
        self.ipAdress = ip
        self.server.connect((self.ipAddress, PORT))
