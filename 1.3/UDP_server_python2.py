import socket
vowels= "AaEeIiOoUu"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("0.0.0.0",5555))                           
buff,addr=s.recvfrom(100)                           
counter = sum([1 for c in buff if c in 'aeiou'])
print counter
s.sendto(str(counter), addr)  

