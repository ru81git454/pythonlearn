import xmlrpc.client
proxy=xmlrpc.client.ServerProxy('http://localhost:6790/')
num=7
result=proxy.double(num)
print('Double %s is %s' %(num,result))
