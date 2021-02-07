import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt

def slicer(num_grids, path):
    image_list = []
    for filename in glob.glob(path + '*.png'):
        im = np.array(Image.open(filename))
        image_list.append(im)
    
    num_grids = 8
    image_set = []
    for img in image_list:
        grids = []
        if img.shape == (512,512,3):
            for i in range(num_grids):
                y = i * int(512/num_grids)
                for j in range(num_grids):
                    x = j * int(512/num_grids)
                    grids.append(img[y:y + 64,x:x + 64])
            image_set.append(grids)
    return image_set

def importer(path):
    image_list = []
    for filename in glob.glob(path + '*.png'):
        im = np.array(Image.open(filename))
        image_list.append(im)
        
    return image_list