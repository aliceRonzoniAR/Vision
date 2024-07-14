# Vision
Project of Vision and Cognitive System - Università degli Studi di Padova 2023-2024

## TITLE OF THE PROJECT

Nowadays, the problem of correctly dividing and separating waste is present in our society and needs to be solved.
Thanks to object detection and recognition, two techniques that help us to detect and recognize objects, we can try to solve this problem. In this dissertation, the
main idea is to utilize two different models, compare the results and try to identify which of these models is more accurate but at the same time faster to identify the objects.
The models we took into consideration are: Faster R-CNN and YOLO. In particular for the Faster R-CNN model two different backbones will be considered: Resnet-50-FPN v2 and MobileNet-v3-large. On the other hand, YOLOv8 has been utilized as a benchmark.

## Description of the files
- *_json.py : these files are used to write the information about the images in a csv file. The output are two files: *_categories.txt (lists of all the categories in the dataset) and *_images_info.csv (information of the images present in the json file)
- YOLOv8.ipynb: run this file to obtain the results for the YOLOv8 model
- resnet.ipybb: run this file to obtain the results for the ResNET50 model
- mobile_net.ipybn: run this file to obtain the results for the MobileNet model
- mAP: to calculate the value of the mAP for the FasterRCNN models we used the following repository https://github.com/Cartucho/mAP
