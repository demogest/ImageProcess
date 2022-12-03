import math
import numpy as np
img = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [
               90, 100, 110, 120], [130, 140, 150, 160]])
# Twist the image by 30 degrees Horizontal
a = math.tan(30*math.pi/180.0)
img_new = np.zeros([img.shape[0], int(img.shape[1]+img.shape[0]*a)])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        y = int(j+i*a)
        img_new[i, y] = img[i, j]
print(img_new)

img_new = np.zeros([int(img.shape[0]*math.sqrt(2)),
                   int(img.shape[1]*math.sqrt(2))])
x0 = img.shape[0]/2.0
y0 = img.shape[1]/2.0
x1 = img_new.shape[0]/2.0
y1 = img_new.shape[1]/2.0
r = math.sqrt(x0*x0+y0*y0)
a = 45*math.pi/180.0
positions=[]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = int(x1+(i-x0)*math.cos(a)+(j-y0)*math.sin(a))
        y = int(y1-(i-x0)*math.sin(a)+(j-y0)*math.cos(a))
        positions.append([x,y,i,j])
positions = np.array(positions)
minx = np.min(positions[:,0])
miny = np.min(positions[:,1])
for i in positions:
    img_new[i[0]-minx,i[1]-miny] = img[i[2],i[3]]
for i in positions:
    print(str(i[0])+" "+str(i[1]))
print(img_new)
