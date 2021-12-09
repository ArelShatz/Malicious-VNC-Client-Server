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
                pass

		#Security Handshake
		securityOpts = self.__sock.recv(6)
		securityArrLength = securityOpts[0]
		securityTypes = list(securityOpts[1:])
		common_elements = np.intersect1d(securityTypes, supportedSecurity)
		bestValidSecurity = np.amax(common_elements)
		print(common_elements)
		print(bestValidSecurity)
		self.__sock.send(bestValidSecurity.to_bytes(1, "big"))


client = RFBClient()

