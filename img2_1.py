from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
filename="Lenna_(test_image).png"
img = Image.open(filename).convert('L')
img = np.array(img)
#Calculate the histogram
hist=np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist[img[i,j]]+=1
#Normalize the histogram
hist=hist/(img.shape[0]*img.shape[1])
#Plot the histogram and original image
plt.figure(figsize=(10,10))
plt.subplot(1,2,1);plt.imshow(img,cmap="gray");plt.title("Original");plt.axis("off")
plt.subplot(1,2,2);plt.title("Histogram");plt.xlabel("Pixel Value");plt.ylabel("Normalized Frequency")
plt.plot(hist, color='black', label='Gray')
plt.legend()
plt.show()
