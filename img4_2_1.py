import numpy as np
import matplotlib.pyplot as plt
#Median filter
def median_filter(img,kernel):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            windows = img[i:i+kernel,j:j+kernel].astype(np.int32)
            result_img[i+kernel//2,j+kernel//2]=np.median(windows)
    return result_img
#Mean filter
def mean_filter(img,kernel):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            windows = img[i:i+kernel,j:j+kernel].astype(np.int32)
            result_img[i+kernel//2,j+kernel//2]=round(np.mean(windows))
    return result_img
#K nearest neighbor Mean filter
def KNN(img,kernel,k):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            center = img[i+kernel//2,j+kernel//2]
            windows = img[i:i+kernel,j:j+kernel].astype(np.int32)
            result=[[abs(i-center),i] for i in windows.ravel()]
            result.sort()
            result_img[i+kernel//2,j+kernel//2]=round(np.array(result)[:k,1].mean())
    return result_img
#Symmetric nearest neighbor Mean filter
def SNN(img,kernel):
    result_img = img.copy()
    for i in range(result_img.shape[0]-kernel+1):
        for j in range(result_img.shape[0]-kernel+1):
            center = img[i+kernel//2,j+kernel//2]
            windows = img[i:i+kernel,j:j+kernel].astype(np.int32)
            pairs=[]
            for i2 in range(windows.shape[0]//2):
                for j2 in range(windows.shape[1]//2):
                    if i2 == i+kernel//2 and j2 == j+kernel//2:
                        continue
                    pairs.append([windows[2*(kernel//2)-i2,2*(kernel//2)-j2],windows[i2,j2]])
            pairs = np.array(pairs)
            pairs =[pairs[i,0] if abs(pairs[i,0]-center)<abs(pairs[i,1]-center) else pairs[i,1] for i in range(pairs.shape[0])]
            result_img[i+kernel//2,j+kernel//2]=round(np.array(pairs).mean())
    return result_img
#Gray erosion
def erosion(img,kernel:np.ndarray):
    result_img = img.copy()
    for i in range(1,result_img.shape[0]-kernel.shape[0]+1):
        for j in range(1,result_img.shape[0]-kernel.shape[0]+1):
            windows = img[i-1:i+kernel.shape[0]-1,j-1:j+kernel.shape[0]-1].astype(np.int32)
            result_img[i,j]=np.min(windows-kernel)
    return result_img
#Gray dilation
def dilation(img,kernel:np.ndarray):
    result_img = img.copy()
    for i in range(1,result_img.shape[0]-kernel.shape[0]+1):
        for j in range(1,result_img.shape[0]-kernel.shape[0]+1):
            windows = img[i-1:i+kernel.shape[0]-1,j-1:j+kernel.shape[0]-1].astype(np.int32)
            result_img[i,j]=np.max(windows+kernel)
    return result_img
#Gray opening
def opening(img,kernel:np.ndarray):
    return dilation(erosion(img,kernel),kernel)
#Gray closing
def closing(img,kernel:np.ndarray):
    return erosion(dilation(img,kernel),kernel)
img = np.array([[2,     6,      2,      4,      38,     10,     2,      16],        \
                [2,     9,      221,    7,      0,      10,     3,      12],        \
                [30,    9,      6,      120,    120,    3,      10,     8],         \
                [3,     7,      5,      10,     8,      3,      6,      66],        \
                [4,     120,    9,      12,     8,      240,    6,      6],         \
                [2,     0,      7,      9,      6,      4,      2,      8]])
kernel = np.array([[1,0],[1,1]])
print("Original image:\n",img)
print("Mean filter:\n",mean_filter(img,3))
print("Median filter:\n",median_filter(img,3))
print("KNN filter:\n",KNN(img,3,3))
print("SNN filter:\n",SNN(img,3))
print("Gray opening:\n",opening(img,kernel))
print("Gray closing:\n",closing(img,kernel))