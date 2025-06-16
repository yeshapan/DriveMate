import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time 
import uuid

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

IMAGES_PATH = os.path.join('../', 'data', 'images')
print(IMAGES_PATH)
labels = ["awake", "drowsy"]
number_imgs = 20

cap = cv2.VideoCapture(0)

for label in labels:
    print(f'Collecting images for {label}')
    time.sleep(5)

    for img_num in range(number_imgs):
        print(f'Collecting image {img_num} for {label}')

        ret, frame = cap.read()

        imgname = os.path.join(IMAGES_PATH, label+"."+str(uuid.uuid1())+".jpg")

        cv2.imwrite(imgname, frame)
        print(f'Image saved as {imgname}')

        cv2.imshow('Image collection', frame)

        time.sleep(2)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
