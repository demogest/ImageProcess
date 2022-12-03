from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
filename="img4_1_add.png"
img = Image.open(filename)
img = np.array(img)

#K nearest neighbor Mean filter
def KNN(img,kernel,k):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            for l in range(result_img.shape[2]):
                center = img[i+kernel//2,j+kernel//2,l]
                windows = img[i:i+kernel,j:j+kernel,l].astype(np.int32)
                result=[[abs(i-center),i] for i in windows.ravel()]
                result.sort()
                result_img[i+kernel//2,j+kernel//2,l]=round(np.array(result)[:k,1].mean())
    return result_img       
#Symmetric nearest neighbor Mean filter
def SNN(img,kernel):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            for l in range(result_img.shape[2]):
                center = img[i+kernel//2,j+kernel//2,l]
                windows = img[i:i+kernel,j:j+kernel,l].astype(np.int32)
                pairs=[]
                for i2 in range(windows.shape[0]//2):
                    for j2 in range(windows.shape[1]//2):
                        if i2 == i+kernel//2 and j2 == j+kernel//2:
                            continue
                        pairs.append([windows[2*(kernel//2)-i2,2*(kernel//2)-j2],windows[i2,j2]])
                pairs = np.array(pairs)
                pairs =[pairs[i,0] if abs(pairs[i,0]-center)<abs(pairs[i,1]-center) else pairs[i,1] for i in range(pairs.shape[0])]
                result_img[i+kernel//2,j+kernel//2,l]=round(np.array(pairs).mean())
    return result_img
      
img_KNN = KNN(img,3,5)
img_SNN = SNN(img,3)
plt.figure(figsize=(10,10))
plt.subplot(1,3,1);plt.imshow(img);plt.title("Original");plt.axis("off")
plt.subplot(1,3,2);plt.imshow(img_KNN);plt.title("KNN");plt.axis("off")
plt.subplot(1,3,3);plt.imshow(img_SNN);plt.title("SNN");plt.axis("off")
plt.show()