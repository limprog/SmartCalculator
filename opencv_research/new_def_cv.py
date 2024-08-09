import cv2
import numpy as np

def matrix_corol_like_img(img: np.ndarray, color: list):
    matrix_like_img = np.zeros_like(img)
    matrix_like_img[:] = color
    return matrix_like_img