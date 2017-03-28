
import socket
import time
import threading

from queue import Queue

def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]

myIpAddress = get_ip_address()
print(myIpAddress)

UDP_IP = str (myIpAddress)
RUDP_PORT = 2005
SUDP_PORT = 2003
Ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # sending socket
Rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # reciver socket
Rsock.bind((UDP_IP, RUDP_PORT))#bind Rsock to recive messages

paused = False

def waitForResponse():
	global paused
	paused = True;
	RECIEVED, addr = Rsock.recvfrom(1024) # buffer size is 1024 bytes
	print ("[client] got message:	"+str(RECIEVED))
	#t2.stop()

	paused = False


def waitTenSeconds():
	global paused
	paused = True

	time.sleep(10)
	if(paused):
		print("10 seconds passed, cannot confirm that last message was sent")
	#t1.stop()
	
	paused = False




        
# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an task from the queue
        task = q.get()
        print(task)
        # Run the task
        time.sleep(.5)

        # completed with the job
        q.task_done()  
        
        
# Create the queue and threader 
q = Queue()

# allow/create 20 threads
for x in range(20):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

start = time.time()

# 20 jobs assigned.
for worker in range(20):
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:',time.time() - start)


#print(_thread.activeCount)

print("Send stop to stop both the server and client")
while True:
	MESSAGE = input("enter a message:	")
	Ssock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, SUDP_PORT))
	print ("[client] sent message:",MESSAGE)
	if MESSAGE == "stop":
		break

	#now to either wait 10 seconds or get response
	
	t1 = threading.Thread(target=waitForResponse)
	# classifying as a daemon, so they will die when the main dies
	t1.daemon = True
	# begins, must come after daemon definition
	t1.start()

	
	t2 = threading.Thread(target=waitTenSeconds)
	# classifying as a daemon, so they will die when the main dies
	t2.daemon = True
	# begins, must come after daemon definition
	t2.start()
	
	print(paused)
	while(paused):
		pass
	


#waitForResponse()
	

