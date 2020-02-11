import numpy as np
from skimage.external.tifffile import imsave, imread
import torch


def make_gaussian_noise(height, width, std):
    noise_img = np.zeros((1,height,width), dtype=np.float32)
    for h in range(height):
        for w in range(width):
            # avg : 0, std : 1
            std_norm = np.random.normal() 
            # avg : 0, std : std
            random_noise = std*std_norm
            noise_img[0][h][w] = random_noise 
    return noise_img

def save_tiff(path, np_image):
    imsave(path, np_image)
    print("{} save".format(path))

noise1 = make_gaussian_noise(512, 512, 0.1)
noise2 = make_gaussian_noise(512, 512, 0.1)
noise1 = torch.from_numpy(noise1)
noise2 = torch.from_numpy(noise2)
noise = torch.cat([noise1,noise2],dim=0)
print(noise.shape)
save_tiff("./01.tiff", noise)
