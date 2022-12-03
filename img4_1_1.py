from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
filename="img4_1_add.png"
#read color image to array
img = np.array(Image.open(filename))
#Function of Median Filter with mask size
def median_filter(img,mask_size,result):
    img_new=np.zeros(img.shape,dtype=np.uint8)
    for i in range(mask_size//2,img.shape[0]-mask_size//2):
        for j in range(mask_size//2,img.shape[1]-mask_size//2):
            for k in range(img.shape[2]):
                img_new[i,j,k]=np.median(img[i-mask_size//2:i+mask_size//2+1,j-mask_size//2:j+mask_size//2+1,k])
    result["median"+str(mask_size)]=img_new
#Function of Mean Filter with mask size
def mean_filter(img,mask_size,result):
    img_new=np.zeros(img.shape,dtype=np.uint8)
    for i in range(mask_size//2,img.shape[0]-mask_size//2):
        for j in range(mask_size//2,img.shape[1]-mask_size//2):
            for k in range(img.shape[2]):
                img_new[i,j,k]=np.mean(img[i-mask_size//2:i+mask_size//2+1,j-mask_size//2:j+mask_size//2+1,k])
    result["mean"+str(mask_size)]=img_new
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    result = manager.dict()
    process_list=[]
    p1 = multiprocessing.Process(target=median_filter,args=(img,3,result))
    process_list.append(p1)
    p2 = multiprocessing.Process(target=median_filter,args=(img,5,result))
    process_list.append(p2)
    p3 = multiprocessing.Process(target=median_filter,args=(img,7,result))
    process_list.append(p3)
    p4 = multiprocessing.Process(target=mean_filter,args=(img,3,result))
    process_list.append(p4)
    p5 = multiprocessing.Process(target=mean_filter,args=(img,5,result))
    process_list.append(p5)
    p6 = multiprocessing.Process(target=mean_filter,args=(img,7,result))
    process_list.append(p6)
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
    result=dict(result)
    plt.figure(figsize=(10,10))
    plt.subplot(2,3,1);plt.imshow(result["median3"]);plt.title("3x3 Median Filter");plt.axis("off")
    plt.subplot(2,3,2);plt.imshow(result["median5"]);plt.title("5x5 Median Filter");plt.axis("off")
    plt.subplot(2,3,3);plt.imshow(result["median7"]);plt.title("7x7 Median Filter");plt.axis("off")
    plt.subplot(2,3,4);plt.imshow(result["mean3"]);plt.title("3x3 Mean Filter");plt.axis("off")
    plt.subplot(2,3,5);plt.imshow(result["mean5"]);plt.title("5x5 Mean Filter");plt.axis("off")
    plt.subplot(2,3,6);plt.imshow(result["mean7"]);plt.title("7x7 Mean Filter");plt.axis("off")
    plt.show()