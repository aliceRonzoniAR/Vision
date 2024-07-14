import json
import numpy as np
import pandas as pd

PATH_TEST_JSON = "./test/_annotations.coco.json"

f = open(PATH_TEST_JSON)
data = json.load(f)

i = 0

## CATEGORIES

with open("test_categories.txt", "w") as text_file:
    for cat in data['categories']:
        if cat['name'] != "trash-detection":
            text_file.write("\"" + cat['name'] + "\"," )
            i += 1

# print(i)
            
## IMAGE INFORMATION

imgs_list = []

for img in data['images']:
    imgs_dict = {"img_id":0, "file_name":"none", "height":0, "width":0}

    imgs_dict['img_id'] = img['id']
    imgs_dict['file_name'] = img['file_name']
    imgs_dict['height'] = img['height']
    imgs_dict['width'] = img['width']

    imgs_list.append(imgs_dict)


## ASSOCIATE TO EACH IMAGE THE BOUNDING BOX AND THE TYPE ON OBJECT DETECTED
    
ann_list = []

for row in data['annotations']:
    ann_dict = {}

    ann_dict['ann_id'] = row["id"]
    ann_dict["image_id"] = row["image_id"]
    ann_dict["category_id"] = row["category_id"]
    ann_dict["x1"] = row["bbox"][0]
    ann_dict["y1"] = row["bbox"][1]
    ann_dict["w"] = row["bbox"][2]
    ann_dict["h"] = row["bbox"][3]

    ann_list.append(ann_dict)

df1 = pd.DataFrame(imgs_list, columns =['img_id', 'file_name', 'height', 'width'])
print(df1.head())

df2 = pd.DataFrame(ann_list, columns =['ann_id', 'image_id', 'category_id', 'x1', 'y1', 'w', 'h'])
print(df2.head())

result = pd.merge(df2, df1, how='left', left_on='image_id', right_on='img_id')
result = result.drop(columns=['img_id'])

print(result.head())

result.to_csv('test_images_info.csv', index=False)