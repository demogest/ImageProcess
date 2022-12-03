from PIL import Image
import numpy as np
filename="Lenna_(test_image).png"
#read color image to array
img = np.array(Image.open(filename))
#Color image Contrast Widening
fa=100;fb=200;ga=200;gb=220
alpha=ga/fa;beta=(gb-ga)/(fb-fa);gamma=(255-gb)/(255-fb)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            if img[i,j,k]<=fa:
                img[i,j,k]=alpha*img[i,j,k]
            elif img[i,j,k]<=fb:
                img[i,j,k]=beta*(img[i,j,k]-fa)+ga
            else:
                img[i,j,k]=gamma*(img[i,j,k]-fb)+gb
#Convert array to image
img = Image.fromarray(img)
img.show()