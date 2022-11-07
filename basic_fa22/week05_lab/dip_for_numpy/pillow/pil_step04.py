#############################################
# Convert Color image to Gray image using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('../images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
img.show()
def rgb2gray(rgb):
    r,g,b = rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    gray = (1/3)*r+(1/3)*g+(1/3)*b

    return gray
img_np = np.array(img) # numpy로 바꾸기
print(img_np.shape,img_np.dtype,img_np.size,img_np.ndim)  # uint8 은 unsigned 이므로 0~255, ndim은 3차원이여서 3출력
x = rgb2gray(img_np)
image2 = Image.fromarray(x)

print(type(image2))

image2.show()

