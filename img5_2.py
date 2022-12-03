import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.array([[2,     6,      2,      160,        10,         12,         16],    \
                [2,     4,      2,      140,        10,         13,         12],    \
                [3,     5,      3,      120,        10,         10,         10],    \
                [20,    60,     20,     100,        120,        140,        120],   \
                [20,    40,     20,     150,        240,        220,        240],   \
                [30,    50,     30,     250,        240,        200,        240]])
#Convert img to Mat
img = cv2.convertScaleAbs(img)
#One-way first-order differential operator (Horizontal)
im1 = img[:,1:] - img[:,:-1]
#One-way first-order differential operator (Vertical)
im2 = img[1:,:] - img[:-1,:]
#Roberts operator
kernelx=np.array([[1,0],[0,-1]], dtype=np.float32)
kernely=np.array([[0,1],[-1,0]], dtype=np.float32)
robertsx = cv2.filter2D(img, cv2.CV_32F, kernelx)
robertsy = cv2.filter2D(img, cv2.CV_32F, kernely)
absrobertsx = cv2.convertScaleAbs(robertsx)
absrobertsy = cv2.convertScaleAbs(robertsy)
robertsxy = cv2.addWeighted(absrobertsx, 0.5, absrobertsy, 0.5, 0)
#Sobel operator
sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
abssobelx = cv2.convertScaleAbs(sobelx)
abssobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(abssobelx, 0.5, abssobely, 0.5, 0)
#Prewitt operator
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], dtype=np.float32)
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=np.float32)
prewittx = cv2.filter2D(img, cv2.CV_32F, kernelx)
prewitty = cv2.filter2D(img, cv2.CV_32F, kernely)
absprewittx = cv2.convertScaleAbs(prewittx)
absprewitty = cv2.convertScaleAbs(prewitty)
prewittxy = cv2.addWeighted(absprewittx, 0.5, absprewitty, 0.5, 0)
#Laplacian operator
laplacian = cv2.Laplacian(img, cv2.CV_32F)
absLaplacian = cv2.convertScaleAbs(laplacian)
#Wallis operator
kernelx = np.array([[0,0,0],[-1,2,-1],[0,0,0]], dtype=np.float32)
kernely = np.array([[0,-1,0],[0,2,0],[0,-1,0]], dtype=np.float32)
wallisx = cv2.filter2D(img, cv2.CV_32F, kernelx)
wallisy = cv2.filter2D(img, cv2.CV_32F, kernely)
abswallisx = cv2.convertScaleAbs(wallisx)
abswallisy = cv2.convertScaleAbs(wallisy)
wallisxy = cv2.addWeighted(abswallisx, 0.5, abswallisy, 0.5, 0)
#Print the results
print("Original image:\n", img)
print("One-way first-order differential operator (Horizontal):\n", im1)
print("One-way first-order differential operator (Vertical):\n", im2)
print("Roberts operator:\n", robertsxy)
print("Sobel operator:\n", sobelxy)
print("Prewitt operator:\n", prewittxy)
print("Laplacian operator:\n", absLaplacian)
print("Wallis operator:\n", wallisxy)

