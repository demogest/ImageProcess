import math
import numpy as np
img = np.array([[2,6,220,220,120,160,220,160],  \
                [2,9,221,220,120,12,12,12],     \
                [3,9,12,120,120,3,10,8],        \
                [3,7,12,10,8,3,6,6],            \
                [4,2,9,12,8,4,6,6],             \
                [2,0,7,9,6,4,2,8]])
print("Original Image:\n"+str(img))
#Image Dynamic Range Compression
c=255/(math.log(1+np.max(img)))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j]=c*math.log(1+img[i,j])
print("After Dynamic Range Compression:\n"+str(img))