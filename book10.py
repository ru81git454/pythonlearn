# fout=open('oop.txt','wt')
# print('oops,i created afile.',file=fout)
# fout.close()

# with open('oop.txt','wt') as fout:
# 	print('oops,i created afile.',file=fout)

# name-'oop.txt'
# os.path.isfile(name)
# import multiprocessing
# import os
# def do_this(what):
# 	whoami(what)
# def whoami(what):
# 	print("process  %s says: %s" %(os.getpid(),what))
# if __name__ == '__main__':
# 	whoami('i am  the main program')
# 	for n in range(4):
# 		p=multiprocessing.Process(target=do_this,args=('i am function %s' %n,))

# 		p.start()
# import multiprocessing
# import time 
# import os
# def whoami(name):
# 	print('i am %s ,in process %s' %(name,os.getpid()))
# def loopy(name):
# 	whoami(name)
# 	start=1
# 	stop=10000
# 	for num in range(start,stop):
# 		print('\tNumber %s of %s. honk!'%(num,stop))
# 		time.sleep(1)
# if __name__ == '__main__':
# 	whoami('main')
# 	p=multiprocessing.Process(target=loopy,args=("loopy",))
# 	p.start()
# 	time.sleep(5)
# 	p.terminate()

import locale
from datetime import date
halloween=date(2014,10,31)
for lang_country in ['en_us','de_at',]:
	locale.setlocale(locale.LC_TIME,lang_country)
	print(halloween.strftime('%A %B %d'))
