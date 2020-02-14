import os, sys
import glob
import numpy as np

from skimage.external.tifffile import imsave, imread

GT_dir = "../../../data/CycleGAN-data/datasets/denoising_full/testA/"
GT_list = sorted(os.listdir(GT_dir))

def calculate_mean_std():
    
    mean = 0.
    std = 0.
    nb_samples = 0.
    for f in GT_list:
        data = imread(GT_dir+f)
        mean += np.mean(data)
        std += np.std(data)

    mean /= len(GT_list)
    std /= len(GT_list)

    # print("mean.size():", mean.size())
    # print("std.size():", std.size())
    return mean, std


print(calculate_mean_std())

"""
full_1mm trainA (0.2974482899666286, 0.3435000343241166)
"""