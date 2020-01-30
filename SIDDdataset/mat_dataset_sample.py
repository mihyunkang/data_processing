import numpy as np
import h5py
import skimage 
import os 

dir_list = ["SIDD_Medium_Raw"]

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

for d in dir_list:
    make_dir("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"):
    make_dir("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/")
    folder_list = os.listdir('../../../data/SIDD-dataset/'+d+'/Data/')
    for folder in folder_list:
        file_list  = os.listdir('../../../data/SIDD-dataset/'+d+'/Data/'+folder+'/')
        for f in file_list:
            if f[5:9] != "META":
                # only GT, NOISY
                with h5py.File('../../../data/SIDD-dataset/'+d+'/Data/'+folder+'/'+f, 'r') as F:
                    data = np.asarray(F['x'], dtype=np.float32)
                    data = np.transpose(data, (1,0)) #change w, h -> h, w

                    # seperate dir
                    if f[5:7] == "GT":
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f[:-4]+'.tiff', data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/GT/"+f[:-4]+'.tiff'))
                    else: # NOISY
                        skimage.external.tifffile.imsave("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f[:-4]+'.tiff', data)
                        print("filename {} image save".format("../../../data/SIDD-dataset/"+d+"_tiff"+"/NOISY/"+f[:-4]+'.tiff'))

