import numpy as np
img = np.array([   [2,     2,      2,      100,    105,    105,    105,    105],\
                            [2,     2,      2,      100,    105,    105,    105,    105],\
                            [2,     5,      5,      5,      5,      110,    110,    110],\
                            [2,     100,    5,      5,      5,      5,      140,    110],\
                            [2,     100,    100,    100,    108,    240,    110,    110],\
                            [2,     100,    100,    108,    108,    240,    110,    110]])
hist = np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist[img[i,j]] += 1
hist = hist/(img.shape[0]*img.shape[1])
#Use Maximum Entropy to binarize
img_Divided=np.array(img)
threshold = 0
max_entropy = 0
for i in range(1,255):
    w0 = np.sum(hist[:i])
    w1 = np.sum(hist[i:])
    u0 = np.sum(hist[:i]*np.arange(i))
    u1 = np.sum(hist[i:]*np.arange(i,256))
    u = w0*u0+w1*u1
    if w0 == 0 or w1 == 0:
        continue
    entropy = -w0*np.log(w0)-w1*np.log(w1)
    if entropy > max_entropy:
        max_entropy = entropy
        threshold = i
print("Threshold:", threshold)
#Binarization
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] >= threshold:
            img_Divided[i,j] = 255
        else:
            img_Divided[i,j] = 0
print(img_Divided)