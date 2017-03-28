
import socket
class ping:
	def ping(self,host):
		
		UDP_IP = str(host)
		RUDP_PORT = 2004
		SUDP_PORT = 2003
		Ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # sending socket
		Rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # reciver socket
		Rsock.bind(("localhost", RUDP_PORT))#bind Rsock to recive messages
		MESSAGE = str("pinging "+str(host))
		Ssock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, SUDP_PORT))
		print ("[client] sent message:",MESSAGE)
		

