from fileinput import filename


import numpy as np
from PIL import Image
img=np.array([[100,76,0,132,7,7],[28,7,7,7,7,243],[28,243,7,100,7,28],[100,7,7,0,7,100]])
#Save image as bmp
img=Image.fromarray(img)
img.save("img.bmp")