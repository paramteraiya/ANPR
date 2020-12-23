import cv2
img = cv2.imread("LicPlateImages/ind1.jpg")
resized_img = cv2.resize(img, (1366, 768))
cv2.imshow('resized',resized_img)
cv2.imwrite('resized.jpg', resized_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

