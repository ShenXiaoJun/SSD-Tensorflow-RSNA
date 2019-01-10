# encoding:utf-8
import os
rootdir = '../demo'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
	path = os.path.join(rootdir,list[i])
	if os.path.isfile(path):
		print path

names = sorted(list)
for i in range(0, len(list)):
	print names[i]