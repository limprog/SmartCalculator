import cv2
import os
import numpy as np
from opencv_research.utils import new_def_cv

def base_preprocessing(old_path: str, new_path: str):
    file_list, list_of_dirs = new_def_cv.all_list_file(old_path)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    for files_dir, dir in zip(file_list, list_of_dirs):
        if not os.path.isdir(os.path.join(new_path, dir)):
            os.mkdir(os.path.join(new_path, dir))
        for file in files_dir:
            cv2.imwrite(os.path.join(new_path, file), preprocessing_img(cv2.imread(os.path.join(old_path, file))))


def preprocessing_img(img: np.ndarray):
    img = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)
    th = 255 - th
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)
    # th = 255 - th
    contours, _ = cv2.findContours(th, 1, 2)
    x1, y1, x2, y2 = get_crop_cord(contours)
    return img[y1:y2, x1:x2]


def get_crop_cord(cnts):
    xes1 = []
    ys1 = []
    xes2 = []
    ys2 = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        xes1.append(x)
        ys1.append(y)
        xes2.append(x+w)
        ys2.append(y+h)

    return min(xes1), min(ys1), max(xes2), max(ys2)



