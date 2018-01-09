#hw11.1


# import socket
# from datetime import datetime
# from time import sleep
# address=('localhost',6789)
# max_size=4096

# print('starting the client at',datetime.now())
# client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
# 	sleep(5)
# 	client.sendto(b'time',address)
# 	data,server_addr=client.recvfrom(max_size)
# 	print('client read',data)
# client.close()


#hw11.2
# import zmq
# from datetime import datetime
# from time import sleep 

# host='127.0.0.1'
# port=6789
# context=zmq.Context()
# client=context.socket(zmq.REQ)
# client.connect('tcp://%s:%s' %(host,port))
# print('client start at',datetime.utcnow())
# while True:
# 	sleep(5)
# 	request=b'time'
# 	client.send(request)
# 	reply=client.recv()
# 	print('client received %s' %reply)

#hw11.3 xmlrpc_time_client.py
# import xmlrpc.client
# from time import sleep 

# proxy=xmlrpc.client.ServerProxy('http://localhost:6789/')
# while True:
# 	sleep(5)
# 	data=proxy.now()
# 	print('client.received',data)

#hw11.4 redis.lucy.py
# import redis
# from datetime import datetime
# from time import sleep


# conn=redis.Redis()
# timeout=10
# conveyor='chocolate'
# while True:
# 	sleep(0.5)
# 	msg=conn.blpop(conveyor,timeout)
# 	remaining=conn.llen(conveyor)
# 	if msg:
# 		piece=msg[1]
# 		print('lucy got a ',piece,'at',datetime.utcnow(),
# 			',only,',remaining,'left')
		
#11.4 poem_sub.py
import string
import zmq
host='127.0.0.1'
port=6789
ctx=zmq.Context()
sub=ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' %(host,port))
sub.setsockopt(zmq.SUBSCRIBE,b'vowels')
sub.setsockopt(zmq.SUBSCRIBE,b'five')
while True:
	topic,word=sub.recv_multipart()
	print(topic,word)
	