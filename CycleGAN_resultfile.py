import os 
from PIL import Image

path = '../CycleGAN/paired512result/denoisind_full_serial_batch_on_cyclegan/test_latest/images/'

file_list = os.listdir(path)
for f in file_list:
    if f[9:15] == "fake_A" :
        im = Image.open(path+f)
        im.save(path+'../FakeClean/'+f)
        print("filename {} image save".format(path+'../FakeClean/'+f))
    elif f[9:15] == "fake_B" :
        im = Image.open(path+f)
        im.save(path+'../FakeNoise/'+f)
        print("filename {} image save".format(path+'../FakeNoise/'+f))
    elif f[9:15] == "real_A" :
        im = Image.open(path+f)
        im.save(path+'../RealClean/'+f)
        print("filename {} image save".format(path+'../RealClean/'+f))
    elif f[9:15] == "real_B" :
        im = Image.open(path+f)
        im.save(path+'../RealNoise/'+f)
        print("filename {} image save".format(path+'../RealNoise/'+f))
    elif f[9:14] == "rec_B" :
        im = Image.open(path+f)
        im.save(path+'../FakeFakeNoise/'+f)
        print("filename {} image save".format(path+'../FakeFakeNoise/'+f))
    elif f[9:14] == "rec_A" :
        im = Image.open(path+f)
        im.save(path+'../FakeFakeClean/'+f)
        print("filename {} image save".format(path+'../FakeFakeClean/'+f))

