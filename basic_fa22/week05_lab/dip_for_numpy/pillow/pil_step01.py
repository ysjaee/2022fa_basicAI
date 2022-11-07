#############################################
# Image Read & Show
#############################################

import numpy as np
from PIL import Image  # pillow 모듈에 이미지 불러오기
image = Image.open('../images/baby.png') # 상대 경로 위치


print(type(image))
#image.show()  # 이미지보기

img_np = np.array(image) # numpy로 바꾸기
print(img_np.shape,img_np.dtype,img_np.size,img_np.ndim)  # uint8 은 unsigned 이므로 0~255, ndim은 3차원이여서 3출력

image2 = Image.fromarray(img_np)

print(type(image2))
image2.show()
