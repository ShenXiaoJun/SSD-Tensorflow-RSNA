# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
import csv
import string

def indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def make_xml(filename, path, label_num, label):
    annotation_node = ET.Element('annotation')

    folder_node = ET.SubElement(annotation_node, 'folder')
    folder_node.text = 'RSNA'

    filename_node = ET.SubElement(annotation_node, 'filename')
    filename_node.text = filename

    path_node = ET.SubElement(annotation_node, 'path')
    path_node.text = path + filename + ".jpg"

    source_node = ET.SubElement(annotation_node, 'source')
    database_node = ET.SubElement(source_node, 'database')
    database_node.text = 'RSNA'

    size_node = ET.SubElement(annotation_node, 'size')
    width_node = ET.SubElement(size_node, 'width')
    width_node.text = '1024'
    height_node = ET.SubElement(size_node, 'height')
    height_node.text = '1024'
    depth_node = ET.SubElement(size_node, 'depth')
    depth_node.text = '1'

    segmented_node = ET.SubElement(annotation_node, 'segmented')
    segmented_node.text = '0'

    for label_idx in range(0, label_num):
        object_node = ET.SubElement(annotation_node, 'object')
        name_node = ET.SubElement(object_node, 'name')
        name_node.text = 'opacity'
        pose_node = ET.SubElement(object_node, 'pose')
        pose_node.text = 'Unspecified'
        truncated_node = ET.SubElement(object_node, 'truncated')
        truncated_node.text = '0'
        difficult_node = ET.SubElement(object_node, 'difficult')
        difficult_node.text = '0'
        bndbox_node = ET.SubElement(object_node, 'bndbox')
        xmin_node = ET.SubElement(bndbox_node, 'xmin')
        xmin_node.text = str(label[0 + label_idx*4])
        ymin_node = ET.SubElement(bndbox_node, 'ymin')
        ymin_node.text = str(label[1 + label_idx*4])
        xmax_node = ET.SubElement(bndbox_node, 'xmax')
        xmax_node.text = str(label[2 + label_idx*4])
        ymax_node = ET.SubElement(bndbox_node, 'ymax')
        ymax_node.text = str(label[3 + label_idx*4])
	
    indent(annotation_node)    # 增加对根节点的额外处理

    tree = ET.ElementTree(annotation_node)
    tree.write(filename + ".xml")

os.chdir("/home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_labels/")
labels_file = "/home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_labels.csv"
pic_dir     = "/home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_images_jpg"
pic_list = sorted(os.listdir(pic_dir))
for pic_idx in range(0, len(pic_list)):
    pic_name = pic_list[pic_idx]
    pic_path = os.path.join(pic_dir,pic_name)
    pic_name_only = pic_name.split('.')[0]
	
    with open(labels_file, 'r') as labels_csv:
        labels_reader = csv.DictReader(labels_csv)
        label_num = 0
        label = []
        for row in labels_reader:
            if pic_name_only in row.get('patientId'):
                if row.get('Target') == "0":
                    continue                
                label_x = string.atoi(row.get('x').split('.')[0])
                label_y = string.atoi(row.get('y').split('.')[0])
                label_width  = string.atoi(row.get('width').split('.')[0])
                label_height = string.atoi(row.get('height').split('.')[0])
                label.append(label_x)
                label.append(label_y)
                label.append(label_x + label_width)
                label.append(label_y + label_height)
                label_num += 1

    print("pic_name_only:%s, label_num:%d"%(pic_name_only, label_num))
    for label_idx in range(0, label_num):
        print("    [%s]: %d, %d, %d, %d"% (pic_name_only, \
            label[0 + label_idx*4], label[1 + label_idx*4], \
            label[2 + label_idx*4], label[3 + label_idx*4]))

    make_xml(pic_name_only, pic_dir, label_num, label)