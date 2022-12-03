from PIL import Image
import numpy as np
filename="Lenna_(test_image).png"
#read color image to array
img = np.array(Image.open(filename))
#Add Gaussian Noise
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            img[i,j,k]+=np.random.normal(0,10)
#Add Salt and Pepper Noise
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            if np.random.rand()<0.01:
                img[i,j,k]=0
            elif np.random.rand()<0.01:
                img[i,j,k]=255
#Convert array to image
img = Image.fromarray(img)
img.show()
#Save the image
img.save("img4_1_add.png")