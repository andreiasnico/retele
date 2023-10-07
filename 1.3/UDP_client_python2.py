import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("salut sunt eu un haiduc",("192.168.14.117",5555))                 
#print s.recvfrom(100)            

