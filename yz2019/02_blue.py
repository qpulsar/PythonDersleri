import cv2
import matplotlib
import numpy as np

img = cv2.imread('./images/ornek.png', cv2.IMREAD_UNCHANGED)
mavi = img[:, :, 0]

mavi_img = np.zeros(img.shape)
mavi_img[:, :, 0] = mavi
cv2.imshow('Siftah', img)
cv2.imshow('Mavi', mavi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
