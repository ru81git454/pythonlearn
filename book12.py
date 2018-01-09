#unitest test_cap.py
# import unittest
# import cap

# class TestCap(unittest.TestCase):
# 	def setup(self):
# 		pass
# 	def tearDown(self):
# 		pass
# 	def test_one_word(self):
# 		text='duck'
# 		result=cap.just_do_it(text)
# 		self.assertEqual(result,'Duck')
# 	def test_multiple_words(self):
# 		text='a varitable flock of ducks'
# 		result=cap.just_do_it(text)
# 		self.assertEqual(result,'A Varitable Flock Of Ducks')
# 	def test_words_with_apostrophes(self):
# 		text="I'm fresh out of ideas"
# 		result=cap.just_do_it(text)
# 		self.assertEqual(result,"I'm Fresh Out Of Ideas")
# 	def test_words_with_quotes(self):
# 		text="\"You're despicable,\" said Daffy Duck"
# 		result=cap.just_do_it(text)
# 		self.assertEqual(result,"\"You're Despicable,\" Said Daffy Duck")

# if __name__ == '__main__':
# 	unittest.main()

#test_cap_nose.py


# import cap
# from nose.tools import eq_

# def test_one_word():
# 	text='duck'
# 	result=cap.just_do_it(text)
# 	eq_(result,'Duck') 
# def test_multiple_words():
# 	text='a veritable flock of ducks'
# 	result=cap.just_do_it(text)
# 	eq_(result,'A Veritable Flock Of Ducks')
# def test_words_with_apostrophes():
# 	text="I'm fresh out of ideas"
# 	result=cap.just_do_it(text)
# 	eq_(result,"I'm Fresh Out Of Ideas")
# def test_words_with_quotes():
# 	text="\"You're despicable,\" said Daffy Duck"
# 	result=cap.just_do_it(text)
# 	eq_(result,"\"You're Despicable,\" Said Daffy Duck")

#debug


# def func(*args,**kwargs):
# 	print(vars())
# func(1,2,3)

# def dump(func):
# 	'print input argument and output values'
# 	def wrapped(*args,**kwargs):
# 		print('function names:%s'%func.__name__)
# 		print('inpput arguments: %s'%' '.join(map(str,args)))
# 		print('input keyword arguments:%s'%kwargs.items())
# 		output=func(*args,**kwargs)
# 		print('output:',output)
# 		return output
# 	return wrapped

# #decorator

# @dump
# def double(*args,**kwargs):
# 	"double every argument"
# 	output_list=[2*arg for arg in args]
# 	output_dict={k:2*v for k,v in kwargs.items()}
# 	return output_list,output_dict
# if __name__ == '__main__':
# 	output=double(3,5,first=100,next=98.6,last=-40)

# def process_cities(filename):
# 	with open(filename,'rt') as file:
# 		for line in file:
# 			line=line.strip()
# 			if 'quit' == line.lower():
# 				return
# 			country,city=line.split(',')
# 			city=city.strip()
# 			country=country.strip()
# 			print(city.title(),country.title(),sep=',')
# if __name__ == '__main__':
# 	import sys
# 	process_cities(sys.argv[1])

#logging


# import logging
# logging.debug('look like rain')
# logging.info('and hail')
# logging.warn('did i hear thunder')
# logging.error('was that lightning')

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('it is raining again')
# logging.info('with hail the size of hailstones')
# import logging
# logging.basicConfig(level='DEBUG')
# logger=logging.getLogger('bunyan')
# logger.debug('timber!')
# import logging
# logging.basicConfig(level='DEBUG',filename='blue_ox.log')
# logger=logging.getLogger('bunyan')
# logger.debug('where is my axe')
# logger.warn('i need my axe')

# import logging
# fmt='%(asctime)s %(levelname)s %(lineno)s %(message)s'
# logging.basicConfig(level='DEBUG',format=fmt)
# logger=logging.getLogger('bunyan')
# logger.error('where is my other plaid shirt?')

from timeit import repeat
print(repeat('num=5;num*=2',repeat=3))

from timeit import timeit
def make_list_1():
	result=[]
	for value in range(1000):
		result.append(value)
	return result
def make_list_2():
	result=[value for value in range(1000)]
	return result 
print('make_list_1 takes',timeit(make_list_1,number=1000),'seconds')

print('make_list_2 takes',timeit(make_list_2,number=1000),'seconds')
