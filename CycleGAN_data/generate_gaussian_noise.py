import numpy as np

def make_gaussian_noise(height, width, std):
    img_noisy = np.zeros((h,w), dtype=np.float32)
    for h in range(height):
        