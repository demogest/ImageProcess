from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#Read image
im = np.array(Image.open('Lenna_(test_image).png').convert('L'))
#One-way first-order differential operator (vertical)
im1 = im[1:,:] - im[:-1,:]
#One-way first-order differential operator (horizontal)
im2 = im[:,1:] - im[:,:-1]
#Show image
plt.figure()
plt.subplot(131); plt.imshow(im, cmap='gray'); plt.axis('off'); plt.title('Original image')
plt.subplot(132); plt.imshow(im1, cmap='gray'); plt.axis('off'); plt.title('Vertical')
plt.subplot(133); plt.imshow(im2, cmap='gray'); plt.axis('off'); plt.title('Horizontal')
plt.show()