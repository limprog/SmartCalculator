import os
import cv2
import numpy as np
from new_def_cv import *
img = cv2.imread(os.path.join("data/classification2detection/photo_2024-08-09_20-49-42.jpg"))
img = cv2.resize(img, (0,0), fx=0.7, fy=0.7)
white_like_img = matrix_corol_like_img(img, [255, 255, 255])
print(white_like_img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([20, 0, 0])
upper_blue = np.array([50, 90, 170])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(img, white_like_img, mask=mask)
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
cv2.imshow("input", img)
cv2.imshow("output", hsv)
cv2.imshow("research", mask)
cv2.waitKey(0)