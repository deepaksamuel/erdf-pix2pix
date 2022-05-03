#%%
import os
import math
import random
import numpy as np
import cv2
from PIL import Image
IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def make_dataset(dir):
    images = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir

    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                images.append(path)

    return images

input_path = "erdf_img_png"        #set your own input images folder 
target_path  = "wepl_img_png"      #set your own target images folder 
save_dir = "img/"          #set your own save images folder

input_img = make_dataset(input_path)    #create a list of images
target_img  = make_dataset(target_path) #same
input_img = np.sort(input_img)
target_img = np.sort(target_img)


for inp, tar in zip(input_img, target_img):

    ip_filename = inp.split("/")[-1].split(".png")[0].replace("-ERDF","") #split the filename from path
    tar_filename = tar.split("/")[-1].split(".png")[0] #split the filename from path
    if(ip_filename == tar_filename):
        filename = ip_filename
        print(filename)
        inp_img  = cv2.imread(inp) #input image
        tar_img = cv2.imread(tar)  #target image
        h, w, _ = inp_img.shape
        
        #make sure two images has same size
        tar_img = cv2.resize(tar_img,(w,h),interpolation=cv2.INTER_AREA)

        #combine two images as one
        tmp = np.hstack((tar_img,inp_img))

        #save the combine image to save images folder
        cv2.imwrite(os.path.join(save_dir + filename + ".png"),tmp)
        print(filename + " Save...") #comfirm the process
    else:
        print("Input and target filenames mismatch...")
        print(ip_filename,tar_filename);
        break
