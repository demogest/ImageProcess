import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
filename = "Lenna_(test_image).png"
img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
img2 = np.array(img)
#Caclute histogram
hist = np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist[img[i,j]] += 1
hist = hist/(img.shape[0]*img.shape[1])
#Calculate cumulative histogram
cum_hist,threshold,p=0,0,0.5
for i in range(1,256):
    cum_hist += hist[i]
    if cum_hist >= p:
        threshold = i
        break
print("Threshold of P=0.5:", threshold)
#Binarization
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] >= threshold:
            img2[i,j] = 255
        else:
            img2[i,j] = 0
#Use peeks and valleys to binarize
img3=np.array(img)
peeks, valleys = [], []
for i in range(1,255):
    if hist[i-1] < hist[i] and hist[i] > hist[i+1]:
        peeks.append(i)
    elif hist[i-1] > hist[i] and hist[i] < hist[i+1]:
        valleys.append(i)
#Calculate threshold
threshold = (peeks[0]+valleys[0])//2
print("Threshold of peeks and valleys:", threshold)
#Binarization
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] >= threshold:
            img3[i,j] = 255
        else:
            img3[i,j] = 0
#Use Maximum Variance within Class to binarize
img4=np.array(img)
u=np.mean(img4)
threshold = 0
max_var = 0
for i in range(1,255):
    u0 = 0 if np.all(img4[img4<i]!=img4[img4<i]) else np.mean(img4[img4<i])
    u1 = 0 if np.all(img4[img4>=i]!=img4[img4>=i]) else np.mean(img4[img4>=i])
    var0 = np.sum((img4[img4<i]-u0)**2)
    var1 = np.sum((img4[img4>=i]-u1)**2)
    var_b = np.sum(hist[:i])*(u0-u)**2 + np.sum(hist[i:])*(u1-u)**2
    var_in = np.sum(hist[:i])*var0 + np.sum(hist[i:])*var1
    if abs(var_b/var_in) > max_var:
        max_var = abs(var_b/var_in)
        threshold = i
print("Threshold of class variance:", threshold)
#Binarization
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] >= threshold:
            img4[i,j] = 255
        else:
            img4[i,j] = 0

#Use Maximum Entropy to binarize with numpy
img7=np.array(img)
threshold = 0
max_entropy = 0
hist = cv.calcHist([img],[0],None,[256],[0,256])
for i in range(1,255):
    w0 = np.sum(hist[:i])
    w1 = np.sum(hist[i:])
    # u0 = np.sum(hist[:i]*np.arange(i))
    # u1 = np.sum(hist[i:]*np.arange(i,256))
    # u = w0*u0+w1*u1
    if w0 == 0 or w1 == 0:
        continue
    entropy = -w0*np.log(w0)-w1*np.log(w1)
    if entropy > max_entropy:
        max_entropy = entropy
        threshold = i
print("Threshold of maximum entropy:", threshold)
#Binarization
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] >= threshold:
            img7[i,j] = 255
        else:
            img7[i,j] = 0
#Save image7
cv.imwrite("Lenna_Binarization.png", img7)
#Show images
plt.figure(figsize=(10,10))
plt.subplot(3,3,2);plt.imshow(img,cmap='gray');plt.title('Original');plt.axis('off')
plt.subplot(3,3,4);plt.imshow(img2,cmap='gray');plt.title('P Threshold');plt.axis('off')
plt.subplot(3,3,6);plt.imshow(img3,cmap='gray');plt.title('Peeks and Valleys');plt.axis('off')
plt.subplot(3,3,7);plt.imshow(img4,cmap='gray');plt.title('Maximum Variance within and between Class');plt.axis('off')
plt.subplot(3,3,9);plt.imshow(img7,cmap='gray');plt.title('Maximum Entropy');plt.axis('off')
plt.show()