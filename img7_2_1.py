import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def Division_Judge(img, h0, w0, h, w):
    area = img[h0: h0 + h, w0: w0 + w]
    std = np.std(area, ddof=1)
    if std < 1:
        return True
    else:
        return False


def Merge(img, sub):
    total, areas = 0, []
    for area in sub:
        for i in range(area[0], area[0]+area[2]):
            for j in range(area[1], area[1]+area[3]):
                areas.append([i, j, total])
        total += 1
    areas = np.array(areas)
    sub = np.zeros(img.shape)
    for i in range(areas.shape[0]):
        area = areas[areas[:, 2] == i]
        if area.shape[0] > 0:
            sub[area[:, 0], area[:, 1]] = i
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (i+1 < img.shape[0] and sub[i, j] != sub[i+1, j]):
                if abs(np.mean(img[sub == sub[i, j]])-np.mean(img[sub == sub[i+1, j]])) < 10:
                    sub[sub == sub[i+1, j]] = sub[i, j]
            if (j+1 < img.shape[1] and sub[i, j] != sub[i, j+1]):
                if abs(np.mean(img[sub == sub[i, j]])-np.mean(img[sub == sub[i, j+1]])) < 10:
                    sub[sub == sub[i, j+1]] = sub[i, j]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.mean(img[sub == sub[i, j]]) > 100:
                img[sub == sub[i, j]] = 255
            else:
                img[sub == sub[i, j]] = 0


def Recursion(img, h0, w0, h, w, total, sub):
    total += 1
    if (not Division_Judge(img, h0, w0, h, w)) and (h > 1 or w > 1):
        h1 = h // 2
        w1 = w // 2
        Recursion(img, h0, w0, h1, w1, total, sub)
        Recursion(img, h0 + h1, w0, h - h1, w1, total, sub)
        Recursion(img, h0, w0 + w1, h1, w - w1, total, sub)
        Recursion(img, h0 + h1, w0 + w1, h - h1, w - w1, total, sub)
    else:
        sub.append([h0, w0, h, w])


def Division_Merge_Segmented():
    img_gray = np.array(
        cv.imread('Lenna_(test_image).png', cv.IMREAD_GRAYSCALE))
    segemented_img = img_gray.copy()
    sub = []
    Recursion(segemented_img, 0, 0,
              segemented_img.shape[0], segemented_img.shape[1], 0, sub)
    Merge(segemented_img, sub)
    # show image
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(segemented_img, cmap='gray')
    plt.title('Segmented Image')


img_gray = np.array(cv.imread('Lenna_(test_image).png', cv.IMREAD_GRAYSCALE))
segemented_img = img_gray.copy()
sub = []
Recursion(segemented_img, 0, 0,
          segemented_img.shape[0], segemented_img.shape[1], 0, sub)
Merge(segemented_img, sub)
# show image
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(segemented_img, cmap='gray')
plt.title('Segmented Image')
plt.show()