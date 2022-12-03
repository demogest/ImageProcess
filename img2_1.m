filename="E:\Lenna_(test_image).png";
img = imread(filename);
imgGray = rgb2gray(img);
imshow(img)
imshow(imgGray)
hist=imhist(imgGray);
figure
bar(hist)