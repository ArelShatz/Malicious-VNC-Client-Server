import socket
import time
import numpy as np


validVersions = ["RFB 003.003\n", "RFB 003.007\n", "RFB 003.008\n"]
supportedSecurity = [1, 2]


class RFBClient():
    def __init__(self, host = "127.0.0.1"):
        self.__CHUNK = 65536
        self.__host = host
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.__sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, self.__CHUNK)
        self.__address = (self.__host, 3398)
        self.__sock.connect(self.__address)
        self.__sock.send(b'\x00')

        self.Handshake()

    def Handshake(self):
        #ProtocolVersion Handshake
        maxVer = self.__sock.recv(12).decode()
        if maxVer in validVersions:
            self.__sock.send(maxVer.encode())

        else:
            self.__sock.close()
            return


        #Security Handshake
        securityOpts = self.__sock.recv(8)
        securityArrLength = securityOpts[0]
        if securityArrLength == 0:
            self.onError()
            return
        
        securityTypes = list(securityOpts[1:])
        common_elements = list(set(securityTypes).intersection(supportedSecurity))
        bestValidSecurity = max(common_elements)
        self.__sock.send(bestValidSecurity.to_bytes(1, "big"))
        securityOK = self.__sock.recv(4)
        if bestValidSecurity == 1:
            self.onError()
            return

        elif bestValidSecurity == 2:
            challenge = self.__sock.recv(16)
            

        self.Initialization()


    def Initialization(self):
        pass


        #SecurityResult Handshake


    def onError(self):
        errMsg = self.__sock.recv(32)
        print(errMsg[4:])
        self.__sock.close()


client = RFBClient()
