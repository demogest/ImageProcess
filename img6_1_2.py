from email.mime import image
from turtle import position
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
#Use Affine transformation formula to implement image rotation ,twist and mirror
def affine(img,func,degree):
    if func == "mirror":
        kernel = np.array([[-1,0,0],[0,1,0],[0,0,1]])
        img_new=np.zeros(img.shape)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                position = np.array([i,j,1])
                position_new = np.dot(kernel,position)
                img_new[img.shape[0]-1+position_new[0],position_new[1],:]=img[i,j,:]
        return Image.fromarray(img_new.astype(np.uint8))
    elif func == "rotate":
        kernel = np.array([ [math.cos(degree*math.pi/180.0),    math.sin(degree*math.pi/180.0), 0],\
                            [-math.sin(degree*math.pi/180.0),   math.cos(degree*math.pi/180.0), 0],\
                            [0,                                 0,                              1]])
        img_new=np.zeros([int(img.shape[0]*math.sqrt(2)),int(img.shape[1]*math.sqrt(2)),img.shape[2]])
        positions=[]
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                position = np.array([i,j,1])
                position_new = np.dot(kernel,position)
                positions.append([position_new[0],position_new[1],i,j])
        positions = np.array(positions)
        mina = np.min(positions[:,0],axis=0)
        minb = np.min(positions[:,1],axis=0)
        for i in range(positions.shape[0]):
            img_new[int(positions[i,0]-mina),int(positions[i,1]-minb),:]=img[int(positions[i,2]),int(positions[i,3]),:]
        #Fill the empty area with the mean value of the nearest 8 pixels
        for i in range(img_new.shape[0]):
            for j in range(img_new.shape[1]):
                if np.sum(img_new[i,j,:])==0:
                    img_new[i,j,:]=np.mean(
                        img_new[max(0,i-1):min(img_new.shape[0],i+2),max(0,j-1):min(img_new.shape[1],j+2),:],axis=(0,1))
        return Image.fromarray(img_new.astype(np.uint8))
    elif func == "twist":
        kernel = np.array([[1,math.tan(degree*math.pi/180.0),0],[0,1,0],[0,0,1]])
        img_new = np.zeros([int(img.shape[0]+img.shape[1]*math.tan(degree*math.pi/180.0)),img.shape[1],img.shape[2]])
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                x = int(i*kernel[0,0]+j*kernel[0,1]+kernel[2,0])
                y = int(i*kernel[1,0]+j*kernel[1,1]+kernel[2,1])
                if x>=0 and x<img_new.shape[0] and y>=0 and y<img_new.shape[1]:
                    img_new[x,y,:]=img[i,j,:]
    return Image.fromarray(np.uint8(img_new))
#Read color image to array
filename="Lenna_(test_image).png"
img = np.array(Image.open(filename))
#Mirror
img_mirror = affine(img,"mirror",0)
#Rotate
img_rotate = affine(img,"rotate",30)
#Twist
img_twist = affine(img,"twist",30)
#Show image
plt.figure(figsize=(10,10))
plt.subplot(2,2,1);plt.title("Original Image");plt.imshow(img);plt.axis("off")
plt.subplot(2,2,2);plt.title("Mirror Image");plt.imshow(img_mirror);plt.axis("off")
plt.subplot(2,2,3);plt.title("Rotate Image");plt.imshow(img_rotate);plt.axis("off")
plt.subplot(2,2,4);plt.title("Twist Image");plt.imshow(img_twist);plt.axis("off")
plt.show()