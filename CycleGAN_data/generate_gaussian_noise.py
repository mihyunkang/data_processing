import numpy as np
from skimage.external.tifffile import imsave, imread

def make_gaussian_noise(height, width, std):
    noise_img = np.zeros((height,width), dtype=np.float32)
    for h in range(height):
        for w in range(width):
            # avg : 0, std : 1
            std_norm = np.random.normal() 
            # avg : 0, std : std
            random_noise = std*std_norm
            noise_img[h][w] = random_noise 
    return noise_img

def save_tiff(path, np_image):
    imsave(path, np_image)
    print("{} save".format(path))

save_tiff("./1.tiff", make_gaussian_noise(512, 512, 1))