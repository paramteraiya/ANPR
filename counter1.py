import numpy as np
import cv2 
img = cv2.imread("LicPlateImages/ind1.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
imS = cv2.resize(img, (960, 540)) 
cv2.imwrite('counter.jpg', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
