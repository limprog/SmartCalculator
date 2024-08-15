# In this file will be presented solution of task TEAM-9 solution and study will be conducted for the task TEAM-5

import os
import cv2
import numpy as np
from opencv_research.utils import new_def_cv
import random
import time
from tqdm import tqdm


list_classes = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', 'A', 'alpha', 'ascii_124', 'b', 'beta', 'C', 'cos', 'd', 'Delta', 'div', 'e', 'exists', 'f', 'forall', 'forward_slash', 'G', 'gamma', 'geq', 'gt', 'H', 'i', 'in', 'infty', 'int', 'j', 'k', 'l', 'lambda', 'ldots', 'leq', 'lim', 'log', 'lt', 'M', 'mu', 'N', 'neq', 'o', 'p', 'phi', 'pi', 'pm', 'prime', 'q', 'R', 'rightarrow', 'S', 'sigma', 'sin', 'sqrt', 'sum', 'T', 'tan', 'theta', 'times', 'u', 'v', 'w', 'X', 'y', 'z', '[', ']', '{', '}']
dir = "data_dir/new_data"

f = open('math.labels', "w")
for class_cv in list_classes:
    f.write(class_cv)
f.close()

print("Start")
for i in tqdm(range(500)):
    white_img = cv2.resize(cv2.imread("opencv_research/Wallpaper-1-1920x1080.jpg"), (0, 0), fx=0.5, fy=0.5)
    new_img = white_img.copy()
    h, w, _ = white_img.shape
    w_list = list(range(1, w+1))
    h_list = list(range(1, h+1))
    files, _ = new_def_cv.all_list_file("data_dir/data", True)
    list_files = [file for file in random.choices(files, k=random.randint(9, 17))]
    list_param = []
    for file in list_files:
        test = True
        class_name = file.split("/")[0]

        while test:
            img = cv2.imread(os.path.join("data_dir/data", file))
            resize_x_y = random.uniform(0.5, 2)
            img = cv2.resize(img, (0, 0), fx=resize_x_y, fy=resize_x_y)
            height, width, _ = img.shape
            x, y = random.choice(w_list), random.choice(h_list)
            if x + width <= w and y + height <= h:
                break

        new_img[y:y+height, x:x+width] = cv2.addWeighted(img, 1, new_img[y:y+height, x:x+width], 0, 0)
        list_param.append(f"{list_classes.index(class_name)} {(x+width/2) / w} {(y+height/2) / h} {width / w} {height / h}")
        del w_list[x:x+width-1]
        del h_list[y:y+height-1]
    cv2.imwrite(f"{dir}/{i}.png", new_img)
    f = open(f"{dir}/{i}.txt", "w")
    for text in list_param:
        f.write(text+"\n")
    f.close()

print("Finish")
