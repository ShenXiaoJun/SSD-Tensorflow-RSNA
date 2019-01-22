# encoding:utf-8
import os
import shutil
src_dir = '/home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_images_jpg/'

train_dir = '/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA-train/JPEGImages/'
test_dir = '/home/shenxj/SSD-Tensorflow-RSNA/VOC-RSNA-test/JPEGImages/'

test_num = 1000

src_list = sorted(os.listdir(src_dir))
for src_idx in range(0, len(src_list)):
    src_file_path = os.path.join(src_dir, src_list[src_idx])
    if src_idx < test_num:
        test_file_path = os.path.join(test_dir, src_list[src_idx])
        shutil.copy(src_file_path,  test_file_path)
    else:
        train_file_path = os.path.join(train_dir, src_list[src_idx])
        shutil.copy(src_file_path,  train_file_path)
