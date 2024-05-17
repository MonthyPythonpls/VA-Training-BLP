import cv2
import math
import os



def extract_function():
    imagesFolder = "C:/Users/admin/Downloads/annotations/vid2_frames/"
    counter = 0
    listing = os.listdir("C:/Users/admin/Downloads/annotations/vids/")
    print(listing)

    for vid in listing:
        vid = "C:/Users/admin/Downloads/annotations/vids/" + vid
        cap = cv2.VideoCapture(vid)
        counter += 1
        # frameRate = cap.get(5) #frame rate
        if not cap.isOpened():
            print("Error: Could not open video.")

        while (cap.isOpened()):
            frameId = cap.get(1)  # current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(10) == 0):
                filename = imagesFolder + "/image_" + str(int(counter)) + "_" + str(int(frameId)) + ".jpg"
                cv2.imwrite(filename, frame)
        cap.release()
        print("Done!")

extract_function()