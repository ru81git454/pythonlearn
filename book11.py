# import multiprocessing as mp
# def washer(dishes,output):
# 	for dish in dishes:
# 		print('washing',dish,'dish')
# 		output.put(dish)

# def dryer(input):
# 	while True:
# 		dish=input.get()
# 		print('drying',dish,'dish')

# dish_queue=mp.JoinableQueue()
# dryer_proc=mp.Process(target=dryer,args=(dish_queue,))
# dryer_proc.daemon=True
# dryer_proc.start()

# dishes=['salad','bread','entree','dessert']

# washer(dishes,dish_queue)
# dish_queue.join()
# import threading
# def do_this(what):
# 	whoami(what)
# def whoami(what):
# 	print(" thread %s says: %s" %(threading.current_thread(),what))

# if __name__ == "__main__":
# 	whoami('i am the main program')
# 	for n in range(4):
# 		p=threading.Thread(target=do_this, args=("I am function %s"%n,))
# 		p.start()

# def interview(name):
    
#     print('hello professor i am %s use process %s to show' %(name,os.getpid()))
# def introduction(name):
#     print('%s aaa use process %s to show' %(name,os.getpid()))

# import multiprocessing as mp
# if __name__=='__main__':
#     interview('pei')
#     for n in range(4):
#         p=mp.Process(target=introduction,args=(' this is %s' %n,))
#         p.start()
'''綠色執行緒'''

# import threading
# def do_this(what):
#     whoami(what)
# def whoami(what):
#     print("thread %s says: %s" %(threading.current_thread(),what))
# from gevent import monkey
# monkey.patch_all()
# import gevent
# from gevent import socket
# hosts=['www.crappytaxidermy.com','www.walterpottertaxidermy.com','www.antique-taxidermy.com']
# jobs=[gevent.spawn(gevent.socket.gethostbyname,host) for host in hosts]
# gevent.joinall(jobs,timeout=5)
# for job in jobs:
# 	print(job.value)

# import gevent
# from gevent import monkey;monkey.patch_all()
# import socket
# hosts=['www.crappytaxidermy.com','www.walterpottertaxidermy.com','www.antique-taxidermy.com']
# jobs=[gevent.spawn(socket.gethostbyname,host) for host in hosts]
# gevent.joinall(jobs,timeout=5)
# for job in jobs:
# 	print(job.value)

# '''twist'''
# from twisted.internet import protocol,reactor

# class knock(protocol.Protocol):
# 	def dataReceived(self,data):
# 		print('client:',data)
# 		if data.startswith('knock knock'):
# 			response='who is there?'
# 		else:
# 			response=data+'who?'
# 		print('server:',response)
# 		self.transport.write(response)

# reactor.listenTCP(8000,knockFactory())
# reactor.run()
# import redis
# conn=redis.Redis()
# print('washing is starting')
# dishes=['salad','bread','entree','dessert']
# for dish in dishes:
# 	conn.rpush('dishes', dish)
# 	print('push', dish)
# conn.rpush('dishes','quit')
# print('washer is done')

# 發布訂閱模式 redis
# import redis
# import random
# conn=redis.Redis()
# cats=['s','p','m','n']
# hats=['s','b','t','f']
# for msg in range(10):
# 	cat=random.choice(cats)
# 	hat=random.choice(hats)
# 	print('Publish: %s wears a %s' %(cat,hat))
# 	conn.publish(cat,hat)
#zeroMQ pub-sub
# import zmq
# import random
# import time
# host='*'
# port=6789
# ctx=zmq.Context()
# pub=ctx.socket(zmq.PUB)
# pub.bind('tcp://%s:%s' %(host,port))
# cats=['s','p','m','n']
# hats=['s','b','t','f']
# time.sleep(1)
# for msg in range(10):
# 	cat=random.choice(cats)
# 	cat_bytes=cat.encode('utf-8')
# 	hat=random.choice(hats)
# 	hat_bytes=hat.encode('utf-8')
# 	print('publish: %s wears a %s' %(cat,hat))
# 	pub.send_multipart([cat_bytes,hat_bytes])

# from datetime import datetime
# import socket
# server_address=('localhost',6789)
# max_size=4096

# print('Starting the server at', datetime.now())
# print('waiting for a client to call.')
# server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# server.bind(server_address)
# data,client=server.recvfrom(max_size)

# print('at',datetime.now(),client,'said',data)
# server.sendto(b'Are you talking to me?',client)
# server.close()
# from datetime import datetime
# import socket
# address=('localhost',6789)
# max_size=1000

# print('starting the server at', datetime.now())
# print('waiting for a client to call')
# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(address)
# server.listen(5)
# client,addr=server.accept()
# data=client.recv(max_size)
# print('at',datetime.now(),client,'said',data)
# client.sendall(b'are you talking to me?')
# client.close()
# server.close()

#p308 zeroMQ
# import zmq
# host='127.0.0.1'
# port=6789
# context=zmq.Context()
# server=context.socket(zmq.REP)
# server.bind("tcp://%s:%s" %(host,port))
# while True:
# 	#wait for next request from client
# 	request_bytes=server.recv()
# 	request_str=request_bytes.decode('utf-8')
# 	print('that voice in my head says: %s' %request_str)
# 	reply_str='Stop saying: %s' %request_str
# 	reply_bytes=bytes(reply_str,'utf-8')
# 	server.send(reply_bytes)
#DNS
# import socket 
# socket.gethostbyname('www.crappytaxidermy.com')
# socket.gethostbyname_ex('www.crappytaxidermy.com')

# import requests
# url='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json'
# response=requests.get(url)
# data=response.json()
# for video in data['feed']['entry'][0:6]:
# 	print(video['title']['$t'])

# from xmlrpc.server import SimpleXMLRPCServer
# def double(num):
# 	return num*2

# server=SimpleXMLRPCServer(("localhost",6790))
# server.register_function(double,'double')
# server.serve_forever()

#msgpack
# from msgpackrpc import Server,Address
# class Services():
# 	def double(self,num):
# 		return num*2

# server=Server(Services())
# service.listen(Address('localhost',6789))
# server.start()

#11.1 udp_time_server
# from datetime import datetime
# import socket
# address=('localhost',6789)
# max_size=4096
# print('starting the server at',datetime.now())
# print('waiting for a client to call')
# server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# server.bind(address)
# while True:
# 	data,client_addr=server.recvfrom(max_size)
# 	if data==b'time':
# 		now=str(datetime.utcnow())
# 		data=now.encode('utf-8')
# 		server.sendto(data,client_addr)
# 		print('server sent',data)
# server.close()

#11.2 zmq_time server.py
# import zmq
# from datetime import datetime
# host='127.0.0.1'
# port=6789
# context=zmq.Context()
# server=context.socket(zmq.REP)
# server.bind('tcp://%s:%s' %(host,port))
# print('server start at',datetime.utcnow())
# while True:
# 	#wait for next request from client
# 	message=server.recv()
# 	if message==b'time':
# 		now=datetime.utcnow()
# 		reply=str(now)
# 		server.send(bytes(reply,'utf-8'))
# 		print('server sent',reply)

# #11.3 xmlrpc_time)server.py
# from xmlrpc.server import SimpleXMLRPCServer


# def now():
# 	from datetime import datetime
# 	data=str(datetime.utcnow())
# 	print('server sent',data)
# 	return data 

# server=SimpleXMLRPCServer(('localhost',6789))
# server.register_function(now,'now')
# server.serve_forever()

#11.4 redis_choc_supply.py
# import redis
# import random
# from time import sleep

# conn=redis.Redis()
# vars=['truffle','cherry','caramel','nougat']
# conveyor='chocolates'
# while True:
# 	seconds=random.random()
# 	sleep(seconds)
# 	piece=random.choice(vars)
# 	conn.rpush(conveyor,piece)	

#11.5
import string
import zmq

host='127.0.0.1'
port=6789
ctx=zmq.Context()
pub=ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' %(host,port))

with open('today.txt','rt') as poem:
	words=poem.read()
for word in words.split():
	word=word.strip(string.punctuation)
	data=word.encode('utf-8')
	if word.startswith(('a','e','i','o','u')):
		pub.send_multipart([b'vowels',data])
	if len(word)==5:
		pub.send_multipart([b'five',data])



