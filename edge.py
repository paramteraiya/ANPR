import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("LicPlateImages/ind1.jpg")
#resized_img = cv2.resize(img, (1366, 768))
edges = cv2.Canny(img,100,200)
cv2.imshow('canny edge',edges)
cv2.imwrite('edges.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
