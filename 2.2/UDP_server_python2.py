import re
import socket
vowels= "AaEeIiOoUu"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("0.0.0.0",5555))                           
buff,addr=s.recvfrom(100)                           
res = len(re.findall(r'\w+', buff))

print res
s.sendto(str(res), addr)  
