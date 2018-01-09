# from PIL import Image
# img=Image.open("O'Reilly_logo.png")
# img.format
# img.size
# img.mode

# import tkinter
# from PIL import Image,ImageTK

# main=thinter.TK()
# img=Image.open("O'Reilly_logo.png")
# tkiimg=ImageTK.PhotoImage(img)
# tkinter.Label(main,image=tkimg).pack()
# main.main.loop()

# from direct.showbase.ShowBase import ShowBase

# class MyApp(ShowBase):

# 	def __init__(self):
# 		ShowBase.__init__(self)

# 		#Load the environment model
# 		self.environ=self.loader.loadModel('models/environment')
# 		#Reparent the model to render
# 		self.environ.reparentTo(self.render)

# import matplotlib.pyplot as plot
# import matplotlib.image as image
# img=image.imread("O'Reilly_logo.png")
# plot.imshow(img)
# plot.show()

# import csv
# from collections import Counter

# counts=Counter()


# with open('zoo.csv','rt') as fin:
# 	cin=csv.reader(fin)
# 	for num,row in enumerate(cin):
# 		if num>0:
# 			counts[row[0]]+=int(row[-1])
# for animal,hush in counts.items():
# 	print("%10s %10s" %(animal,hush))

# import bubbles

# p=bubbles.Pipeline()
# p.source(bubbles.data_object('csv_source','zoo.csv',infer_fields=True))
# p.aggregate('animal','hush')
# p.pretty_print()

# def display_shapefile(name,iwidth=500,iheight=500):
# 	import shapefile
# 	from PIL import Image, ImageDraw
# 	r=shapefile.Reader(name)
# 	mleft,mbottom,mright,mtop=r.bbox
# 	#map units
# 	mwidth=mright-mleft
# 	mheight=mtop-mbottom
# 	#scale map units to image units
# 	hscale=iwidth/mwidth
# 	vscale=iheight/mheight
# 	img=Image.new('RGB',(iwidth,iheight),'white')
# 	draw=ImageDraw.Draw(img)
# 	for shape in r.shapes():
# 		pixels=[
# 		(int(iwidth-((mright-x)*hscale)),int((mtop-y)*vscale))
# 		for x,y in shape.points]
# 		if shape.shapeType==shapefile.POlYGON:
# 			draw.polygon(pixels,outline='black')
# 		elif shape.shapeType==shapefile.POLYLINE:
# 			draw.line(pixels,fill='black')
# 	image.show()
# if __name__ == '__main__':
# 	import sys
# 	display_shapefile(sys.argv[1],700,700)

#import math decimal
# from decimal import Decimal
# price=Decimal('19.99')
# tax=Decimal('0.06')
# total=price*(1+tax)
# print(total)
# penny=Decimal('0.01')
# print(total.quantize(penny))

# import numpy as np
# a=np.arange(10)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
# a=np.arange(7,11)
# print(a)
# a=np.arange(7,11,2)
# print(a)
# f=np.arange(2.0,9.8,0.3)
# print(f)
# g=np.arange(10,4,-1.5,dtype=np.float)
# print(g)

#zero(),ines(),random()
import numpy as np
# a=np.zeros((3,))
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
# b=np.zeros((2,4))
# print(b)
# print(b.ndim)
# print(b.shape)
# print(b.size)
# k=np.ones((3,5))
# print(k)
# m=np.random.random((3,5))
# print(m)
# a=np.arange(10)
# print(a)
# a=a.reshape(2,5)
# print(a)
# print(a.shape)
# a=a.reshape(5,2)
# print(a)
# a=np.arange(10)
# print(a[7])
# print(a[-1])
# a.shape=(2,5)
# print(a)
# print(a[1,2])
# a=np.arange(10)
# a=a.reshape(2,5)
# print(a)
# print(a[0,2:])
# print(a[-1,:3])
# a[:,2:4]=1000
# print(a)

from numpy import *

