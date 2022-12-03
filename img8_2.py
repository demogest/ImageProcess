import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def erosion(img,kernel):
    img2 = np.array(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 0:
                for m in range(kernel.shape[0]):
                    for n in range(kernel.shape[1]):
                        if kernel[m,n] == 1:
                            if i+m-1 < 0 or i+m-1 >= img.shape[0] or j+n-1 < 0 or j+n-1 >= img.shape[1]:
                                img2[i,j] = 255
                            elif img[i+m-1,j+n-1] == 255:
                                img2[i,j] = 255
    return img2
def dilation(img,kernel):
    img2 = np.array(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 255:
                for m in range(kernel.shape[0]):
                    for n in range(kernel.shape[1]):
                        if kernel[m,n] == 1:
                            if i+m-1 < 0 or i+m-1 >= img.shape[0] or j+n-1 < 0 or j+n-1 >= img.shape[1]:
                                img2[i,j] = 0
                            elif img[i+m-1,j+n-1] == 0:
                                img2[i,j] = 0
    return img2
#Opening
def opening(img,kernel):
    img2 = erosion(img,kernel)
    img3 = dilation(img2,kernel)
    return img3
#Closing
def closing(img,kernel):
    img2 = dilation(img,kernel)
    img3 = erosion(img2,kernel)
    return img3
filename = "Lenna_Binarization.png"
img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
kernel = np.ones((3,3))
img2 = erosion(img,kernel)
img3 = dilation(img,kernel)
img4 = opening(img,kernel)
img5 = closing(img,kernel)
#Show images
plt.figure(figsize=(10,10))
plt.subplot(151);plt.imshow(img,cmap="gray");plt.title("Original");plt.axis("off")
plt.subplot(152);plt.imshow(img2,cmap="gray");plt.title("Erosion");plt.axis("off")
plt.subplot(153);plt.imshow(img3,cmap="gray");plt.title("Dilation");plt.axis("off")
plt.subplot(154);plt.imshow(img4,cmap="gray");plt.title("Opening");plt.axis("off")
plt.subplot(155);plt.imshow(img5,cmap="gray");plt.title("Closing");plt.axis("off")
plt.show()