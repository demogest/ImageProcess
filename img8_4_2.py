import numpy as np
img = np.array([[0,0,0,1,0,0,0,0],[0,1,1,1,0,0,0,0],[0,0,1,1,1,1,0,0],[0,1,0,1,1,1,1,1],[0,1,0,1,1,1,0,0],[0,1,1,0,0,1,0,0]])
reslut = np.zeros(img.shape)
#Inverse for connect 8
img = 1-img
#Calculate each pixel
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        if img[i,j] == 0:
            s=0
            s+=img[i,j+1]-img[i,j+1]*img[i-1,j+1]*img[i-1,j]
            s+=img[i-1,j]-img[i-1,j]*img[i-1,j-1]*img[i,j-1]
            s+=img[i,j-1]-img[i,j-1]*img[i+1,j-1]*img[i+1,j]
            s+=img[i+1,j]-img[i+1,j]*img[i+1,j+1]*img[i,j+1]
            reslut[i,j] = s
print(reslut)