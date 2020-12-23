import cv2
img = cv2.imread("LicPlateImages/ind1.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray_img)
cv2.imwrite('gray_img.jpg', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
