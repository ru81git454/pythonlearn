# import urllib.request as ur
# url='https://www.youtube.com/?gl=TW&hl=zh-TW'
# conn=ur.urlopen(url)
# print(conn)
# data=conn.read()
# print(conn.status)
# print(conn.getheader('Content-Type'))
# for key,value in conn.getheaders():
# 	print(key,value)
# bottle
# import requests
# r=requests.get(url)
# print(r)
# print(r.text)
# from bottle import route,run
# @route('/')
# def home():
# 	return "it isn't fancy,but it is my home page"

# run(host='localhost', port=9999)

# from bottle import route,run,static_file
# @route('/')
# def main():
# 	return static_file('index.html',root='.')
# run(host='localhost', port=9999)

# from bottle import route,run,static_file
# @route('/')
# def home():
# 	return static_file('index.html',root='.')
# @route('/echo/<thing>')
# def echo(thing):
# 	return"say hello to my little friend: %s!" % thing
# run(host='localhost', port=9999)

# import requests
# r=requests.get('http://localhost:9999/echo/pei')
# if r.status_code==200 and \
#  r.text=='say hello to my little friend:pei!':
#   print ('it worked! that almost never happens')
# else:
# 	print('argh,got this:',r.text)

# flask
from flask import Flask
app=Flask(__name__,static_folder='.', static_url_path='')

@app.route('/')
def home():
	return app.send_static_file('index.html')
@app.route('/echo/<thing>')
def echo(thing):
	return"say hello to my little friend: %s!" % thing

app.run(port=9999, debug=True)

