import redis
conn=redis.Redis()

topics=['m','p']
sub=conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
	if msg['type']=='message':
		cat=msg['channel']
		hat=msg['data']
		print('subscribe: %s wears a %s' %(cat,hat))