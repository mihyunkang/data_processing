from skimage.measure import compare_ssim
from skimage.measure import compare_psnr
import os
import numpy 
import cv2
from skimage.external.tifffile import imsave, imread

result_dir = "../../../data/CycleGAN-data/result_mayo_blur_gaussian/128_longskip_mstd_r9/128_longskip_mstd_r9/test_latest/FakeClean/"
GT_dir = "../../../data/CycleGAN-data/datasets/mayo_blur/testA/"
noise_dir = "../../../data/CycleGAN-data/datasets/mayo_blur/testB/"

result_list = sorted(os.listdir(result_dir))
GT_list = sorted(os.listdir(GT_dir))
noise_list = sorted(os.listdir(noise_dir))
avg_psnr_r = 0
avg_ssim_r = 0
avg_psnr_n = 0
avg_ssim_n = 0
print(len(result_list))
print(len(GT_list))
print(len(noise_list))
if len(result_list) == len(GT_list) and len(result_list) == len(noise_list):
    for i in range(len(result_list)):
        result = imread(result_dir+result_list[i])
        GT = imread(GT_dir+GT_list[i])
        noise = imread(noise_dir+noise_list[i])

        psnr_r = compare_psnr(GT, result)
        ssim_r = compare_ssim(GT, result)
        psnr_n = compare_psnr(GT, noise)
        ssim_n = compare_ssim(GT, noise)
        print("result psnr {} ssim {}".format(psnr_r, ssim_r))
        print("noise  psnr {} ssim {}".format(psnr_n, ssim_n))
        avg_psnr_r += psnr_r
        avg_ssim_r += ssim_r
        avg_psnr_n += psnr_n
        avg_ssim_n += ssim_n
    print("--------------------------------result-----------------------------")
    print("average result psnr {} ssim {}".format(avg_psnr_r/len(GT_list), avg_ssim_r/len(GT_list)))
    print("average noise  psnr {} ssim {}".format(avg_psnr_n/len(GT_list), avg_ssim_n/len(GT_list)))
else:
    print("lengths of file are different")


    """
    모든 이미지에 -0.5 내꺼에 *2 ---> 1mm
    average result psnr 41.59305725469379 ssim 0.9538950636226659 
    average noise  psnr 39.4374916335283 ssim 0.9242086433746843
    -> ../../../data/CycleGAN-data/result/mayo-20200131-waveletdl-patch64-swt-bior2.2-lv2-parallel+channels_per_group10-patch_offset8/


    average result psnr 31.326445243407175 ssim 0.9456032874843044
    average noise  psnr 39.4374916335283 ssim 0.9242086433746843
    ->../../../data/CycleGAN-data/result/mayo-20191225-redcnn-patch64-n_feats96-n_resblocks16-offset_x0_512-offset_y0_512-patch_offset5/


    average result psnr 40.71353008853013 ssim 0.9456377965321326
    average noise  psnr 39.4374916335283 ssim 0.9242086433746843 
    ->../../../data/CycleGAN-data/result/mayo-20200211-edsr-patch64-n_feats96-n_resblocks16-patch_offset5/

    average result psnr 40.92642010992271 ssim 0.9602056497981172
    average noise  psnr 39.4374916335283 ssim 0.9242086433746843 
    ->../../../data/CycleGAN-data/result/mayo-20200121-waveletdl-patch64-swt-bior2.2-lv2-parallel+channels_per_group10-perceptual_loss-srgan-patch_offset5/


    average result psnr 40.99929111011324 ssim 0.9552245408397698
    average noise  psnr 39.4374916335283 ssim 0.9242086433746843
    ->../../../data/CycleGAN-data/result/add_pixelwiseloss_512_cat_noise_200/pixelwiaeloss_concatNoise_512/test_latest/FakeClean/
    """