import cv2


#img = cv2.imread('./230615/test.jpg', cv2.IMREAD_GRAYSCALE)

#img_small = cv2.resize(img, (200, 90))

img = cv2.imread('./230615/test.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width, channel = img.shape
print(height,width,channel)

img_crop = img[:, :int(width/2)]
img_blur = cv2.blur(img_crop, (10, 10))

#cv2.imshow('Original', img)
cv2.imshow('Original_Crop', img_crop)
cv2.imshow('blur', img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()