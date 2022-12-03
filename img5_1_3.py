import cv2
import numpy as np
import matplotlib.pyplot as plt
#Read image
im = cv2.imread('Lenna_(test_image).png')
b,g,r = cv2.split(im)
im2 = cv2.merge([r,g,b])
#Gray image
grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#Laplacian operator
laplacian = cv2.Laplacian(grayImage, cv2.CV_32F)
absLaplacian = cv2.convertScaleAbs(laplacian)
#Wallis operator
kernelx = np.array([[0,0,0],[-1,2,-1],[0,0,0]], dtype=np.float32)
kernely = np.array([[0,-1,0],[0,2,0],[0,-1,0]], dtype=np.float32)
wallisx = cv2.filter2D(grayImage, cv2.CV_32F, kernelx)
wallisy = cv2.filter2D(grayImage, cv2.CV_32F, kernely)
abswallisx = cv2.convertScaleAbs(wallisx)
abswallisy = cv2.convertScaleAbs(wallisy)
wallisxy = cv2.addWeighted(abswallisx, 0.5, abswallisy, 0.5, 0)
#Show image
plt.figure()
plt.subplot(231); plt.imshow(im2); plt.axis('off'); plt.title('Original image')
plt.subplot(232); plt.imshow(absLaplacian, cmap='gray'); plt.axis('off'); plt.title('Laplacian')
plt.subplot(233); plt.imshow(wallisxy, cmap='gray'); plt.axis('off'); plt.title('Wallis')
plt.show()