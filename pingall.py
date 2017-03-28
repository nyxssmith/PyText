#pings all devices on network on port 2003
import socket
import ipcalc#requires python-ipcalc from aur
import ping

import _thread
print("getting list of devices")

def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]

myIpAddress = get_ip_address()
print(myIpAddress)

workingDevices = []
def pingAll():
	for ip in ipcalc.Network(str(myIpAddress)+"/24"):
		print( str(ip))
		try:
			ping.ping().ping(ip)
			#workingDevices.append(ip)
		except ConnectionRefusedError:
			print("Connection Refused")
		
def startRecServer():
	import recServer
	print("starting server")
	recServer.recServer().start(myIpAddress)


pingAll()#pings everything. the server waits 30 seconds to reply, so that should be enough time to send em all

startRecServer()#starts listening of its own. this should stay alive for 30 seconds where it will then have a list of replies
#do in vm with many ip, so i can test. once list of ips are made, find the phone aka the one device. then get mac address or custom code and save/autheticate



#try:
#_thread.start_new_thread( startRecServer())
#_thread.start_new_thread( pingAll() )

#except:
#	print( "Error: unable to start thread")

	
print(workingDevices)
