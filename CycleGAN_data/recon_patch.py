import os
import glob
from PIL import Image

from skimage.external.tifffile import imsave, imread

target_dir = "/data/mihyun/workspaces/CycleGAN/results2/denoising_cyclegan/test_latest/images/"
for i in range(526):
    files = glob.glob(target_dir+"L506-{:03d}*_fake_A.png".format(i))
    print(files)
    new_image = Image.new('F',(512,512))
    for j, f in enumerate(sorted(files)):
        image = imread(f)
        filename = os.path.basename(f)
        file_info = filename.split('-')
        patient_id = file_info[0]
        slice_num = file_info[1]
        h = int(file_info[2])
        w = int(file_info[3].split('_')[0])
        print("{} {} {} {}".format(patient_id, slice_num, h, w))
        # f.split('/')[-1]
        new_image.paste(image,(h, w))
    imsave("/data/mihyun/workspaces/CycleGAN/results2/denoising_cyclegan/test_latest/images_merge_fake/L506-{0}.tiff".format(i),new_image)
    print("save file L506-{0}_fake".format(slice_num))