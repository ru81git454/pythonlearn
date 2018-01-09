#coursera Chapter 8 - Lists
print('test') 
print([1,[5,6],7,'red'])
#fruit='banana'
#fruit[0]='B'
#print(fruit)
numbers=[3,41,12,9,74,15]
print (len(numbers))
print (max(numbers))
print (min(numbers))
print (sum(numbers))
print (sum(numbers)/len(numbers))
#not store only count once time
total=0
count=0
# while  True:
	# try:
	#  inp=input('enter value:')
	#  if inp=='done':break
	#  value=float(inp)
	#  total=total+value
	#  count+=1
	# except:
	#  pass
# average=total/count
# print('average:',average)
# numlist=list()
# #store and count
# while True:
# 	inp=input('enter a number:')
# 	if inp=='done':break
# 	value=float(inp)
# 	numlist.append(value)
# average=sum(numlist)/len(numlist)

# abc='with three words'
# stuff=abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])
# fhand=open('mbox-short.txt')
# for line in fhand:
# 	line=line.rstrip()
# 	if not line.startswith('From'):continue
# 	words=line.split()
# 	print(words[2])
email=words[1]
piece=email.split('@')
print(piece[1])