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
#Use Maximum Variance within Class to binarize
img_Divided=np.array(img)
u=np.mean(img)
threshold = 0
max_var = 0
for i in range(1,255):
    u0 = np.mean(img[img<i])
    u1 = np.mean(img[img>=i])
    var0 = np.sum((img[img<i]-u0)**2)
    var1 = np.sum((img[img>=i]-u1)**2)
    var_b = np.sum(hist[:i])*(u0-u)**2 + np.sum(hist[i:])*(u1-u)**2
    var_in = np.sum(hist[:i])*var0 + np.sum(hist[i:])*var1
    if abs(var_b/var_in) > max_var:
        max_var = abs(var_b/var_in)
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