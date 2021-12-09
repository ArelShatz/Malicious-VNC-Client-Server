import socket
import time

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
		self.conn.send("RFB 003.008\n".encode())
		usedVer = self.conn.recv(12).decode()

		#Security Handshake
		byte = len(security).to_bytes(1, "big") + bytes(security)
		self.conn.send(byte)
		usedSecurity = self.conn.recv(1)
                #if usedSecurity == 0:
                #        pass
                        


server = RFBServer()

