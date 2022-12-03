from fileinput import filename
import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt
filename = "Lenna_(test_image).png"
img = cv.imread(filename)
b, g, r = cv.split(img)
img2 = cv.merge([r, g, b])
#Scale up image
img3 = cv.resize(img2, (img2.shape[1]*2, img2.shape[0]*2), interpolation=cv.INTER_CUBIC)
#Scale down image
img4 = cv.resize(img2, (img2.shape[1]//2, img2.shape[0]//2), interpolation=cv.INTER_CUBIC)
#Non-proportional scale up image
img5 = cv.resize(img2, (img2.shape[1]*2, img2.shape[0]//2), interpolation=cv.INTER_CUBIC)
#Non-proportional scale down image
img6 = cv.resize(img2, (img2.shape[1]//2, img2.shape[0]*2), interpolation=cv.INTER_CUBIC)
#Show image
plt.figure(figsize=(10,10))
print("img3 size: ", img3.shape)
print("img4 size: ", img4.shape)
plt.subplot(2,3,1);plt.imshow(img2);plt.title("Original");plt.axis("off")
plt.subplot(2,3,2);plt.imshow(img3);plt.title("Scale up");plt.axis("off")
plt.subplot(2,3,3);plt.imshow(img4);plt.title("Scale down");plt.axis("off")
plt.subplot(2,3,4);plt.imshow(img5);plt.title("Non-proportional scale up");plt.axis("off")
plt.subplot(2,3,5);plt.imshow(img6);plt.title("Non-proportional scale down");plt.axis("off")
plt.show()