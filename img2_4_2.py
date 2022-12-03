import numpy as np
from matplotlib import pyplot as plt 
img = np.matrix([[100,76,0,132,7,7],[28,7,7,7,7,243],[28,243,7,100,7,28],[100,7,7,0,7,100],[100,0,7,7,132,0],[132,132,132,100,7,100]])
#caclute the histogram
hist = np.zeros(256)
for i in range(6):
    for j in range(6):
        hist[img[i,j]] += 1
#plot the histogram
plt.plot(hist)
plt.show()
