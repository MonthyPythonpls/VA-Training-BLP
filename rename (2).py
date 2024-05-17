import os
# import cv2 as cv

path = "c:/Users/admin/Downloads/annotations/p/"
dirs = os.listdir(path)

def rename():
    i = 1
    for item in dirs:
        if os.path.isfile(path+item):
            dst = "Amlichikuwadi_"+str(i)+".jpg"
            src = path+item
            dst = path+dst
            os.rename(src,dst)
            i+=1
    print('success')
    print(i)

rename()