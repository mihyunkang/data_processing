import os 
from PIL import Image

path = '../../../data/CycleGAN-data/result/add_pixelwiseloss_128_cat_noise/patch128_pixelwiaeloss_concatNoise_512/test_latest/images/'
if not os.path.exists(path+'../FakeClean/'):
    os.makedirs(path+'../FakeClean/')
if not os.path.exists(path+'../RealClean/'):
    os.makedirs(path+'../RealClean/')
if not os.path.exists(path+'../FakeNoise/'):
    os.makedirs(path+'../FakeNoise/')
if not os.path.exists(path+'../RealNoise/'):
    os.makedirs(path+'../RealNoise/')
if not os.path.exists(path+'../FakeFakeClean/'):
    os.makedirs(path+'../FakeFakeClean/')
if not os.path.exists(path+'../FakeFakeNoise/'):
    os.makedirs(path+'../FakeFakeNoise/')
file_list = os.listdir(path)

for f in file_list:
    if f[9:15] == "fake_A" or f[-11:-5] == "fake_A":
        im = Image.open(path+f)
        im.save(path+'../FakeClean/'+f)
        print("filename {} image save".format(path+'../FakeClean/'+f))
    elif f[9:15] == "fake_B" or f[-11:-5] == "fake_B":
        im = Image.open(path+f)
        im.save(path+'../FakeNoise/'+f)
        print("filename {} image save".format(path+'../FakeNoise/'+f))
    elif f[9:15] == "real_A" or f[-11:-5] == "real_A":
        im = Image.open(path+f)
        im.save(path+'../RealClean/'+f)
        print("filename {} image save".format(path+'../RealClean/'+f))
    elif f[9:15] == "real_B" or f[-11:-5] == "real_B":
        im = Image.open(path+f)
        im.save(path+'../RealNoise/'+f)
        print("filename {} image save".format(path+'../RealNoise/'+f))
    elif f[9:14] == "rec_B" or f[-10:-5] == "rec_B":
        im = Image.open(path+f)
        im.save(path+'../FakeFakeNoise/'+f)
        print("filename {} image save".format(path+'../FakeFakeNoise/'+f))
    elif f[9:14] == "rec_A" or f[-10:-5] == "rec_A":
        im = Image.open(path+f)
        im.save(path+'../FakeFakeClean/'+f)
        print("filename {} image save".format(path+'../FakeFakeClean/'+f))

