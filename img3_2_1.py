import numpy as np
img = np.array([[2,6,220,220,120,160,220,160],  \
                [2,9,221,220,120,12,12,12],     \
                [3,9,12,120,120,3,10,8],        \
                [3,7,12,10,8,3,6,6],            \
                [4,2,9,12,8,4,6,6],             \
                [2,0,7,9,6,4,2,8]])
print("Original Image:\n"+str(img))
#Image Contrast Widening
fa=8;fb=160;ga=4;gb=240
alpha=ga/fa;beta=(gb-ga)/(fb-fa);gamma=(255-gb)/(255-fb)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j]<=fa:
            img[i,j]=alpha*img[i,j]
        elif img[i,j]<=fb:
            img[i,j]=beta*(img[i,j]-fa)+ga
        else:
            img[i,j]=gamma*(img[i,j]-fb)+gb
print("After Contrast Widening:\n"+str(img))