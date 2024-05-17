import os
import cv2
import torch
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from shapely.geometry import Polygon
import numpy as np
from extract import extract_function
from xml_to_txt import xml_to_txt_function

extract_function()
xml_to_txt_function()

def create_anno_xml(file_path, bboxes):
    root = Element('annotations')
    for bbox in bboxes:
        annotation = SubElement(root, 'annotation')
        SubElement(annotation, 'bbox').text = str(bbox)
    tree = ElementTree(root)
    tree.write(file_path)

def check_intrusion(ROI, bbox):
    roi_poly = Polygon(ROI)
    bbox_poly = Polygon([(bbox[0], bbox[1]), (bbox[2], bbox[1]), (bbox[2], bbox[3]), (bbox[0], bbox[3])])
    return roi_poly.intersects(bbox_poly)

def process_images(image_dir, ROI, model):
    bboxes = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(image_dir, filename))
            results = model(img)
            for *xyxy, conf, cls in results.xyxy[0]:
                if int(cls) == 0:
                    bbox = tuple(map(int, xyxy))
                    bboxes.append(bbox)
                    if check_intrusion(ROI, bbox):
                        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                        cv2.putText(img, 'Intrusion Detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Draw the ROI polygon
                    cv2.polylines(img, [np.array(ROI)], True, (255, 0, 0), 2)
                    
                    cv2.imwrite(os.path.join(image_dir, 'output_' + filename), img)
                    create_anno_xml(os.path.join(image_dir, 'annotations.xml'), bboxes)

def main():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    ROI = [(230, 230), (365, 300), (350, 357), (194, 358)]
    image_dir = "C:/Users/admin/Downloads/annotations/vid2_frames"
    process_images(image_dir, ROI, model)

if __name__ == "__main__":
    main()