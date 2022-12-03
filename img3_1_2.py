from cmath import log
import math
from PIL import Image
import numpy as np
filename="Lenna_(test_image).png"
img = Image.open(filename)
img = np.array(img)
#Calculate Dynamic Range
c=255/(math.log(1+np.max(img)))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            img[i,j,k]=c*math.log(1+img[i,j,k])
#Convert back to image
img = Image.fromarray(img)
img.show()