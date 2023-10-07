import socket
vowels= "AaEeIiOoUu"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("0.0.0.0",5555))                           
buff,addr=s.recvfrom(100)                            
conc=buff.replace(" ","")
print conc
s.sendto(conc, addr)  
