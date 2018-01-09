from twisted.internet import reactor,protocol

class KnockClient(protocol.Protocol):
	"""docstring for knockClient"""
	def connectionMade(self):
		self.transport.write(b'knock knock')
	def dataReceived(self,data):
		if data.startswith(b'who is there?'):
			response='Disappearing client'
			self.transport.write(response)
		else:
			self.transport.loseConnection()
			reactor.stop()
class KnockFactory(protocol.ClientFactory):
	protocol=KnockClient
def main():
	f=KnockFactory()
	reactor.connectTCP('localhost',8001,f)
	reactor.run()
if __name__ == '__main__':
	main()