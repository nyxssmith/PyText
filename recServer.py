
import socket
class recServer:
	def start(self,myIpAddress):

		UDP_IP = str(myIpAddress)
		RUDP_PORT = 2005
		SUDP_PORT = 2004
		Ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # sending socket
		Rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # reciver socket
		Rsock.bind((UDP_IP, RUDP_PORT))#bind Rsock to recive messages

		RECIEVED, addr = Rsock.recvfrom(1024) # buffer size is 1024 bytes
		print ("[server] got message:", RECIEVED,"from",str(addr[0]))
		
	def __init__(self):
		print("started")
