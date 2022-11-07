#############################################
# Color Image Split & Merge using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

print(img.mode)
print(img.size)

img_np = np.array(img)
print(img_np.shape)

red = img_np[:,:,0]
green = img_np[:,:,1]
blue =  img_np[:,:,2]           # r,g,b를 다시 합치는 법 빈 3차원에 대입
print(red.shape)

img_c = np.zeros((680,1024,3), dtype=np.uint8)    # dtype 명시해줌
img_c[:,:,0] = red
img_c[:,:,1] = green
img_c[:,:,2] = blue
image2 = Image.fromarray(img_c)


merge_img = np.zeros((600,800,3), dtype = np.uint8)
merge_img[:,:,0] = 255        # 빨
merge_img[:,:,1] = 255         #   g
merge_img[:,:,2] = 255       # b
merge_img = Image.fromarray(merge_img)
merge_img.show()
