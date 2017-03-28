
import socket

UDP_IP = "localhost"
RUDP_PORT = 2004
SUDP_PORT = 2003
Ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # sending socket
Rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # reciver socket
Rsock.bind((UDP_IP, RUDP_PORT))#bind Rsock to recive messages
print("Send stop to stop both the server and client")
while True:
	MESSAGE = input("enter a message:	")
	Ssock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, SUDP_PORT))
	print ("[client] sent message:",MESSAGE)
	if MESSAGE == "stop":
		break
	RECIEVED, addr = Rsock.recvfrom(1024) # buffer size is 1024 bytes
	print ("[client] got message:	"+str(RECIEVED))

