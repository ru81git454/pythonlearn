import multiprocessing as mp
def washer(dishes,output):
	for dish in dishes:
		print('washing',dish,'dish')
		output.put(dish)

def dryer(input):
	while True:
		dish=input.get()
		print('drying',dish,'dish')

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

'''twist'''
from twisted.internet import protocol,reactor

class Knock(protocol.Protocol):
	def dataReceived(self,data):
		print('client:', str(data))
		if data.startswith(b'knock knock'):
			response='who is there?'
		else:
			response=data+'who?'
		print('server:',response)
		self.transport.write(b"knock")
class KnockFactory(protocol.Factory):
	def buildProtocol(self,addr):
		return Knock()
reactor.listenTCP(8001,KnockFactory())
reactor.run()
