from fileinput import filename
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
filename="Lenna_(test_image).png"
img = Image.open(filename)
img = np.array(img)
#Split RGB channels
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]
#Calculate the histogram of each channel
hist_r=np.zeros(256)
hist_g=np.zeros(256)
hist_b=np.zeros(256)
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        hist_r[r[i,j]]+=1
        hist_g[g[i,j]]+=1
        hist_b[b[i,j]]+=1
#Normalize the histogram
hist_r=hist_r/(r.shape[0]*r.shape[1])
hist_g=hist_g/(g.shape[0]*g.shape[1])
hist_b=hist_b/(b.shape[0]*b.shape[1])
#Plot the histogram of each channel
plt.title("Histogram of RGB channels")
plt.xlabel("Pixel Value")
plt.ylabel("Normalized Frequency")
plt.plot(hist_r, color='red', label='Red')
plt.plot(hist_g, color='green', label='Green')
plt.plot(hist_b, color='blue', label='Blue')
plt.legend()
plt.show()