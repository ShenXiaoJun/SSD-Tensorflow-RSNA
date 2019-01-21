# -*- coding:utf-8 -*-
import os
import random
import csv

trainval_percent = 0.66
train_percent = 0.5
xmlfilepath = '/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA/Annotations'
#txtsavepath = 'ImageSets\Main'
#total_xml = os.listdir(xmlfilepath)
total_xml = sorted(os.listdir(xmlfilepath))

num = len(total_xml)
list = range(num)
tv = int(num*trainval_percent)
tr = int(tv*train_percent)
trainval = random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA/ImageSets/Main/trainval.txt', 'w')
ftest     = open('/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA/ImageSets/Main/test.txt', 'w')
ftrain    = open('/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA/ImageSets/Main/train.txt', 'w')
fval      = open('/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA/ImageSets/Main/val.txt', 'w')

labels_file = "/home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_labels.csv"

for i in list:
    name = total_xml[i][:-4]
    target = 0
    with open(labels_file, 'r') as labels_csv:
        labels_reader = csv.DictReader(labels_csv)        
        for row in labels_reader:
            if name in row.get('patientId'):
                if row.get('Target') == "0":
                    target = -1
                else:
                    target = 1
    if i in trainval:
        ftrainval.write(name + " " + str(target) + "\n")        
        if i in train:
            ftrain.write(name + " " + str(target) + "\n")
            print("name:%s, target:%d, type:train"%(name, target))
        else:
            fval.write(name + " " + str(target) + "\n")
            print("name:%s, target:%d, type:val"%(name, target))
    else:
        ftest.write(name + " " + str(target) + "\n")
        print("name:%s, target:%d, type:test"%(name, target))

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
