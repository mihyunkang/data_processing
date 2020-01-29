import numpy as numpy
from PIL import Image
import os

final_path_dir = "../../CycleGAN/paired512resultAvg10/"
base_path = "../../CycleGAN/paired512result_"
if not os.path.exists(final_path_dir):
    os.makedirs(final_path_dir)

path1 = base_path+str(0)+'/test_latest/FakeClean/'
file_list =os.listdir(path1)
for f in file_list:
    img1 = Image.fromarray(path1+f)
    img1 = (img1)/10
    for i in range(1,10):
        path2 = base_path+str(i)+'/test_latest/FakeClean/'
        if f in os.listdir(path2):
            img2 = Image.fromarray(path2+f)
            img1 +=(img2)/10
    img1.save(final_path_dir+f)
    print("{} is saved".format(final_path_dir+f))
            

