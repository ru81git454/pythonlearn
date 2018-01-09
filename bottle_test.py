
import requests
r=requests.get('http://localhost:9999/echo/pei')
if r.status_code==200 and r.text=='say hello to my little friend:pei!':
	print ('it worked! that almost never happens')
else:
	print('argh,got this:',r.text)