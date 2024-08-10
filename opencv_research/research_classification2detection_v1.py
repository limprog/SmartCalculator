# In this file will be presented solution of task TEAM-7 solution and study will be conducted for the task



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
gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 7, 80, 80)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 17, 2)
mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((3, 3)))
result = cv2.bitwise_and(white_like_img, img)
# result = cv2.bitwise_and(img, img, mask=thresh)

cv2.imshow("input", img)
cv2.imshow("output", thresh)
cv2.imshow("research", result)
cv2.waitKey(0)