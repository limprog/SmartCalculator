import cv2
import numpy as np
import os

def matrix_coral_like_img(img: np.ndarray, color: list):
    matrix_like_img = np.zeros_like(img)
    matrix_like_img[:] = color
    return matrix_like_img


def all_list_file(path: str, param: bool = False):
    result = []
    list_of_dirs = os.listdir(path)
    for dir in list_of_dirs:
        if param:
            files_dir = os.listdir(os.path.join(path, dir))
            for file in files_dir:
                result.append(os.path.join(dir, file))
        else:
            full_path_files_dir = []
            files_dir = os.listdir(os.path.join(path, dir))
            for file in files_dir:
                full_path_files_dir.append(os.path.join(dir, file))
            result.append(full_path_files_dir)
    return result, list_of_dirs


