# from datetime import date
# today=date.today()
# today=str(today)
# with open('today.txt','wt') as fout:
# 	fout.write(today)
# with open('today.txt','rt')	as fin:
# 	today_string=fin.read()
# from datetime import datetime
# print(today_string)
# fmt='%Y-%m-%d'
# datetime.strptime(today_string,fmt)
import multiprocessing
def now(seconds):
	from datetime import datetime
	from time import sleep
	sleep(seconds)
	print('wait',seconds,'seconds,time is ',datetime.utcnow())
if __name__ == '__main__':
	import random
	for n in range(3):
		seconds=random.random()
		proc=multiprocessing.Process(target=now,args=(seconds,))
		proc.start()
from datetime import date		
mydate=date(1993,3,6)
print(mydate.isoweekday())
from datetime import timedelta
partyday=mydate+timedelta(days=10000)
print(partyday)
