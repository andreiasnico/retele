import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("salut sunt eu un haiduc",("127.0.0.1",5555))                 
print s.recvfrom(100)            
