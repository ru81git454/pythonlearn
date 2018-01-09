# #8.1 8.2
# test1='this is a test of the emergency test system'
# len(test1)
# outfile=open('text.txt','wt')
# outfile.write(test1)
# outfile.close()
# with open('text.txt','wt') as outfile:
# 	 outfile.write(test1)
# with open('text.txt','rt') as infile:
# 	test2=infile.read()
# print(test1==test2)

# #8.3
# import csv
# text='''a,b
# c,d
# e,f'''
# with open('test.csv','wt') as writefile:
# 	writefile.write(text)
# with open('test.csv','rt') as infile:
# 	books=csv.DictReader(infile)
# 	for book in books:
# 		print(books)

# #8.5
# text='''title,author,year
# a,b,c 
# d,e,f'''
# with open('book.csv','wt') as outfile:
# 	 outfile.write(text)
# import sqlite3
# db=sqlite3.connect('books.db')
# curs=db.cursor()
# #curs.execute('''create table book(title text,author text ,year int)''')
# #db.commit()

# import csv
# import sqlite3
# ins_str='insert into book values(?,?,?)'
# with open('book.csv','rt') as infile:
#  books=csv.DictReader(infile)
#  for book in books:
#  	curs.execute(ins_str,(book['title'],book['author'],book['year']))
# #8.8
# sql='select title from book order by title asc'
# for row in db.execute(sql):
# 	print(row)
# for row in db.execute(sql):
# 	print(row[0])
# sql='''select title from book order by
# case when (title like "the %") then substr(title,5) else title end'''
# for row in db.execute(sql):
# 	print(row[0])

# #8.9
# for row in db.execute('select * from book order by year'):
# 	print(row)
# for row in db.execute('select * from book order by year'):
# 	print(*row,sep=',')
# # 8.10
# import sqlalchemy
# conn=sqlalchemy.create_engine('sqlite:///books.db')
# sql='select title from book order by title asc'
# rows=conn.execute(sql)
# for row in rows:
# 	print(row)

import redis
conn=redis.Redis()
conn.delete('test')
print(conn.hmset('test',{'count':1,'name':'fester bestertester'}))
print(conn.hgetall('test'))
print(conn.hincrby('test','count',3))
print(conn.hget('test',3))