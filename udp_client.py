# import socket
# from datetime import datetime
# server_address=('localhost',6789)
# max_size=4096

# print ('starting the client at', datetime.now())
# client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# client.sendto(b'HEY!',server_address)
# data,server=client.recvfrom(max_size)
# print('at',dateime.now(),server,'said',data)
# client.close()

import socket
from datetime import datetime

address=('localhost',6789)
max_size=1000

print('starting the client at', datetime.now())
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'hey!')
data=client.recv(max_size)
print('at',datetime.now(),'someone replied', data)
client.close()
