from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
#Twist image Horizontally
def twist(image,angle):
    a = math.tan(angle*math.pi/180.0)
    img_new = np.zeros([int(image.shape[0]+image.shape[1]*a),image.shape[1],image.shape[2]])
    print(img_new.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x = int(i+j*a)
            img_new[x,j,:]=image[i,j,:]
    return Image.fromarray(img_new.astype(np.uint8))
#Rotate image to x degree use polar coordinate
def rotate(img,degree):
    img_new = np.zeros([int(img.shape[0]*math.sqrt(2)),int(img.shape[1]*math.sqrt(2)),img.shape[2]])
    x0 = img.shape[0]/2.0
    y0 = img.shape[1]/2.0
    x1 = img_new.shape[0]/2.0
    y1 = img_new.shape[1]/2.0
    r = math.sqrt(x0*x0+y0*y0)
    a = degree*math.pi/180.0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = int(x1+(i-x0)*math.cos(a)+(j-y0)*math.sin(a))
            y = int(y1-(i-x0)*math.sin(a)+(j-y0)*math.cos(a))
            if x>=0 and x<img_new.shape[0] and y>=0 and y<img_new.shape[1]:
                img_new[x,y,:]=img[i,j,:]
    #Process the empty area
    for i in range(img_new.shape[0]):
        for j in range(img_new.shape[1]):
            if (img_new[i,j,:]==0).all():
                #Fill the empty area with the mean value of the nearest 8 pixels
                sum = np.zeros([1,3])
                count = 0
                for m in range(-1,2):
                    for n in range(-1,2):
                        if i+m>=0 and i+m<img_new.shape[0] and j+n>=0 and j+n<img_new.shape[1]:
                            sum = sum+img_new[i+m,j+n,:]
                            count = count+1
                img_new[i,j,:]=sum/count
    return Image.fromarray(img_new.astype(np.uint8))
filename="Lenna_(test_image).png"
img = np.array(Image.open(filename))
#Mirror image (Horizontal)
img2=img[::-1,:,:]
#Rotate image
img3=rotate(img,-45)
#Twist image
img4=twist(img,30)

#Show image
plt.figure(figsize=(10,10))
plt.subplot(1,4,1);plt.imshow(img);plt.title("Original");plt.axis("off")
plt.subplot(1,4,2);plt.imshow(img2);plt.title("Mirror");plt.axis("off")
plt.subplot(1,4,3);plt.imshow(img3);plt.title("Rotate");plt.axis("off")
plt.subplot(1,4,4);plt.imshow(img4);plt.title("Twist");plt.axis("off")
plt.show()
