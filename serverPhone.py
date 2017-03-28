#server for phone
import socket
import time
def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]

myIpAddress = get_ip_address()


UDP_IP = str(get_ip_address())
RUDP_PORT = 2003
SUDP_PORT = 2005
Ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # sending socket
Rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # reciver socket
Rsock.bind((UDP_IP, RUDP_PORT))#bind Rsock to recive messages

while True:	
	RECIEVED, addr = Rsock.recvfrom(1024) # buffer size is 1024 bytes
	print ("[server] got message:", RECIEVED,"from",addr)
	if RECIEVED == bytes("stop", "utf-8"):
		break	
	MESSAGE = str("echoing"+str(RECIEVED))
	time.sleep(2)#wait 10 seconds to respond
	print ("[server] echoing:", RECIEVED,"to",str(addr[0]))
	Ssock.sendto(bytes(MESSAGE, "utf-8"), (str(addr[0]), SUDP_PORT))
	
