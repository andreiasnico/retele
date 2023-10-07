import re
import socket
vowels= "AaEeIiOoUu"
consoane ="qQWwRrTtyYPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("0.0.0.0",5555))
buff,addr=s.recvfrom(100)

word_list=buff.split()
mylist=sorted(word_list, key=lambda x: sum(1 for y in x if y in consoane),reverse=True)


print mylist[0] 
s.sendto(mylist[0], addr)  
