ndex=0
for file in /home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_images/*
do
    echo "$index"
    echo $file
    cp $file /home/shenxj/SSD-Tensorflow-RSNA/RSNA/stage_1_train_images_5k/
    ((index++))
    [ $index -eq 5000 ] && break
done
