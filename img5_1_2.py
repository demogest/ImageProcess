import numpy as np
import matplotlib.pyplot as plt
import cv2
#Read image 
im = cv2.imread('Lenna_(test_image).png')
b,g,r = cv2.split(im)
im2 = cv2.merge([r,g,b])
#Gray image
grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#Sobel operator
sobelx = cv2.Sobel(grayImage, cv2.CV_32F, 1, 0)
sobely = cv2.Sobel(grayImage, cv2.CV_32F, 0, 1)
absx = cv2.convertScaleAbs(sobelx)
absy = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)
#Roberts operator
kernelx = np.array([[-1,0],[0,1]], dtype=np.float32)
kernely = np.array([[0,-1],[1,0]], dtype=np.float32)
robertsx = cv2.filter2D(grayImage, cv2.CV_32F, kernelx)
robertsy = cv2.filter2D(grayImage, cv2.CV_32F, kernely)
absrobertsx = cv2.convertScaleAbs(robertsx)
absrobertsy = cv2.convertScaleAbs(robertsy)
robertsxy = cv2.addWeighted(absrobertsx, 0.5, absrobertsy, 0.5, 0)
#Prewwit operator
kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=np.float32)
kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], dtype=np.float32)
prewwitx = cv2.filter2D(grayImage, cv2.CV_32F, kernelx)
prewwity = cv2.filter2D(grayImage, cv2.CV_32F, kernely)
absprewwitx = cv2.convertScaleAbs(prewwitx)
absprewwity = cv2.convertScaleAbs(prewwity)
prewwitxy = cv2.addWeighted(absprewwitx, 0.5, absprewwity, 0.5, 0)
#Show image
plt.figure()
plt.subplot(232); plt.imshow(im2); plt.axis('off'); plt.title('Original image')
plt.subplot(234); plt.imshow(sobelxy, cmap='gray'); plt.axis('off'); plt.title('Sobel')
plt.subplot(235); plt.imshow(robertsxy, cmap='gray'); plt.axis('off'); plt.title('Roberts')
plt.subplot(236); plt.imshow(prewwitxy, cmap='gray'); plt.axis('off'); plt.title('Prewwit')
plt.show()