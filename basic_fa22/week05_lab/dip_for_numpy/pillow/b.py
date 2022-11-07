import numpy as np
from PIL import Image

x = np.zeros((600,800,3),dtype=np.uint8)

x[:,:,0] = 255
x[:,:,1] = 255
x[:,:,2] = 255
x = Image.fromarray(x)
x.show()
