from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
filename="img4_1_add.png"
img = Image.open(filename).convert("L")
img = np.array(img)
#Gray value erosion
def erosion(img):
    result_img = img.copy()
    kernel = np.ones((3,3),np.uint8)
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
                windows = img[i-1:i+2,j-1:j+2].astype(np.int32)
                result_img[i,j]=np.min(windows-kernel)
    return result_img
#Gray value dilation
def dilation(img):
    result_img = img.copy()
    kernel = np.ones((3,3),np.uint8)
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
                windows = img[i-1:i+2,j-1:j+2].astype(np.int32)
                result_img[i,j]=np.max(windows+kernel)
    return result_img
#Gray value opening
def opening(img):
    result_img = erosion(img)
    result_img = dilation(result_img)
    return result_img
#Gray value closing
def closing(img):
    result_img = dilation(img)
    result_img = erosion(result_img)
    return result_img
img_Close = closing(img)
img_Open = opening(img)
#Show gray img
plt.figure(figsize=(10,10))
plt.subplot(1,3,1);plt.imshow(img,cmap="gray");plt.title("Original");plt.axis("off")
plt.subplot(1,3,2);plt.imshow(img_Close,cmap="gray");plt.title("Close");plt.axis("off")
plt.subplot(1,3,3);plt.imshow(img_Open,cmap="gray");plt.title("Open");plt.axis("off")
plt.show()