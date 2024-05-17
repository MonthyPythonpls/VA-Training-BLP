import os
import cv2
import torch
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import numpy as np
from shapely.geometry import LineString, box, polygon, Point
import time
from scipy.spatial.distance import cdist


def create_anno_xml(filename, ROI, counter):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    root = ET.Element("annotation")
    ET.SubElement(root, "ROI").text = str(ROI)
    ET.SubElement(root, "counter").text = str(counter)
    tree = ET.ElementTree(root)
    tree.write(filename.replace('.jpg', '.xml'))

def check_intrusion(ROI, bbox, prev_center):
    roi_line = LineString(ROI)
    curr_center = Point((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2)
    bbox_line = LineString([prev_center, curr_center])
    return roi_line.intersects(bbox_line)

def process_images(image_dir, ROI, model):
    # Read the counter from a file
    counter = 0

    prev_centers = []  # Keep track of the previous centers of the bounding boxes

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(image_dir, filename))
            img_copy = img.copy()  # Clone the image

            results = model(img)
            curr_centers = []
            bboxes = []
            intrusion_detected = False
            for *xyxy, conf, cls in results.xyxy[0]:

                if int(cls) == 2 and conf > 0.4:
                    bbox = tuple(map(int, xyxy))
                    bboxes.append(bbox)
                    center = [int((bbox[0] + bbox[2]) / 2), int((bbox[1] + bbox[3]) / 2)]
                    curr_centers.append(center)
                    if prev_centers:
                        closest_prev_center = prev_centers[cdist([center], prev_centers).argmin()]
                        if check_intrusion(ROI, bbox, Point(*closest_prev_center)):
                            intrusion_detected = True
                    cv2.drawMarker(img_copy, center, (0, 0, 255), cv2.MARKER_CROSS, 10, 1)
        if intrusion_detected:
            counter += 1
        prev_centers = curr_centers

            # Draw the ROI and counter on the cloned image
        cv2.polylines(img_copy, [np.array(ROI)], True, (0, 255, 0), 2)
        cv2.putText(img_copy, f'Counter: {counter}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imwrite(os.path.join(image_dir, 'annotated_' + filename), img_copy)

        create_anno_xml(os.path.join(image_dir, filename.replace('.jpg', '.xml')), bboxes, counter)

def main():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    ROI = [(220, 190), (580, 265)]
    image_dir = 'C:/Users/admin/Downloads/annotations/vid2_frames/'
    process_images(image_dir, ROI, model)

if __name__ == '__main__':
    main()