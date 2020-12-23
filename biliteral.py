import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread("LicPlateImages/ind1.jpg")
resized_img = cv2.resize(img, (1366, 768))
gray_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(gray_img,-1,kernel)
cv2.imwrite('biliteral.jpg', gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

