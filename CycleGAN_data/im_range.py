from skimage.external.tifffile import imsave, imread
import os


result_dir = "../../../data/CycleGAN-data/result_mayo_blur_gaussian/128_longskip_mstd_r9/128_longskip_mstd_r9/test_latest/FakeClean/"


result_list = sorted(os.listdir(result_dir))

for i in range(len(result_list)):
    im = imread(result_dir+result_list[i])
    im[im < 0] = 0
    im[im > 1] = 1
    print(result_dir+result_list[i])
    imsave(result_dir+result_list[i], im)
    