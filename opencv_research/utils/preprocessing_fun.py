import cv2
import os
import numpy as np


def all_list_file(path: str):
    result = []
    list_of_dirs = os.listdir(path)
    for dir in list_of_dirs:
        full_path_files_dir = []
        files_dir = os.listdir(os.path.join(path, dir))
        for file in files_dir:
            full_path_files_dir.append(os.path.join(dir, file))
        result.append(full_path_files_dir)
    return result, list_of_dirs


def base_preprocessing(old_path: str, new_path: str):
    file_list, list_of_dirs = all_list_file(old_path)
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
    contours, _ = cv2.findContours(th, 1, 2)

    x, y, w, h = cv2.boundingRect(contours[-1])
    result = img[y:y+h, x:x+w]
    return result

