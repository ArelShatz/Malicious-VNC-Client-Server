import socket
import time
from Crypto.Random import get_random_bytes


validVersions = ["RFB 003.003\n", "RFB 003.007\n", "RFB 003.008\n"]
supportedSecurity = [1, 2]


class RFBServer():
    def __init__(self, host = "127.0.0.1"):
        self.__CHUNK = 65536
        self.__host = host
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.__sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, self.__CHUNK)
        self.__address = (self.__host, 3398)
        self.__sock.bind(self.__address)
        self.__sock.listen(1)
        self.conn, addr = self.__sock.accept()
        data = ""
        while not data:
            data = self.conn.recv(1).decode()
            time.sleep(1)

        self.Handshake()


    def Handshake(self):
        #ProtocolVersion Handshake
        self.conn.send(validVersions[-1].encode())
        usedVer = self.conn.recv(12).decode()


        #Security Handshake
        if usedVer not in validVersions:
            byte = (0).to_bytes(1, "big")
            self.conn.send(byte)
            self.onError("the server does not support the version specified by the client")
            return
            
        byte = len(supportedSecurity).to_bytes(1, "big") + bytes(supportedSecurity)
        self.conn.send(byte)
        usedSecurity = self.conn.recv(1)


        #SecurityResult Handshake
        if usedSecurity == 0:
            self.conn.send((0).to_bytes(4, "big"))
            self.onError("the server does not support the security type specified by the client")
            return

        elif usedSecurity == 2:
            challenge = b''
            for _ in range(16):
                challenge += random.randint(0, 255).to_bytes(1, "big")

            self.conn.send(challenge)


        self.conn.send((1).to_bytes(4, "big"))
        self.Initialization()


    def Initialization(self):
        pass


    def onError(self, errMsg):
        self.conn.send(len(errMsg).to_bytes(4, "big") + errMsg.encode())
        self.conn.close()


server = RFBServer()
