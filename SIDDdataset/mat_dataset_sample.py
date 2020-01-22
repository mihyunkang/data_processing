import torch
import torchvision
import torchvision.transforms as transforms
import scipy.io as io
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
import numpy as np
import mat73
import h5py as h5
import h5py
import skimage 
import matplotlib
import os 
dir_list = ["SIDD_Medium_Raw"]
for d in dir_list:
    folder_list = os.listdir('../../../data/SIDD-dataset/'+d+'/Data/')
    for folder in folder_list:
        file_list  = os.listdir('../../../data/SIDD-dataset/'+d+'/Data/'+folder+'/')
        for f in file_list:
            if f[5:9] != "META":
                with h5py.File('../../../data/SIDD-dataset/'+d+'/Data/'+folder+'/'+f, 'r') as F:
                    #print(F.keys())
                    data = np.asarray(F['x'], dtype=np.float32)
                    print(data.shape)
                    #data = torch.from_numpy(data)
                    if f[5:7] == "GT":
                        #with skimage.external.tifffile.TiffWriter("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f[:-4]+'.tiff', bigtiff=True) as tif:
                            #tif.save(data)
                        #matplotlib.image.imsave("../../../data/SIDD-dataset/"+d+"_png"+"/GT/"+f[:-4]+'.png', data)
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f[:-4]+'.tiff', data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f[:-4]+'.png'))
                    else:
                        #with skimage.external.tifffile.TiffWriter("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f[:-4]+'.tiff', bigtiff=True) as tif:
                            #tif.save(data)
                        #matplotlib.image.imsave("../../../data/SIDD-dataset/"+d+"_png"+"/NOISY/"+f[:-4]+'.png', data)
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f[:-4]+'.tiff', data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f[:-4]+'.png'))





"""
 if f[5:7] == "GT":
                        with TiffWriter('temp.tif', bigtiff=True) as tif:
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f, data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f))
                    else:
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"/NOISY/"+f, data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f))

class MyDataset(Dataset):
    def __init__(self, mat_path):
        data = h5.File(mat_path, 'r')
        data = np.asarray(data)
        #data = mat73.loadmat(mat_path)
        self.images = torch.from_numpy(data)

    def __getitem__(self, index):
        x = self.images[index]
 
        return x

    def __len__(self):
        return len(self.images)

trainset = MyDataset(mat_path = "../../../data/SIDD-dataset/0001_GT_RAW_010.mat")
trainloader = torch.utils.data.DataLoader(trainset, batch_size=1,
                                          shuffle=True)
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()



# 학습용 이미지를 무작위로 가져오기
dataiter = iter(trainloader)
images, labels = dataiter.next()
print("이미지 보여주기 전")
# 이미지 보여주기
imshow(torchvision.utils.make_grid(images))
print("이미지 보여주기 후")"""