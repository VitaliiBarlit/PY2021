# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 08:42:32 2019

@author: User
"""
from PIL import Image, ImageOps, _imaging
import os


#image_list = []
area = (0, 0, 1185, 768)
#D:\Project\PY\imgc\
p = os.getcwd()


for filename in glob.glob(p + '\*.jpg'):
    im = Image.open(filename)
    im = ImageOps.invert(im)
    im = im.crop(area)
    name = filename.replace(p,'')
    name = name[1:]
    im.save( name, format='JPEG' )
#    image_list.append(im)


input('Press Enter to exit.')


 






    
