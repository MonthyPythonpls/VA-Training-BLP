import os
import shutil

image_path = "C:/Users/admin/Downloads/annotations/p/"
annotaion_path = "c:/Users/admin/Downloads/annotations/p_labeled/"
save_path ="c:/Users/admin/Downloads/annotations/final_folder/"

try:
    os.makedirs(save_path, exist_ok=True)
except OSError as err:
    print(err)
else:
    print("Successfully created directory")

image_list=os.listdir(image_path)
annotation_list = os.listdir(annotaion_path)

image_names=[]
annot_names=[]
for i in image_list:
    names=os.path.splitext(i)[0]
    image_names.append(names)
for j in annotation_list:
    name=os.path.splitext(j)[0]
    annot_names.append(name)
#common = [i for i, j in zip(annot_names, image_names) if i == j]
list1_as_set = set(annot_names)
intersection = list1_as_set.intersection(image_names)
common = list(intersection)

for k in range(len(common)):
    x=common[k]
    x=x+'.xml'
    common[k]=x

for item in common:
    print(item)
    shutil.copy(image_path+item, save_path)