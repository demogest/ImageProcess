from PIL import Image
import numpy as np
filename="Lenna_(test_image).png"
img = Image.open(filename)
img = np.array(img)
#Calculate Histogram Equalization
hist=np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            hist[img[i,j,k]]+=1
hist=hist/(img.shape[0]*img.shape[1]*img.shape[2])
for i in range(1,256):
    hist[i]+=hist[i-1]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            img[i,j,k]=255*hist[img[i,j,k]]
#Convert back to image
img = Image.fromarray(img)
img.show()