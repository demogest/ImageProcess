import numpy as np
img = np.array([[0,0,0,1,0,0,0,0],[0,1,1,1,0,0,0,0],[0,0,1,1,1,1,0,0],[0,1,0,1,1,1,1,1],[0,1,0,1,1,1,0,0],[0,1,1,0,0,1,0,0]])
def calculate(img,p,q):
    m=0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            m+=pow(i+1,p)*pow(j+1,q)*img[i,j]
    return m
m10=calculate(img,1,0)
m01=calculate(img,0,1)
m00=calculate(img,0,0)
print("m10:",m10)
print("m01:",m01)
print("m00:",m00)
xm=m10/m00
ym=m01/m00
print("xm:",xm)
print("ym:",ym)
print("Center of gravity:", xm, ym)