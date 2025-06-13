import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_url = 'https://imgs.search.brave.com/Ee9YYXlXYvYnNLY1R0Jg6VJy470XXDTRYAdQtMGFWZ0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDc2/MjM5NDk1L3Bob3Rv/L3RyYWZmaWMtamFt/LW9uLXJ1c2gtaG91/ci1pc3RhbmJ1bC5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/R2V5bHdRUUpmaENs/QkI3MTdmXzhoTGNP/aUFPTnZsWHpMMl9p/Y1lXazJ1MD0'

results = model(img_url)
print(results)

rendered_img = results.render()[0]

cv2.imshow("YOLO Output", rendered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()